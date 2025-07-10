# InventoryDB

InventoryDB/
├── db/
│   ├── schema.sql              # PostgreSQL schema for inventory tables
│   ├── init_data.sql           # Sample data for testing
│   ├── queries.sql             # Common SQL queries (e.g., stock reports)
│   └── triggers.sql            # Triggers and stored procedures
├── scripts/
│   ├── setup.sh                # Bash script for DB setup and initialization
│   ├── backup.sh               # Script for automated database backups
│   └── monitor.sh              # Script for monitoring DB performance
├── app/
│   ├── main.py                 # Streamlit app main file
│   ├── requirements.txt        # Python dependencies for Streamlit
│   ├── config.yaml             # Configuration for DB connection and app settings
│   └── utils/
│       ├── db_connect.py       # Database connection logic
│       └── helpers.py          # Helper functions for Streamlit app
├── tests/
│   ├── test_queries.py         # Unit tests for SQL queries
│   └── test_app.py             # Tests for Streamlit app functionality
├── docs/
│   ├── README.md               # Project overview and setup instructions
│   ├── DESIGN.md               # Database and system design details
│   └── CHANGELOG.md            # Version history
├── .gitignore                  # Git ignore file for Python and virtual env
└── LICENSE                     # License file (e.g., MIT)
