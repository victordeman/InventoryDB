#!/bin/bash
# Setup PostgreSQL database for InventoryDB
DB_NAME="inventorydb"
DB_USER="postgres"
DB_HOST="localhost"
DB_PORT="5432"
DB_PASSWORD="soft@1980"  # Replace with your PostgreSQL password

# Set PGPASSWORD to avoid password prompts
export PGPASSWORD=$DB_PASSWORD

echo "Creating database $DB_NAME..."
psql -U $DB_USER -h $DB_HOST -p $DB_PORT -c "CREATE DATABASE $DB_NAME;" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "Database created successfully."
else
    echo "Failed to create database. It may already exist. Attempting to proceed..."
fi

echo "Loading schema..."
psql -U $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f sql/schema.sql 2>/dev/null
if [ $? -eq 0 ]; then
    echo "Schema loaded successfully."
else
    echo "Failed to load schema."
    exit 1
fi

echo "Loading seed data..."
psql -U $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f sql/seed.sql 2>/dev/null
if [ $? -eq 0 ]; then
    echo "Seed data loaded successfully."
else
    echo "Failed to load seed data."
    exit 1
fi

echo "Setting up triggers..."
psql -U $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f sql/triggers.sql 2>/dev/null
if [ $? -eq 0 ]; then
    echo "Triggers set up successfully."
else
    echo "Failed to set up triggers."
    exit 1
fi

echo "Database setup complete!"
unset PGPASSWORD  # Clear password from environment
