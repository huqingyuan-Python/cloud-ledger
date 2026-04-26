# CyberLedger

[English](./README.en.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [日本語](./README.ja.md)

---

本地云记账系统。手机和电脑在同一局域网下就能用，数据全存在本地，不走任何第三方服务器。

---

## 适用场景

- 不想把财务数据交给支付宝/微信，但又想随时随地查看
- 偶尔需要在手机上记一笔，电脑上看统计
- 小团队内部简单记账，不想要复杂的财务软件

---

## 功能列表

### 记账核心

- 记收入、支出，设置分类（餐饮、交通、购物、娱乐等）
- 每条记录可以加备注、标记是否是定期支出（房租、水电之类）
- 按日期范围筛选，搜索备注/分类关键词

### 可视化

- 余额趋势折线图：看一个月下来钱是多了还是少了
- 收支占比饼图：直观看到钱都花哪儿了
- 分类柱状图：各分类的支出对比

### 目标管理

- 设置月度支出预算，超出会有提示
- 设置攒钱目标，看当前进度到百分之多少了

### 数据处理

- 导出 Excel，方便在电脑上报表或者做进一步分析
- 导出 JSON 备份，防止数据丢失
- 导入 JSON 备份，支持增量合并（不会覆盖现有数据）

---

## 安装步骤

### 1. 确保有 Python

需要 Python 3.8 以上。打开终端输入 python --version 检查，如果提示找不到去 python.org 下载安装。

### 2. 克隆项目

```bash
git clone https://github.com/huqingyuan-Python/CyberLedger.git
cd CyberLedger
```

不会用 git 的话，直接在 GitHub 页面点 Code -> Download ZIP 下载也行，解压后进入文件夹。

### 3. 安装依赖

```bash
pip install flask flask-cors colorama
```

如果这台电脑上还有别的 Python 项目怕版本冲突，可以建一个虚拟环境：

```bash
# 创建虚拟环境（只需要做一次）
python -m venv .venv

# 激活虚拟环境
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# 安装依赖
pip install flask flask-cors colorama
```

### 4. 运行

```bash
python main.py
```

终端会打印出访问地址：

```
╔══════════════════════════════════════════════════╗
║           CyberLedger v1.0                       ║
╠══════════════════════════════════════════════════╣
║  Local:   http://127.0.0.1:5000                  ║
║  Network: http://192.168.x.x:5000                ║
╚══════════════════════════════════════════════════╝
```

---

## 如何访问

### 在本机打开

直接在浏览器地址栏输入 http://127.0.0.1:5000 或者 http://localhost:5000。

### 在手机上打开（局域网访问）

1. 确保手机和电脑连的是同一个 WiFi
2. 看终端输出的 Network 后面的地址，比如 http://192.168.1.100:5000
3. 手机浏览器打开这个地址

> 如果手机打不开，可能是防火墙拦了。Windows 可以去控制面板 -> Windows Defender 防火墙 -> 允许应用通过防火墙，把 Python 加进去。

### 命令行参数

```bash
# 指定端口（默认 5000）
python main.py -p 8080

# 开启调试模式（改了代码自动重载，适合开发）
python main.py --debug

# 组合使用
python main.py -p 3000 --debug
```

---

## 文件结构

```
CyberLedger/
├── main.py           # Python 后端，Flask 服务器
├── index.html        # 前端页面，所有 HTML/CSS/JS 都在这里面
├── background.png    # 背景图
├── data.json         # 账单数据，程序第一次运行后自动创建
├── requirements.txt  # Python 依赖列表
└── README.*.md       # 多语言文档
```

**关于 data.json**：这个文件保存所有账单数据，会在程序首次运行时自动生成。因为是本地数据所以没上传 GitHub，不用担心隐私泄露。

---

## 技术细节

- **后端**：Python 3 + Flask，轻量级 Web 框架
- **前端**：原生 HTML/CSS/JS，没有用任何前端框架
- **图表**：Chart.js，浏览器端绘图库
- **Excel 导出**：SheetJS，用于生成 .xlsx 文件
- **数据存储**：JSON 文件，用 Python 的 json 模块读写

整体逻辑不复杂，Flask 提供几个 API 接口，前端调接口读写 data.json。如果想加功能可以直接改 main.py 和 index.html。

---

## 数据备份建议

定期导出备份是个好习惯。点页面里的备份按钮可以导出 JSON 文件，建议每个月备份一次。如果重装系统或者换电脑，导入备份文件就能恢复数据。

---

## 常见问题

**Q: 手机访问显示拒绝连接**
A: 检查电脑防火墙，或者试试把端口改成没被占用的其他端口。

**Q: 改了代码没反应**
A: 启动时加 --debug 参数：python main.py --debug

**Q: 想多人同时记账**
A: 这个系统是单用户设计的，多人同时写可能导致数据冲突。如果真需要多人用，建议换成真正的数据库后端。

---

## 许可证

MIT，随便用。
