#!/bin/bash
# Backup InventoryDB
DB_NAME="inventorydb"
BACKUP_DIR="backups"
TIMESTAMP=$(date +%F_%H-%M-%S)
BACKUP_FILE="${BACKUP_DIR}/inventorydb_${TIMESTAMP}.sql"

mkdir -p $BACKUP_DIR
pg_dump -U postgres $DB_NAME > $BACKUP_FILE
echo "Backup created at $BACKUP_FILE"
