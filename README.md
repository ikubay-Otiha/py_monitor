# py-monitor

Python FastAPI ベースのCPU, メモリなどのモニタリングサービス。

## 🚀 環境セットアップ

### 1. 必要なもの

- Docker

### 2. .envファイルを作成し以下を記入

```.env
# ポート番号
PORT=3000

# ログファイルのパス（開発用）
LOG_FILE = "system_monitor.log"

```

### 3. Docker イメージのビルド

```sh
./build.sh
```

### 4. コンテナの起動

```sh
./run.sh
```

### 5. ログの確認

```sh
sudo docker logs -f py-monitor
```

### 6. 停止と削除

```sh
sudo docker stop py-monitor
sudo docker rm py-monitor
```