#!/bin/bash
# Setup PostgreSQL database for InventoryDB
DB_NAME="inventorydb"
DB_USER="postgres"
DB_HOST="localhost"
DB_PORT="5432"

echo "Creating database ..."
psql -U $DB_USER -h $DB_HOST -p $DB_PORT -c "CREATE DATABASE ;"

echo "Loading schema..."
psql -U $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f ../sql/schema.sql

echo "Loading seed data..."
psql -U $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f ../sql/seed.sql

echo "Setting up triggers..."
psql -U $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f ../sql/triggers.sql

echo "Database setup complete!"
