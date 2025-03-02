import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI

from src.lib.utils import write_log_info, get_env_files
from src.routers import log, root

# load .env file
dotenv.load_dotenv()

app = FastAPI()

# add API routers
app.include_router(root.router)
app.include_router(log.router)

if __name__ == "__main__":
    import uvicorn

    # ログファイルのパスを取得
    log_file_path = get_env_files()

    # スケジューラの起動
    scheduler = BackgroundScheduler()
    scheduler.add_job(write_log_info, "interval", seconds=10, args=[log_file_path])
    scheduler.start()

    # 環境変数からポート番号を取得、デフォルトは3000
    port = int(os.getenv("PORT", 3000))
    uvicorn.run(app, host="0.0.0.0", port=port)
