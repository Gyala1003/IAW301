import sqlite3

# Kết nối (nếu chưa có file users.db thì sẽ tự tạo)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Tạo bảng users
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT
)
""")

# Thêm tài khoản mẫu
cursor.execute("""
INSERT OR IGNORE INTO users (username, email, password)
VALUES ('admin', 'admin@gmail.com', '123456')
""")

conn.commit()
conn.close()

print("Database created successfully!")