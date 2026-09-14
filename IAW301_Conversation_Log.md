# IAW301 - Conversation Log (Prompt & Answer)

> Nhật ký trao đổi giữa người dùng và ChatGPT cho dự án FastAPI + SQLite.

---

## Phiên 1 – Chuẩn bị môi trường

### Prompt
Bắt đầu từ môi trường Miniconda `nhipty`.

### Answer
- Kích hoạt `conda activate nhipty`.
- Cài `fastapi`, `uvicorn`, `jinja2`, `python-multipart`.

---

## Phiên 2 – Tạo Database

### Prompt
Tạo SQLite theo sơ đồ trên bảng.

### Answer
- Tạo `users.db`.
- Tạo bảng `users`.
- Thêm tài khoản mẫu `admin / admin@gmail.com / 123456`.

---

## Phiên 3 – Chạy FastAPI

### Prompt
Chạy server bằng Uvicorn.

### Answer
- `uvicorn app:app --reload`.
- Kiểm tra `/` và `/ping`.

---

## Phiên 4 – Login Form

### Prompt
Hiển thị giao diện đăng nhập.

### Answer
- Tạo `templates/login.html`.
- Thêm endpoint `/login-form`.

---

## Phiên 5 – Sửa lỗi Internal Server Error

### Prompt
Lỗi `TypeError: unhashable type: 'dict'`.

### Answer
- Sửa `TemplateResponse` sang cú pháp mới:
  - `request=request`
  - `name="login.html"`
  - `context={"request": request}`

---

## Phiên 6 – Login với SQLite

### Prompt
Kết nối form với database.

### Answer
- Thêm `POST /login`.
- Kiểm tra `username/email` và `password` trong SQLite.

---

## Phiên 7 – Endpoint `/all`

### Prompt
Thêm endpoint `/all` hiển thị toàn bộ user dưới dạng bảng.

### Answer
- Tạo `templates/all.html`.
- Dùng `fetchall()` để lấy toàn bộ user.
- Render bằng Jinja2.

---

# Quy ước cập nhật

Sau mỗi lần trao đổi, sẽ thêm:

## Phiên X

### Prompt
(Câu hỏi của người dùng)

### Answer
(Lời giải và hướng dẫn đã thực hiện)