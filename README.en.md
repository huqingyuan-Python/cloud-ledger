# CyberLedger

A local cloud accounting system. Your phone and computer just need to be on the same network to use it. All data is stored locally, no third-party servers involved.

---

## When to Use

- You don't want to hand your financial data over to Alipay/WeChat Pay, but still want to check it from anywhere
- You occasionally need to log an expense on your phone and view statistics on your computer
- Small team internal expense tracking without needing complex accounting software

---

## Features

### Core Accounting

- Record income and expenses with categories (food, transport, shopping, entertainment, etc.)
- Add notes to each record, mark recurring expenses (rent, utilities, etc.)
- Filter by date range, search by notes or category keywords

### Visualization

- Balance trend line chart: see if you're saving or overspending over the month
- Income/expense pie chart: instantly see where your money goes
- Category bar chart: compare spending across different categories

### Goal Management

- Set monthly spending budget with over-limit alerts
- Set savings goals and track your progress as a percentage

### Data Handling

- Export to Excel for reporting or further analysis on your computer
- Export JSON backup to prevent data loss
- Import JSON backup with incremental merge (won't overwrite existing data)

---

## Installation

### 1. Python Requirement

Python 3.8 or higher required. Run python --version in terminal to check. If not installed, download from [python.org](https://www.python.org/).

### 2. Clone the Project

`ash
git clone https://github.com/huqingyuan-Python/CyberLedger.git
cd CyberLedger
`

No git? Download the ZIP from the Code button on GitHub and extract it.

### 3. Install Dependencies

Flask is the only required Python library. For a single-purpose machine:

`ash
pip install flask flask-cors colorama
`

To avoid conflicts with other projects, use a virtual environment:

`ash
# Create venv (do this once)
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install flask flask-cors colorama
`

### 4. Run

`ash
python main.py
`

The terminal will show the access address:

`
鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晽
鈺?          CyberLedger v1.0                       鈺?
鈺犫晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨暎
鈺? Local:   http://127.0.0.1:5000                  鈺?
鈺? Network: http://192.168.x.x:5000                鈺?
鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨暆
`

---

## Access

### Local Access

Open http://127.0.0.1:5000 or http://localhost:5000 in your browser.

### Mobile Access (LAN)

1. Make sure your phone and computer are on the same WiFi
2. Look at the Network address shown in the terminal, like http://192.168.1.100:5000
3. Open that address in your phone's browser

> If mobile won't connect, check your firewall or try a different port.

### Command Line Options

`ash
# Custom port (default is 5000)
python main.py -p 8080

# Debug mode (auto-reload on code changes)
python main.py --debug

# Combine
python main.py -p 3000 --debug
`

---

## File Structure

`
CyberLedger/
鈹溾攢鈹€ main.py           # Python backend, Flask server
鈹溾攢鈹€ index.html        # Frontend page (HTML/CSS/JS bundled)
鈹溾攢鈹€ background.png   # Background image
鈹溾攢鈹€ data.json         # Account data, auto-created on first run
鈹溾攢鈹€ requirements.txt  # Python dependencies
鈹斺攢鈹€ README.*.md       # Documentation in different languages
`

**About data.json**: Stores all account records, auto-created on first run. Not uploaded to GitHub for privacy.

---

## Technical Details

- **Backend**: Python 3 + Flask
- **Frontend**: Vanilla HTML/CSS/JS, no framework
- **Charts**: Chart.js
- **Excel export**: SheetJS for generating .xlsx files
- **Data storage**: JSON files via Python's json module

Simple architecture 鈥?Flask provides API endpoints, frontend reads/writes data.json. Easy to modify.

---

## Backup Recommendation

Export backups regularly. Click the backup button in the UI to export JSON. Recommend monthly backups. Restore by importing the backup file.

---

## FAQ

**Q: Mobile shows connection refused**
A: Check firewall settings, or try a different port.

**Q: Code changes don't take effect**
A: Run with --debug: python main.py --debug

**Q: Want multiple users to log simultaneously**
A: This system is single-user by design. Concurrent writes may cause data conflicts.

---

## License

MIT.