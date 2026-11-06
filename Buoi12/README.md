# Đồ án Buổi 12 – Quản lý tủ sách cá nhân

Ứng dụng desktop dùng Tkinter để quản lý sách, SQLite để lưu dữ liệu và Matplotlib để vẽ biểu đồ số lượng sách theo thể loại.

## Chạy ứng dụng

Từ thư mục gốc repository, dùng Python trong môi trường đã có sẵn:

```powershell
.\venv\Scripts\python.exe .\Buoi12\ung_dung_tu_sach.py
```

Ứng dụng tự tạo `tu_sach.db` trong thư mục `Buoi12` nếu cơ sở dữ liệu chưa có. Không cần tạo venv mới; máy cần có Matplotlib để chạy giao diện và biểu đồ.

## Chức năng

- Thêm sách với tên, tác giả và thể loại.
- Hiển thị danh sách, trạng thái đọc; kiểm tra trường bắt buộc.
- Đánh dấu sách đã đọc và xóa sách có xác nhận.
- Thống kê số sách theo thể loại dưới dạng biểu đồ cột.
- Giữ dữ liệu SQLite giữa các lần chạy.

## Cấu trúc

- `csdl_sach.py`: tạo bảng và cung cấp các thao tác SQLite.
- `ung_dung_tu_sach.py`: giao diện, kiểm tra dữ liệu nhập và biểu đồ.
- `tu_sach.db`: cơ sở dữ liệu mẫu gồm một số sách để thử các chức năng.

## Đóng gói (tùy chọn)

Trong thư mục `Buoi12`, chạy lệnh sau bằng môi trường có PyInstaller:

```powershell
pyinstaller --onefile --windowed ung_dung_tu_sach.py
```

Ứng dụng đóng gói lưu `tu_sach.db` cạnh file thực thi.
