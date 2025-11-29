#!/bin/bash

# === CONFIG ===
DATA_DIR="/home/ubuntu/minecraft-server/data"
BACKUP_DIR="/home/ubuntu/backups"
DATE=$(date +"%Y-%m-%d_%H-%M")
BACKUP_NAME="minecraft-backup-$DATE.zip"

# Create backup folder if it doesn't exist
mkdir -p "$BACKUP_DIR"

echo "Starting Minecraft optimized backup from $DATA_DIR…"

cd "$DATA_DIR" || exit

zip -r "$BACKUP_DIR/$BACKUP_NAME" \
    world \
    world_nether \
    world_the_end \
    server.properties \
    whitelist.json \
    ops.json \
    plugins \
    *.jar \
    -x "logs/*" \
    -x "cache/*" \
    -x "crash-reports/*" \
    -x "libraries/*"

echo "Backup completed: $BACKUP_DIR/$BACKUP_NAME"
echo "File size: $(du -h $BACKUP_DIR/$BACKUP_NAME | cut -f1)"
