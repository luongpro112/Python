# camera.py
from config import WORLD_WIDTH, WORLD_HEIGHT

class Camera:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

    def follow(self, target_x, target_y):
        """Giữ camera luôn căn giữa mục tiêu (Nhân vật)"""
        self.x = target_x - self.width // 2
        self.y = target_y - self.height // 2

        # Ràng buộc không cho Camera ra ngoài rìa bản đồ thế giới
        self.x = max(0, min(self.x, WORLD_WIDTH - self.width))
        self.y = max(0, min(self.y, WORLD_HEIGHT - self.height))

    def apply(self, world_x, world_y):
        """Chuyển tọa độ Thế giới (World) sang tọa độ Màn hình (Screen)"""
        return world_x - self.x, world_y - self.y