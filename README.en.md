# CyberLedger

[English](./README.en.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [日本語](./README.ja.md)

---

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

Python 3.8 or higher required. Run `python --version` in terminal to check. If not installed, download from python.org.

### 2. Clone the Project

```bash
git clone https://github.com/huqingyuan-Python/CyberLedger.git
cd CyberLedger
```

No git? Download the ZIP from the Code button on GitHub and extract it.

### 3. Install Dependencies

```bash
pip install flask flask-cors colorama
```

To avoid conflicts with other projects, use a virtual environment:

```bash
# Create venv (do this once)
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install flask flask-cors colorama
```

### 4. Run

```bash
python main.py
```

The terminal will show the access address:

```
╔══════════════════════════════════════════════════╗
║           CyberLedger v1.0                       ║
╠══════════════════════════════════════════════════╣
║  Local:   http://127.0.0.1:5000                  ║
║  Network: http://192.168.x.x:5000                ║
╚══════════════════════════════════════════════════╝
```

---

## Access

### Local Access

Open http://127.0.0.1:5000 or http://localhost:5000 in your browser.

### Mobile Access (LAN)

1. Make sure your phone and computer are on the same WiFi
2. Look at the Network address shown in the terminal
3. Open that address in your phone's browser

> If mobile won't connect, check your firewall or try a different port.

### Command Line Options

```bash
# Custom port (default is 5000)
python main.py -p 8080

# Debug mode (auto-reload on code changes)
python main.py --debug

# Combine
python main.py -p 3000 --debug
```

---

## File Structure

```
CyberLedger/
├── main.py           # Python backend, Flask server
├── index.html        # Frontend page (HTML/CSS/JS bundled)
├── background.png    # Background image
├── data.json         # Account data, auto-created on first run
├── requirements.txt  # Python dependencies
└── README.*.md       # Documentation in different languages
```

---

## License

MIT.
