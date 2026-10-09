# main.py
import tkinter as tk
import time
from config import (SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, FRAME_DELAY, 
                    WORLD_COLS, WORLD_ROWS, WORLD_WIDTH, WORLD_HEIGHT, TILE_TYPES, 
                    SEASONS, CROP_DATA, TOOLS)
from camera import Camera
from player import Player
from systems import TimeSystem, FarmingSystem

class StardewGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stardew Valley Engine - Part 2: Farming & Time")
        self.root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="#111")
        self.canvas.pack(fill="both", expand=True)

        self.keys_pressed = {}
        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.bind("<KeyRelease>", self.on_key_release)

        # Khởi tạo Hệ thống Game
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.player = Player(WORLD_WIDTH // 2, WORLD_HEIGHT // 2)
        self.world_map = self.create_world_map()

        self.time_sys = TimeSystem()
        self.farm_sys = FarmingSystem()

        # Bộ đếm thời gian trôi tự động (1.5s = 10 phút game)
        self.time_accumulator = 0

        self.game_loop()

    def create_world_map(self):
        grid = [[0 for _ in range(WORLD_COLS)] for _ in range(WORLD_ROWS)]
        for r in range(WORLD_ROWS):
            for c in range(WORLD_COLS):
                if r == 0 or r == WORLD_ROWS - 1 or c == 0 or c == WORLD_COLS - 1:
                    grid[r][c] = 5  # Wall
                elif 10 <= r <= 14 and 10 <= c <= 15:
                    grid[r][c] = 3  # Water
        return grid

    def on_key_press(self, event):
        key = event.keysym.lower()
        self.keys_pressed[key] = True

        # Đổi công cụ (Phím 1, 2, 3, 4)
        if event.char in TOOLS:
            self.farm_sys.current_tool = TOOLS[event.char]

        # Thực hiện thao tác làm nông (Phím J)
        elif key == "j":
            col, row = self.player.get_facing_tile()
            if 0 <= col < WORLD_COLS and 0 <= row < WORLD_ROWS:
                current_season = SEASONS[self.time_sys.season_idx]
                self.farm_sys.use_tool(col, row, current_season)

        # Đi ngủ sang ngày mới (Phím Space)
        elif key == "space":
            self.time_sys.next_day()
            current_season = SEASONS[self.time_sys.season_idx]
            self.farm_sys.process_day_change(current_season)

    def on_key_release(self, event):
        key = event.keysym.lower()
        self.keys_pressed[key] = False

    def update(self):
        self.player.handle_input(self.keys_pressed)
        self.player.update(self.world_map)
        self.camera.follow(self.player.x, self.player.y)

        # Cập nhật đồng hồ tự động
        self.time_accumulator += FRAME_DELAY
        if self.time_accumulator >= 1500:  # 1.5 giây trôi 10 phút
            self.time_accumulator = 0
            self.time_sys.advance_time(10)

            # Đêm muộn 2:00 sáng tự ngất xỉu
            if self.time_sys.hour == 2 and self.time_sys.minute == 0:
                self.time_sys.next_day()
                current_season = SEASONS[self.time_sys.season_idx]
                self.farm_sys.process_day_change(current_season)

    def render(self):
        self.canvas.delete("all")

        # 1. Frustum Culling: Chỉ vẽ vùng ô có trên màn hình
        start_col = max(0, int(self.camera.x // TILE_SIZE))
        end_col = min(WORLD_COLS, int((self.camera.x + SCREEN_WIDTH) // TILE_SIZE) + 2)
        start_row = max(0, int(self.camera.y // TILE_SIZE))
        end_row = min(WORLD_ROWS, int((self.camera.y + SCREEN_HEIGHT) // TILE_SIZE) + 2)

        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                world_x = col * TILE_SIZE
                world_y = row * TILE_SIZE
                screen_x, screen_y = self.camera.apply(world_x, world_y)

                # Kiếm tra xem ô này có thông tin nông trại không
                pos = (col, row)
                farm_tile = self.farm_sys.farmland.get(pos)

                if farm_tile:
                    if farm_tile["state"] == "tilled": color = "#834c32"      # Đất nâu khô
                    elif farm_tile["state"] == "watered": color = "#4b2c20"   # Đất ẩm tối
                    else: color = TILE_TYPES[self.world_map[row][col]]["color"]
                else:
                    color = TILE_TYPES[self.world_map[row][col]]["color"]

                # Vẽ nền đất
                self.canvas.create_rectangle(
                    screen_x, screen_y,
                    screen_x + TILE_SIZE, screen_y + TILE_SIZE,
                    fill=color, outline="#2c3e50" if color == "#4cd137" else ""
                )

                # Vẽ Cây trồng trên đất
                if farm_tile and farm_tile.get("crop"):
                    crop = farm_tile["crop"]
                    c_data = CROP_DATA[crop["type"]]
                    cx, cy = screen_x + TILE_SIZE // 2, screen_y + TILE_SIZE // 2

                    if crop["age"] >= c_data["growth"]:
                        self.canvas.create_text(cx, cy, text=c_data["icon"], font=("Arial", 18))
                    else:
                        self.canvas.create_text(cx, cy, text="🌱", font=("Arial", 12))

        # 2. Highlight ô nhắm tới
        f_col, f_row = self.player.get_facing_tile()
        if 0 <= f_col < WORLD_COLS and 0 <= f_row < WORLD_ROWS:
            hx, hy = self.camera.apply(f_col * TILE_SIZE, f_row * TILE_SIZE)
            self.canvas.create_rectangle(
                hx, hy, hx + TILE_SIZE, hy + TILE_SIZE,
                outline="yellow", width=3
            )

        # 3. Vẽ Nhân vật
        px, py = self.camera.apply(self.player.x, self.player.y)
        r = self.player.radius
        self.canvas.create_oval(px - r, py - r, px + r, py + r, fill="#f1c40f", outline="white", width=2)

        # 4. Hiệu ứng làm tối màn hình vào ban đêm
        if self.time_sys.is_night():
            self.canvas.create_rectangle(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, fill="#000033", stipple="gray50")

        # 5. Giao diện HUD
        season_name = SEASONS[self.time_sys.season_idx]
        time_str = f"{self.time_sys.hour:02d}:{self.time_sys.minute:02d}"
        inv = self.farm_sys.inventory

        hud_bg = self.canvas.create_rectangle(10, 10, 380, 85, fill="#1e272e", outline="")
        info_text = (f"📅 Day {self.time_sys.day} ({season_name}) | ⏰ {time_str}\n"
                     f"💰 {inv['Gold']}G | ⚡ Energy: {inv['Energy']}/{inv['Max_Energy']}\n"
                     f"🔧 Tool: [{self.farm_sys.current_tool}] (1-4) | [J]: Dùng | [Space]: Đi ngủ")
        self.canvas.create_text(20, 20, text=info_text, fill="#fbc531", anchor="nw", font=("Consolas", 10, "bold"))

    def game_loop(self):
        self.update()
        self.render()
        self.root.after(FRAME_DELAY, self.game_loop)

if __name__ == "__main__":
    root = tk.Tk()
    app = StardewGameApp(root)
    root.mainloop()