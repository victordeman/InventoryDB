# InventoryDB

# InventoryDB

**InventoryDB** is a PostgreSQL-based inventory management system with a Streamlit web interface, designed to efficiently manage products and categories. It demonstrates robust database design, automation with Linux bash scripts, and a user-friendly frontend for inventory operations. This project highlights skills in database administration, scripting, and frontend development, making it ideal for showcasing technical expertise in a professional setting.

## Features

- **Database Management**: PostgreSQL schema with tables for products and categories, optimized with indexes and triggers for data integrity and performance.
- **Streamlit Interface**: Intuitive web UI to view inventory, add new products, and update stock quantities in real-time.
- **Automation**: Bash scripts for database setup (`scripts/setup.sh`) and backups (`scripts/backup.sh`) to streamline operations.
- **Documentation**: Comprehensive guides, including an Entity-Relationship Diagram (ERD) in `docs/ERD.md`.
- **Testing**: Basic unit tests for database connectivity and operations in `tests/`.

## Tech Stack

- **Database**: PostgreSQL
- **Frontend**: Streamlit, Pandas
- **Backend**: Python (psycopg2 for database connectivity)
- **Scripting**: Linux Bash
- **Version Control**: Git

## Getting Started

### Prerequisites

- PostgreSQL installed (`sudo apt-get install postgresql` on Ubuntu)
- Python 3.8+ and pip
- Git for cloning the repository

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/victordeman/InventoryDB
   cd InventoryDB

2. **Install Python Dependencies**:
   ```bash
   pip install -r scripts/requirements.txt

3. **Set Up PostgreSQL:Ensure PostgreSQL is running and accessible**:
   - Update app/config.py with your PostgreSQL credentials (e.g., password).
   - Run the database setup script:bash 

4. **Launch the Streamlit App**:
   ```bash
   streamlit run app/main.py

   - Open your browser to http://localhost:8501 to access the app.
