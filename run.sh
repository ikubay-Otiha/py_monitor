#!/bin/bash

# 古いコンテナがある場合、削除
if sudo docker ps -a --format '{{.Names}}' | grep -q '^py-monitor$'; then
    echo "Stopping and removing existing container..."
    sudo docker stop py-monitor && sudo docker rm py-monitor
fi

# 新しいコンテナを起動
echo "Starting Docker container..."
sudo docker run -d -p 3000:3000 -e PORT=3000 --name py-monitor \
    --volume /proc:/host_proc:ro \
    --privileged \
    py-monitor
    
# ステータス確認
echo "Docker container started successfully."
echo "Running containers:"
sudo docker ps