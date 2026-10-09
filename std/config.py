# config.py
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 48         # Kích thước ô vuông (48x48 px)
FPS = 60               # Khung hình mục tiêu
FRAME_DELAY = int(1000 / FPS)

# Kích thước thế giới (Tính theo số ô tile)
WORLD_COLS = 50
WORLD_ROWS = 50
WORLD_WIDTH = WORLD_COLS * TILE_SIZE
WORLD_HEIGHT = WORLD_ROWS * TILE_SIZE

# Bảng màu các loại địa hình (Tile Types)
TILE_TYPES = {
    0: {"name": "Grass",       "color": "#4cd137", "solid": False},
    1: {"name": "Soil_Dry",    "color": "#8c7ae6", "solid": False},
    2: {"name": "Soil_Wet",    "color": "#273c75", "solid": False},
    3: {"name": "Water",       "color": "#00a8ff", "solid": True},
    4: {"name": "Wood_Fence",  "color": "#e1b12c", "solid": True},
    5: {"name": "Stone_Wall",  "color": "#7f8fa6", "solid": True},
    6: {"name": "Tree_Trunk",  "color": "#44bd32", "solid": True},
}
# --- BỔ SUNG CHO PHẦN 2 (config.py) ---
SEASONS = ["Spring", "Summer", "Fall", "Winter"]

# Dữ liệu cây trồng: Tên, Mùa, Số ngày lớn, Giá bán, Icon
CROP_DATA = {
    "Parsnip": {"season": "Spring", "growth": 4, "buy": 20, "sell": 35, "icon": "🥕"},
    "Tomato":  {"season": "Summer", "growth": 6, "buy": 50, "sell": 80, "icon": "🍅"},
    "Pumpkin": {"season": "Fall",   "growth": 8, "buy": 100, "sell": 250, "icon": "🎃"}
}

# Công cụ
TOOLS = {
    "1": "Hoe",       # Cuốc đất
    "2": "WaterCan",  # Bình tưới nước
    "3": "Seed",      # Gieo hạt
    "4": "Harvest"    # Thu hoạch
}