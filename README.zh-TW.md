# CyberLedger

[English](./README.en.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [日本語](./README.ja.md)

---

本地雲記帳系統。手機和電腦在同一區域網路下就能用，資料全存在本地，不走任何第三方伺服器。

---

## 適用場景

- 不想把財務資料交給支付寶/微信，但又想隨時隨地查看
- 偶爾需要在手機上記一筆，電腦上看統計
- 小團隊內部簡單記帳，不想要複雜的財務軟體

---

## 功能列表

### 記帳核心

- 記收入、支出，設定分類（餐飲、交通、購物、娛樂等）
- 每筆記錄可以加備註、標記是否是定期支出（房租、水電之類）
- 按日期範圍篩選，搜尋備註/分類關鍵詞

### 可視化

- 餘額趨勢折線圖：一個月看下來錢是多了還是少了
- 收支佔比餅圖：直觀看到錢都花去哪了
- 分類柱狀圖：各分類的支出對比

### 目標管理

- 設定月度支出預算，超出會有提示
- 設定攢錢目標，看當前進度到百分之多少了

### 資料處理

- 匯出 Excel，方便在電腦上報表或做進一步分析
- 匯出 JSON 備份，防止資料遺失
- 匯入 JSON 備份，支援增量合併（不會覆寫現有資料）

---

## 安裝步驟

### 1. 確認有 Python

需要 Python 3.8 以上。開啟終端機輸入 python --version 檢查，如果提示找不到去 python.org 下載安裝。

### 2. 克隆專案

```bash
git clone https://github.com/huqingyuan-Python/CyberLedger.git
cd CyberLedger
```

不會用 git 的話，直接在 GitHub 頁面點 Code -> Download ZIP 下載也行，解壓後進入資料夾。

### 3. 安裝依賴

```bash
pip install flask flask-cors colorama
```

如果這台電腦上還有別的 Python 專案怕版本衝突，可以建一個虛擬環境：

```bash
# 建立虛擬環境（只需要做一次）
python -m venv .venv

# 啟動虛擬環境
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# 安裝依賴
pip install flask flask-cors colorama
```

### 4. 執行

```bash
python main.py
```

終端機會印出存取位址：

```
╔══════════════════════════════════════════════════╗
║           CyberLedger v1.0                       ║
╠══════════════════════════════════════════════════╣
║  Local:   http://127.0.0.1:5000                  ║
║  Network: http://192.168.x.x:5000                ║
╚══════════════════════════════════════════════════╝
```

---

## 如何存取

### 在本機開啟

直接在瀏覽器網址列輸入 http://127.0.0.1:5000 或 http://localhost:5000。

### 在手機上開啟（區域網路存取）

1. 確保手機和電腦連的是同一個 WiFi
2. 看終端機輸出的 Network 後面的位址
3. 手機瀏覽器開啟這個位址

> 如果手機打不開，可能是防火牆擋了。Windows 可以去控制台 -> Windows Defender 防火牆 -> 允許應用程式通過防火牆，把 Python 加進去。

### 命令列參數

```bash
# 指定連接埠（預設 5000）
python main.py -p 8080

# 開啟除錯模式（改了程式碼自動重載，適合開發）
python main.py --debug

# 組合使用
python main.py -p 3000 --debug
```

---

## 檔案結構

```
CyberLedger/
├── main.py           # Python 後端，Flask 伺服器
├── index.html        # 前端頁面，所有 HTML/CSS/JS 都在這裡面
├── background.png    # 背景圖
├── data.json         # 帳單資料，程式第一次執行後自動建立
├── requirements.txt  # Python 依賴列表
└── README.*.md       # 多語言文件
```

---

## 授權

MIT，隨便用。
