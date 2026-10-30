import requests

# Bài tập 5.1: Gọi API công khai
print("--- Bài 5.1 ---")
response = requests.get("https://api.github.com/repos/python/cpython")
if response.status_code == 200:
    du_lieu = response.json()
    print("Tên repository:", du_lieu["full_name"])
    print("Số lượt gắn sao (stars):", du_lieu["stargazers_count"])
    print("Ngôn ngữ chính:", du_lieu["language"])
else:
    print("Gọi API thất bại, mã lỗi:", response.status_code)

# Bài tập 5.2: Vận dụng API tỷ giá ngoại tệ (Cần mạng)
print("\n--- Bài 5.2 ---")
response_ty_gia = requests.get("https://open.er-api.com/v6/latest/USD")
if response_ty_gia.status_code == 200:
    du_lieu_ty_gia = response_ty_gia.json()
    ty_gia_vnd = du_lieu_ty_gia["rates"]["VND"]
    print(f"1 USD = {ty_gia_vnd:,.0f} VND")
else:
    print("Không lấy được tỷ giá, mã lỗi:", response_ty_gia.status_code)