# systems.py
from config import SEASONS, CROP_DATA, WORLD_COLS, WORLD_ROWS

class TimeSystem:
    def __init__(self):
        self.day = 1
        self.season_idx = 0  # 0: Spring, 1: Summer, 2: Fall, 3: Winter
        self.hour = 6
        self.minute = 0

    def advance_time(self, minutes=10):
        self.minute += minutes
        if self.minute >= 60:
            self.minute = 0
            self.hour += 1

    def is_night(self):
        return self.hour >= 22 or self.hour < 6

    def next_day(self):
        self.day += 1
        self.hour = 6
        self.minute = 0
        if self.day > 28:
            self.day = 1
            self.season_idx = (self.season_idx + 1) % 4


class FarmingSystem:
    def __init__(self):
        # Lưu trạng thái đất đai: (col, row) -> {"state": "grass/tilled/watered", "crop": None/dict}
        self.farmland = {}
        self.inventory = {
            "Gold": 500,
            "Energy": 100,
            "Max_Energy": 100,
            "Parsnip Seed": 5,
            "Tomato Seed": 2,
            "Parsnip": 0,
            "Tomato": 0,
            "Pumpkin": 0
        }
        self.current_tool = "Hoe"

    def use_tool(self, col, row, current_season):
        if self.inventory["Energy"] < 2:
            return "Khung năng lượng quá thấp!"

        pos = (col, row)
        tile_data = self.farmland.get(pos, {"state": "grass", "crop": None})

        # 1. CUỐC ĐẤT (Hoe)
        if self.current_tool == "Hoe":
            if tile_data["state"] == "grass":
                tile_data["state"] = "tilled"
                self.inventory["Energy"] -= 2
                self.farmland[pos] = tile_data

        # 2. TƯỚI NƯỚC (WaterCan)
        elif self.current_tool == "WaterCan":
            if tile_data["state"] in ["tilled", "watered"]:
                tile_data["state"] = "watered"
                self.inventory["Energy"] -= 1
                self.farmland[pos] = tile_data

        # 3. GIEO HẠT (Seed)
        elif self.current_tool == "Seed":
            if tile_data["state"] in ["tilled", "watered"] and tile_data["crop"] is None:
                # Tìm hạt giống phù hợp mùa
                for crop_name, data in CROP_DATA.items():
                    seed_key = f"{crop_name} Seed"
                    if data["season"] == current_season and self.inventory.get(seed_key, 0) > 0:
                        self.inventory[seed_key] -= 1
                        tile_data["crop"] = {"type": crop_name, "age": 0}
                        self.inventory["Energy"] -= 2
                        self.farmland[pos] = tile_data
                        break

        # 4. THU HOẠCH (Harvest)
        elif self.current_tool == "Harvest":
            crop = tile_data.get("crop")
            if crop:
                c_data = CROP_DATA[crop["type"]]
                if crop["age"] >= c_data["growth"]:
                    self.inventory[crop["type"]] += 1
                    tile_data["crop"] = None
                    tile_data["state"] = "tilled"
                    self.inventory["Energy"] -= 1
                    self.farmland[pos] = tile_data

    def process_day_change(self, new_season):
        """Xử lý cây lớn lên và đất khô lại vào ngày mới"""
        self.inventory["Energy"] = self.inventory["Max_Energy"]

        for pos, tile_data in list(self.farmland.items()):
            crop = tile_data.get("crop")
            
            # Nếu có cây trồng
            if crop:
                c_data = CROP_DATA[crop["type"]]
                # Kiểm tra chết trái mùa
                if c_data["season"] != new_season:
                    tile_data["crop"] = None
                    tile_data["state"] = "grass"
                else:
                    # Nếu được tưới nước ngày hôm trước -> Cây lớn 1 tuổi
                    if tile_data["state"] == "watered":
                        crop["age"] += 1

            # Đất khô lại sau một đêm
            if tile_data["state"] == "watered":
                tile_data["state"] = "tilled"