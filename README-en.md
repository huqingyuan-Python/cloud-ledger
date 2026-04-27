# 📒 Cloud Glass Ledger

**Language / 语言 / 言語:** [简体中文](./README.md) · [English](./README-en.md) · [日本語](./README-ja.md)

---

A local cloud bookkeeping web app built with Flask + HTML/CSS/JS. Data is stored in a local JSON file, accessible from any device on the same local network — track your finances anywhere.

> Perfect for individuals or small teams. Data stays private, never uploaded to third-party servers.

---

## ✨ Features

- 📱 **Mobile-first** — Open directly in your phone's browser with a beautiful glass-morphism UI
- 📊 **Visual Charts** — Balance trend line chart, income/expense pie chart, category bar chart
- 🎯 **Savings Goal** — Set a goal and track your progress in real time
- 💸 **Monthly Budget** — Set a spending cap with automatic over-budget alerts
- 📅 **Month Comparison** — Compare income and expenses with last month
- 🔄 **Recurring Expense Tags** — Mark rent, utilities, and other recurring costs
- 🔍 **Search & Filter** — Quickly filter records by note or category keywords
- 💾 **Local Storage** — All data saved locally in JSON, fully private
- 📤 **Backup** — One-click export to Excel and JSON backup files
- 📥 **Restore** — Import JSON backups with merge (incremental, no overwrite)

---

## 📦 Installation

### Requirements

- Python 3.8+
- Flask

### Setup

```bash
# 1. Clone or download this project
git clone https://github.com/huqingyuan-Python/CyberLedger.git
cd CyberLedger

# 2. Install dependencies
pip install flask

# 3. Run the server
python main.py
```

---

## 🚀 Usage

The terminal will display access addresses after startup:

```
╔══════════════════════════════════════════════════╗
║  Cloud Glass Ledger v1.0                      ║
╠══════════════════════════════════════════════════╣
║  📍 Local:       http://127.0.0.1:5000        ║
║  📱 LAN:         http://192.168.x.x:5000      ║
╚══════════════════════════════════════════════════╝
```

- **Local**: Open directly in your computer's browser
- **LAN**: Make sure your phone is on the same WiFi, then open the LAN address in your browser

### CLI Arguments

```bash
python main.py -p 8080        # Set port to 8080
python main.py --debug        # Enable debug mode (auto-reload on code changes)
python main.py -p 3000 --debug
```

---

## 📂 Project Structure

```
CyberLedger/
├── main.py           # Flask server backend
├── index.html        # Frontend (HTML/CSS/JS in one file)
├── background.png    # Background image
├── data.json         # Ledger data (auto-generated, not uploaded to GitHub)
├── .gitignore        # Git ignore (data.json excluded)
├── README.md         # This file (Simplified Chinese)
├── README-en.md      # English version
├── README-ja.md      # Japanese version
└── LICENSE           # MIT License
```

---

## ⚙️ Data Notes

- **data.json** is auto-created and managed by the program — **never uploaded to GitHub**
- All data is stored locally and remains completely private
- It is recommended to regularly use the 💾 backup feature in the app to export JSON

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3 + Flask |
| Frontend | HTML5 + CSS3 + Vanilla JS |
| Charts | Chart.js |
| Excel Export | SheetJS (xlsx) |

---

## 📄 License

MIT License — Use freely, modify freely.
