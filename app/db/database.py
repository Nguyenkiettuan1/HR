from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

# Khởi tạo kết nối MongoDB
client = AsyncIOMotorClient(settings.mongodb_url)

# Lựa chọn Database
db = client[settings.mongodb_db_name]

# Dependency để inject database vào router
async def get_db():
    return db
