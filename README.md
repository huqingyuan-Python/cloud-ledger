# CyberLedger

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-2.0%2B-green?style=flat-square&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/Status-Stable-brightgreen?style=flat-square" alt="Status">
</p>

<p align="center">
  <h2 align="center">⚡ CyberLedger</h2>
  <p align="center">Modern Local Cloud Accounting System</p>
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#features">Features</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  <strong>English</strong> | <a href="./README.zh-CN.md">简体中文</a> | <a href="./README.zh-TW.md">繁體中文</a> | <a href="./README.ja.md">日本語</a>
</p>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Tech Stack](#tech-stack)
- [File Structure](#file-structure)
- [FAQ](#faq)
- [Changelog](#changelog)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

CyberLedger is a lightweight, self-hosted accounting system built with Python + Flask. No database setup, no account registration, no cloud dependency. Your phone and computer just need to be on the same network.

### Why CyberLedger?

| Feature | CyberLedger | Traditional Apps |
|---------|-------------|------------------|
| Data Storage | Local JSON | Cloud Server |
| Privacy | 100% Private | Third-party Access |
| Setup | No Installation | Account Required |
| Access | LAN Only | Internet Required |
| Cost | Free | Subscription |

---

## Features

### Core Accounting

| Feature | Description |
|---------|-------------|
| Income/Expense Tracking | Record transactions with amount, category, date, and notes |
| Categories | Customizable spending categories (Food, Transport, Shopping, etc.) |
| Recurring Expenses | Mark recurring items like rent and utilities |
| Search & Filter | Find transactions by keyword, date range, or category |

### Visualization

| Chart Type | Purpose |
|------------|---------|
| Balance Trend | Track savings/spending over time |
| Income/Expense Pie | See where money comes from and goes |
| Category Breakdown | Compare spending across categories |

### Goal Management

| Feature | Description |
|---------|-------------|
| Monthly Budget | Set spending limits with over-limit alerts |
| Savings Goals | Track progress towards financial targets |

### Data Management

| Feature | Description |
|---------|-------------|
| Excel Export | Generate .xlsx reports for offline analysis |
| JSON Backup | Export/import data backups |
| Incremental Import | Merge new data without overwriting existing records |

---

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/huqingyuan-Python/CyberLedger.git
cd CyberLedger

# 2. Create virtual environment (recommended)
python -m venv .venv

# 3. Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# 4. Install dependencies
pip install flask flask-cors colorama
```

### Usage

```bash
# Run the server
python main.py
```

The terminal will display:

```
╔══════════════════════════════════════════════════╗
║           CyberLedger v1.0                       ║
╠══════════════════════════════════════════════════╣
║  Local:   http://127.0.0.1:5000                ║
║  Network: http://192.168.x.x:5000              ║
╚══════════════════════════════════════════════════╝
```

### Access

**On the same computer:**
Open `http://127.0.0.1:5000` or `http://localhost:5000` in your browser.

**On mobile device:**
1. Ensure your phone and computer are on the same WiFi
2. Note the Network address shown in terminal
3. Open that address in your phone's browser

> **Tip:** If mobile can't connect, check your firewall settings or try a different port.

---

## Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `-p, --port` | Set server port (default: 5000) | `python main.py -p 8080` |
| `--debug` | Enable debug mode (auto-reload) | `python main.py --debug` |

```bash
# Common usage examples
python main.py                  # Default (port 5000)
python main.py -p 8080          # Custom port
python main.py --debug          # Debug mode
python main.py -p 3000 --debug  # Custom port + debug
```

---

## Documentation

For detailed documentation, see:

| Language | File |
|----------|------|
| English | README.md (this file) |
| Simplified Chinese | README.zh-CN.md |
| Traditional Chinese | README.zh-TW.md |
| Japanese | README.ja.md |

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| Backend | Python 3 | Server logic |
| Framework | Flask | HTTP API server |
| Frontend | HTML5/CSS3/JS | User interface |
| Charts | Chart.js | Data visualization |
| Excel | SheetJS | Spreadsheet export |
| Storage | JSON | Data persistence |

---

## File Structure

```
CyberLedger/
|
|-- main.py                 # Flask server & API endpoints
|-- index.html              # Frontend application
|-- background.png           # UI background image
|-- data.json                # Account data (auto-created)
|-- requirements.txt         # Python dependencies
|
|-- README.md                # Main documentation (English)
|-- README.zh-CN.md          # Simplified Chinese
|-- README.zh-TW.md          # Traditional Chinese
|-- README.ja.md             # Japanese
|
|-- .gitignore               # Git ignore rules
|-- LICENSE                  # MIT License
```

---

## FAQ

### Q: Mobile shows "Connection Refused"

**A:** This is usually a firewall issue. Try:

1. Make sure your phone and computer are on the **same WiFi**
2. Check Windows Firewall settings
3. Try a different port: `python main.py -p 8080`

### Q: Code changes don't take effect

**A:** Run with debug mode enabled:

```bash
python main.py --debug
```

### Q: Is my data safe?

**A:** Yes. All data is stored locally in `data.json`. It is never uploaded to any server.

### Q: Can multiple users use it simultaneously?

**A:** This is a single-user system. Concurrent writes may cause data conflicts.

---

## Changelog

### v1.0.0 (Current)
- Initial release
- Basic accounting features
- Visualization charts
- Budget and goal tracking
- Excel/JSON export
- Multi-language support

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 huqingyuan-Python

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/huqingyuan-Python">huqingyuan-Python</a>
</p>

<p align="center">
  <a href="https://github.com/huqingyuan-Python/CyberLedger">GitHub</a> •
  <a href="https://github.com/huqingyuan-Python/CyberLedger/issues">Issues</a>
</p>
