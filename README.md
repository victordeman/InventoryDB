# InventoryDB

**InventoryDB** is a PostgreSQL-based inventory management system with a Flask backend and a modern HTML frontend using Tailwind CSS, AOS animations, and Feather icons. It allows users to manage products and categories efficiently through a responsive dashboard.

## Features
- **Database Management**: PostgreSQL with tables for products and categories, optimized with indexes and triggers.
- **Flask Backend**: Handles HTTP requests and serves dynamic HTML templates.
- **HTML Frontend**: Responsive dashboard to view inventory stats, manage products, and categories.
- **Automation**: Bash scripts for database setup (\`scripts/setup.sh\`) and backups (\`scripts/backup.sh\`.
- **Documentation**: Includes Entity-Relationship Diagram (ERD) in \`docs/ERD.md\`.

## Tech Stack
- **Database**: PostgreSQL
- **Backend**: Flask, Python (psycopg2)
- **Frontend**: HTML, Tailwind CSS, AOS, Feather icons
- **Scripting**: Linux Bash
- **Version Control**: Git
  
## Repository Structure

```
InventoryDB/
├── app/
│   ├── static/            # For CSS, JS, and other static assets
│   │   ├── aos.css
│   │   ├── aos.js
│   │   └── feather.min.js
│   ├── templates/         # Jinja2 templates
│   │   ├── base.html      # Base template with navigation and styling
│   │   ├── index.html     # Dashboard (adapted from provided HTML)
│   │   ├── add_product.html
│   │   ├── update_stock.html
│   │   └── categories.html
│   ├── config.py          # Database configuration
│   ├── db.py              # Database operations
│   ├── main.py            # Flask app
│   └── requirements.txt   # Dependencies
├── db/                    # (Optional, can consolidate with sql/)
├── sql/                   # Database schema, seed data, queries
│   ├── schema.sql
│   ├── seed.sql
│   ├── queries.sql
│   └── triggers.sql
├── docs/                  # Documentation
│   ├── CHANGELOG.md
│   ├── DESIGN.md
│   ├── ERD.md
│   └── README.md
├── scripts/               # Automation scripts
│   ├── backup.sh
│   ├── monitor.sh
│   ├── requirements.txt
│   └── setup.sh
├── tests/                 # Unit tests
│   ├── test_app.py
│   ├── test_db.py
│   └── test_queries.py
├── .python-version
├── LICENSE
└── README.md
```

## Getting Started

### Prerequisites
- PostgreSQL (\`sudo apt-get install postgresql\`)
- Python 3.10+ and pip
- Git

### Setup Instructions
1. **Clone the Repository**:
   \`\`\`bash
   git clone https://github.com/victordeman/InventoryDB
   cd InventoryDB
   \`\`\`
2. **Install Python Dependencies**:
   \`\`\`bash
   pip install -r app/requirements.txt
   \`\`\`
3. **Set Up PostgreSQL**:
   - Update \`app/config.py\` with your PostgreSQL credentials.
   - Run:
     \`\`\`bash
     bash scripts/setup.sh
     \`\`\`
4. **Download Static Files**:
   - Download \`aos.css\`, \`aos.js\` from https://unpkg.com/aos@2.3.1/dist/.
   - Download \`feather.min.js\` from https://cdn.jsdelivr.net/npm/feather-icons/dist/.
   - Place them in \`app/static/\`.
5. **Run the Flask App**:
   \`\`\`bash
   python app/main.py
   \`\`\`
   - Open \`http://localhost:5000\` in your browser.

## ERD
See [ERD.md](docs/ERD.md) for the database schema diagram.
