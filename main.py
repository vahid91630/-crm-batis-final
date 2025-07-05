from fastapi import FastAPI
from routers import customer_router
import uvicorn

app = FastAPI()

# اتصال روت مخصوص مشتری‌ها
app.include_router(customer_router.router, prefix="/customers")

# روت اصلی برای تست
@app.get("/")
def read_root():
    return {"message": "به سیستم مدیریت مشتری خوش آمدید"}

# اجرای مستقیم با Uvicorn در حالت لوکال
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
