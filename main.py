# 月語 Moon Whisper - 後端 API 邏輯架構 (FastAPI 版)
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Moon Whisper API 伺服器運行中"}

@app.post("/sync-data")
def sync_data(uid: str, steps: int, heart_rate: int):
    # 這裡負責接收每 5 分鐘一次的數據同步
    return {"status": "success", "message": f"使用者 {uid} 數據已存入資料庫"}

@app.post("/reset-password")
def reset_password(email: str):
    # 這裡負責串接 SMTP 發送密碼重設連結
    return {"status": "success", "message": f"重設連結已發送至 {email}"}

@app.get("/rag-monitor")
def get_low_confidence_queries():
    # 模擬從資料庫抓取置信度低於 50% 的 AI 對話
    return [
        {"query": "疫苗影響經期", "confidence": 0.42},
        {"query": "心率異常處置", "confidence": 0.35}
    ]
