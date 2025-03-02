FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係をコピー
COPY pyproject.toml .

# 依存関係をインストール
RUN pip install uv && uv venv && uv pip install --no-cache-dir -r pyproject.toml

# ソースコードをコピー
COPY src /app/src

# .envファイルをコピー
COPY .env .

# ログファイルを生成する
RUN touch /app/system_monitor.log

# 3001ポートを公開
EXPOSE 3000

# サーバーを起動
CMD [".venv/bin/uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3000"]