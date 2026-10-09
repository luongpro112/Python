# player.py
from config import TILE_SIZE, TILE_TYPES, WORLD_COLS, WORLD_ROWS

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 18
        self.speed = 4.0
        
        self.vx = 0
        self.vy = 0
        self.facing = "DOWN"  # UP, DOWN, LEFT, RIGHT
        self.interact_dist = 30

    def handle_input(self, keys_pressed):
        self.vx = 0
        self.vy = 0

        if keys_pressed.get("w") or keys_pressed.get("Up"):
            self.vy = -self.speed
            self.facing = "UP"
        if keys_pressed.get("s") or keys_pressed.get("Down"):
            self.vy = self.speed
            self.facing = "DOWN"
        if keys_pressed.get("a") or keys_pressed.get("Left"):
            self.vx = -self.speed
            self.facing = "LEFT"
        if keys_pressed.get("d") or keys_pressed.get("Right"):
            self.vx = self.speed
            self.facing = "RIGHT"

        # Chuẩn hóa tốc độ khi đi đường chéo
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def update(self, world_map):
        next_x = self.x + self.vx
        next_y = self.y + self.vy

        # Kiểm tra va chạm riêng biệt cho từng trục X và Y
        if not self.check_collision(next_x, self.y, world_map):
            self.x = next_x
        if not self.check_collision(self.x, next_y, world_map):
            self.y = next_y

    def check_collision(self, check_x, check_y, world_map):
        margin = self.radius - 2
        points = [
            (check_x - margin, check_y - margin),
            (check_x + margin, check_y - margin),
            (check_x - margin, check_y + margin),
            (check_x + margin, check_y + margin)
        ]

        for px, py in points:
            col = int(px // TILE_SIZE)
            row = int(py // TILE_SIZE)

            if col < 0 or col >= WORLD_COLS or row < 0 or row >= WORLD_ROWS:
                return True

            tile_id = world_map[row][col]
            if TILE_TYPES[tile_id]["solid"]:
                return True

        return False

    def get_facing_tile(self):
        """Lấy tọa độ ô vuông (col, row) ngay trước mặt nhân vật"""
        target_x = self.x
        target_y = self.y

        if self.facing == "UP": target_y -= self.interact_dist
        elif self.facing == "DOWN": target_y += self.interact_dist
        elif self.facing == "LEFT": target_x -= self.interact_dist
        elif self.facing == "RIGHT": target_x += self.interact_dist

        col = int(target_x // TILE_SIZE)
        row = int(target_y // TILE_SIZE)
        return col, row