FROM python:3.11-alpine
WORKDIR /app

# psutilをビルドするのに必要なパッケージをインストール
RUN apk add --no-cache gcc python3-dev musl-dev linux-headers

# requirements.txtを作成して依存関係をインストール
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY src /app/src
COPY .env .
RUN touch /app/system_monitor.log

EXPOSE 3000
CMD ["python3", "-m", "src.main"]