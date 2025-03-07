Cài Đặt & Chạy Hệ Thống
🔹 1. Clone Dự Án
git clone https://github.com/your-username/your-repo.git
cd fastapi-system

🔹 2. Tạo Môi Trường Ảo & Cài Đặt Package
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

🔹 3. Cấu Hình .env

Tạo file .env và thêm cấu hình email:
DB_USERNAME=YOUR DATABASE
DB_PASSWORD=PASSWORD
DB_HOSTNAME=localhost
DB_PORT=YOUR PORT
DB_NAME=YOUR DATAVASE NAME
DATABASE_URL=postgresql://user:password@localhost/db_name

📌 3️⃣ Cấu Hình Database & Alembic
📌 Tạo Migration & Cập Nhật Database
🔹 1. Khởi Tạo Alembic
alembic init alembic
🔹 2. Kiểm Tra Cấu Trúc Alembic
mkdir alembic/versions  # Đảm bảo thư mục chứa migration đã tồn tại
ls alembic  # Kiểm tra các file đã tạo

📌 Cấu trúc Alembic sẽ có:
alembic.ini
env.py
script.py.mako
versions/   # Chứa các migration files

🔹 3. Tạo & Áp Dụng Migration

alembic revision --autogenerate -m "Initial Migration"
alembic upgrade head
📌 Sau bước này, database của bạn đã được cập nhật! 🎉

📌 4️⃣ Chạy FastAPI
uvicorn main:app --reload
📌 FastAPI sẽ chạy tại:
👉 http://127.0.0.1:8000/docs (Giao diện API tự động)
👉 http://127.0.0.1:8000/redoc (Tài liệu API)

📌 5️⃣ Cấu Trúc Dự Án
📂 fastapi-system
│── 📂 app
│   ├── 📂 models          # SQLAlchemy Models
│   ├── 📂 routes          # API Routes
│   ├── 📂 schemas         # Pydantic Schemas
│   ├── 📂 services        # Business Logic
│   ├── 📂 utils           # Helper Functions
│   ├── __init__.py
│── 📂 alembic             # Alembic Migrations
│   ├── env.py
│   ├── script.py.mako
│   ├── versions/          # Chứa file migration
│── main.py                # FastAPI Entry Point
│── requirements.txt       # Dependencies
│── .env                   # Environment Variables
│── README.md              # Documentation

Cài Đặt & Chạy Hệ Thống
🔹 1. Clone Dự Án
git clone code về 
cd fastapi-ai-assistant

🔹 2. Cài Đặt Môi Trường Ảo

python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate      # Windows


🔹 3. Cài Đặt Các Gói Cần Thiết
pip install -r requirements.txt

🔹 4. Cấu Hình .env
Tạo file .env 

# Database Config
DB_USERNAME=YOUR DATABASE
DB_PASSWORD=PASSWORD
DB_HOSTNAME=localhost
DB_PORT=YOUR PORT
DB_NAME=YOUR DATAVASE NAME

# JWT Config
SECRET_KEY=mysecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

🔹 5. Chạy FastAPI Backend
uvicorn main:app --reload
FastAPI sẽ chạy tại: 👉 http://127.0.0.1:8000/docs

📂 fastapi-ai-assistant
│── 📂 app
│   ├── 📂 models          # Models (SQLAlchemy)
│   ├── 📂 routes          # API Endpoints
│   ├── 📂 schemas         # Pydantic Schemas
│   ├── 📂 services        # Business Logic
│   ├── 📂 utils           # Helper Functions
│   ├── __init__.py
│── main.py                # FastAPI Entry Point
│── requirements.txt       # Dependencies
│── .env                   # Environment Variables
│── README.md              # Documentation








