# CyberLedger

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Flask-2.0+-green.svg" alt="Flask">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

> Local cloud accounting system. Works over LAN, data stored locally, no third-party servers.

<p align="center">
  <strong>English</strong> | <a href="./README.zh-CN.md">简体中文</a> | <a href="./README.zh-TW.md">繁體中文</a> | <a href="./README.ja.md">日本語</a>
</p>

---

## Overview

CyberLedger is a lightweight accounting system built with Python + Flask. No database setup required, no account registration needed. Your phone and computer just need to be on the same network.

**Core features:**

| Category | Features |
|----------|----------|
| **Accounting** | Income/expense tracking, categories, notes, recurring expenses |
| **Visualization** | Balance trend, income/expense pie chart, category breakdown |
| **Goals** | Monthly budget with alerts, savings target progress |
| **Data** | Excel export, JSON backup/restore, incremental merge |

---

## Screenshots

*UI screenshots coming soon*

---

## Quick Start

### 1. Clone

```bash
git clone https://github.com/huqingyuan-Python/CyberLedger.git
cd CyberLedger
```

### 2. Install

```bash
pip install flask flask-cors colorama
```

### 3. Run

```bash
python main.py
```

Then open http://127.0.0.1:5000 in your browser.

For mobile access over LAN, check the address shown in the terminal (e.g. http://192.168.1.100:5000).

---

## Features

### Accounting Core

- Record income and expenses with customizable categories
- Add notes to any transaction
- Mark recurring expenses (rent, utilities, subscriptions)
- Filter by date range, search by keywords

### Visualization

```
Balance Trend     Income/Expense Pie     Category Bar
     |                    |                    |
  [chart]              [chart]             [chart]
```

- Balance trend line chart (daily/weekly/monthly view)
- Income vs expense pie chart
- Spending breakdown by category

### Goal Management

- Set monthly spending budget
- Get alerts when approaching or exceeding budget
- Track progress towards savings goals

### Data Portability

- Export to Excel (.xlsx) for offline analysis
- Export/import JSON backups
- Incremental import (won't overwrite existing data)

---

## File Structure

```
CyberLedger/
├── main.py           # Flask backend server
├── index.html        # Frontend (HTML/CSS/JS)
├── background.png    # Background image
├── data.json         # Account data (auto-created)
├── requirements.txt  # Python dependencies
└── README.*.md       # Documentation
```

**Note:** `data.json` is auto-generated on first run and not uploaded to GitHub.

---

## Command Line Options

```bash
# Default port (5000)
python main.py

# Custom port
python main.py -p 8080

# Debug mode (auto-reload)
python main.py --debug

# Combine
python main.py -p 3000 --debug
```

---

## Requirements

- Python 3.8+
- Flask
- flask-cors
- colorama

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3 + Flask |
| Frontend | HTML5 + CSS3 + Vanilla JS |
| Charts | Chart.js |
| Excel Export | SheetJS |

---

## FAQ

**Q: Mobile can't connect?**
A: Make sure phone and computer are on the same WiFi. Check firewall settings.

**Q: Changes don't take effect?**
A: Run with `--debug` flag: `python main.py --debug`

**Q: Want multi-user support?**
A: This is a single-user system. For multi-user, consider using a proper database backend.

---

## Contributing

Issues and pull requests are welcome!

---

## License

MIT License - feel free to use and modify.
