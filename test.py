import tkinter as tk
import random

# CẤU HÌNH HỆ THỐNG
SCREEN_W, SCREEN_H = 800, 550
TILE_SIZE = 40

class StardewUltimate:
    def __init__(self, root):
        self.root = root
        self.root.title("Stardew Valley Full Systems - Tkinter Edition")
        self.root.resizable(False, False)

        # 1. CHỈ SỐ NHÂN VẬT & TÀI NGUYÊN
        self.gold = 500
        self.energy = 100
        self.max_energy = 100
        self.hp = 100
        self.max_hp = 100
        
        # Vị trí & Chế độ chơi (FARM, MINE, FISHING)
        self.mode = "FARM"  
        self.px, self.py = 2, 2

        # Túi đồ & NPC
        self.inventory = {"Parsnip Seed": 5, "Parsnip": 2, "Copper Ore": 0, "Fish": 0}
        self.npc_hearts = {"Abigail": 0, "Pierre": 0}
        self.npc_locations = {"Abigail": (8, 2), "Pierre": (8, 6)}

        # Mỏ đá & Quái vật (Mine System)
        self.mine_floor = 1
        self.monsters = []  # Danh sách quái Slime [(x, y, hp)]
        self.rocks = []     # Đá trong mỏ [(x, y)]

        # Khởi tạo Nông trại
        self.farm_grid = {}
        for x in range(10):
            for y in range(10):
                self.farm_grid[(x, y)] = {"state": "grass", "crop": None}

        # GIAO DIỆN
        self.setup_ui()
        self.root.bind("<Key>", self.handle_input)
        self.draw()

    def setup_ui(self):
        self.frame_top = tk.Frame(self.root, bg="#1e272e")
        self.frame_top.pack(fill="x")

        self.lbl_info = tk.Label(self.frame_top, text="", font=("Consolas", 10, "bold"), fg="#fbc531", bg="#1e272e")
        self.lbl_info.pack(pady=5)

        self.canvas = tk.Canvas(self.root, width=SCREEN_W, height=SCREEN_H, bg="#2ed573")
        self.canvas.pack()

    def update_ui_text(self):
        txt = (f"📍 Khu vực: [{self.mode}] | 💰 {self.gold}G | ⚡ Thể lực: {self.energy}/{self.max_energy} | ❤️ Máu: {self.hp}/{self.max_hp}\n"
               f"💕 Thân thiết: Abigail ({self.npc_hearts['Abigail']}❤️) | Pierre ({self.npc_hearts['Pierre']}❤️) | 🎒 Bắt cá: {self.inventory['Fish']} | Quặng: {self.inventory['Copper Ore']}")
        self.lbl_info.config(text=txt)

    def handle_input(self, event):
        key = event.keysym.lower()

        # 1. CHUYỂN ĐỔI KHU VỰC (Phím M)
        if key == "m":
            if self.mode == "FARM":
                self.mode = "MINE"
                self.enter_mine()
            else:
                self.mode = "FARM"
                self.canvas.config(bg="#2ed573")

        # 2. DI CHUYỂN (WASD)
        if key == "w" and self.py > 0: self.py -= 1
        elif key == "s" and self.py < 9: self.py += 1
        elif key == "a" and self.px > 0: self.px -= 1
        elif key == "d" and self.px < 9: self.px += 1

        # 3. TƯƠNG TÁC THEO KHU VỰC
        if self.mode == "FARM":
            if key == "j":  # Cuốc đất / Trồng cây
                pos = (self.px, self.py)
                if self.farm_grid[pos]["state"] == "grass" and self.energy >= 5:
                    self.farm_grid[pos]["state"] = "tilled"
                    self.energy -= 5
            elif key == "f":  # Bắt đầu Minigame Câu cá
                self.start_fishing_minigame()

            # Tặng quà NPC (Phím G)
            elif key == "g":
                for npc, loc in self.npc_locations.items():
                    if (self.px, self.py) == loc:
                        if self.inventory["Parsnip"] > 0:
                            self.inventory["Parsnip"] -= 1
                            self.npc_hearts[npc] += 1
                            print(f"Đã tặng Parsnip cho {npc}! +1 Heart")

        elif self.mode == "MINE":
            if key == "j":  # Đánh quái / Khai thác đá
                self.attack_in_mine()

        self.update_ui_text()
        self.draw()

    # --- HỆ THỐNG MỎ ĐÁ & CHIẾN ĐẤU ---
    def enter_mine(self):
        self.canvas.config(bg="#3d3d3d")
        self.monsters = [(random.randint(3, 8), random.randint(3, 8), 20) for _ in range(2)]
        self.rocks = [(random.randint(1, 8), random.randint(1, 8)) for _ in range(5)]

    def attack_in_mine(self):
        if self.energy < 3: return
        self.energy -= 3

        # Đập đá lấy quặng
        if (self.px, self.py) in self.rocks:
            self.rocks.remove((self.px, self.py))
            self.inventory["Copper Ore"] += 1

        # Tấn công Slime gần kề
        for i, (mx, my, mhp) in enumerate(self.monsters):
            if abs(self.px - mx) <= 1 and abs(self.py - my) <= 1:
                mhp -= 10
                if mhp <= 0:
                    self.monsters.pop(i)
                    self.gold += 15
                else:
                    self.monsters[i] = (mx, my, mhp)
                    # Quái đánh lại
                    self.hp -= 5

    # --- MINIGAME CÂU CÁ ---
    def start_fishing_minigame(self):
        if self.energy < 5: return
        self.energy -= 5
        
        # Mở cửa sổ Minigame căn lực
        fish_win = tk.Toplevel(self.root)
        fish_win.title("Fishing Minigame")
        fish_win.geometry("300x150")

        lbl = tk.Label(fish_win, text="Nhấn [SPACE] khi thanh màu xanh vào giữa!", font=("Arial", 10))
        lbl.pack(pady=10)

        canvas_fish = tk.Canvas(fish_win, width=200, height=30, bg="gray")
        canvas_fish.pack()

        # Vùng mục tiêu câu cá
        canvas_fish.create_rectangle(80, 0, 120, 30, fill="green")
        line = canvas_fish.create_line(0, 0, 0, 30, fill="red", width=3)

        pos = [0]
        direction = [5]

        def animate():
            pos[0] += direction[0]
            if pos[0] >= 200 or pos[0] <= 0:
                direction[0] *= -1
            canvas_fish.coords(line, pos[0], 0, pos[0], 30)
            if fish_win.winfo_exists():
                fish_win.after(30, animate)

        def catch(event):
            if 80 <= pos[0] <= 120:
                self.inventory["Fish"] += 1
                lbl.config(text="BẮT ĐƯỢC CÁ! 🎉", fg="green")
            else:
                lbl.config(text="CÁ CẮN HỤT! ❌", fg="red")
            fish_win.after(800, fish_win.destroy)

        fish_win.bind("<space>", catch)
        animate()

    def draw(self):
        self.canvas.delete("all")

        # 1. VẼ NÔNG TRẠI
        if self.mode == "FARM":
            for (x, y), cell in self.farm_grid.items():
                sx, sy = x * TILE_SIZE + 20, y * TILE_SIZE + 20
                color = "#834c32" if cell["state"] == "tilled" else "#2ed573"
                self.canvas.create_rectangle(sx, sy, sx + TILE_SIZE, sy + TILE_SIZE, fill=color, outline="#1e272e")

            # Vẽ NPC
            for npc, (nx, ny) in self.npc_locations.items():
                nsx, nsy = nx * TILE_SIZE + 20, ny * TILE_SIZE + 20
                self.canvas.create_rectangle(nsx + 5, nsy + 5, nsx + 35, nsy + 35, fill="#e84118")
                self.canvas.create_text(nsx + 20, nsy + 20, text=npc[0], fill="white", font=("Arial", 12, "bold"))

        # 2. VẼ MỎ ĐÁ
        elif self.mode == "MINE":
            for (rx, ry) in self.rocks:
                rsx, rsy = rx * TILE_SIZE + 20, ry * TILE_SIZE + 20
                self.canvas.create_oval(rsx + 5, rsy + 5, rsx + 35, rsy + 35, fill="#718093")

            for (mx, my, _) in self.monsters:
                msx, msy = mx * TILE_SIZE + 20, my * TILE_SIZE + 20
                self.canvas.create_oval(msx + 5, msy + 5, msx + 35, msy + 35, fill="#44bd32")

        # 3. VẼ NHÂN VẬT CHÍNH
        psx, psy = self.px * TILE_SIZE + 20, self.py * TILE_SIZE + 20
        self.canvas.create_oval(psx + 4, psy + 4, psx + 36, psy + 36, fill="#f1c40f", outline="white", width=2)

        # Bảng hướng dẫn
        guide = ("[WASD]: Di chuyển | [M]: Đổi vị trí (Farm / Mỏ đá)\n"
                 "[J]: Cuốc đất (Farm) hoặc Đánh/Đào (Mỏ đá)\n"
                 "[F]: Câu cá | [G]: Tặng Parsnip cho NPC gần kề")
        self.canvas.create_text(220, 480, text=guide, font=("Arial", 9, "bold"), fill="#2c3e50")

if __name__ == "__main__":
    root = tk.Tk()
    app = StardewUltimate(root)
    root.mainloop()