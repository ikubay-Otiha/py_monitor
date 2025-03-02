#!/bin/bash

# エラーハンドリング（エラーが発生したらスクリプトを停止）
set -e

# ログファイル
LOG_FILE="build.log"

echo "Starting Docker build..." | tee "$LOG_FILE"

# Docker ビルドの実行
if sudo docker build -t py-monitor . 2>&1 | tee -a "$LOG_FILE"; then
    echo "✅ Docker image built successfully." | tee -a "$LOG_FILE"
else
    echo "❌ Docker build failed. Check the log file: $LOG_FILE" | tee -a "$LOG_FILE"
    exit 1
fi
