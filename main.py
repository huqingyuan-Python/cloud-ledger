"""
云端玻璃账本 - Flask 服务器后端
提供账单数据的存储与访问接口，配合前端页面使用。
"""

from flask import Flask, request, jsonify, send_from_directory
import json
import os
import socket
import argparse
import sys
import colorama

# ─────────────────────────────────────────────
# 颜色定义（ANSI 转义序列）
# ─────────────────────────────────────────────
class Colors:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    GRAY    = "\033[90m"
    BG_BLUE = "\033[44m"


# ─────────────────────────────────────────────
# Flask 应用初始化
# ─────────────────────────────────────────────
app = Flask(__name__)

# ─────────────────────────────────────────────
# 配置区
# ─────────────────────────────────────────────
DATA_FILE = "data.json"
HTML_FILE = "index.html"
BACKGROUND_FILE = "background.png"


def get_local_ip() -> str:
    """获取本机局域网 IP 地址"""
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except Exception:
        return "127.0.0.1"


# ─────────────────────────────────────────────
# 数据初始化
# ─────────────────────────────────────────────
def init_data_file():
    """确保 data.json 存在，不存在则创建空列表"""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)


# ─────────────────────────────────────────────
# 路由区：静态资源
# ─────────────────────────────────────────────
@app.route("/")
def index():
    """返回前端 HTML 页面"""
    if not os.path.exists(HTML_FILE):
        print(f"{Colors.RED}[错误]{Colors.RESET} 未找到 {HTML_FILE}，请确保它与 {__file__} 在同一目录下。")
        return f"错误：未找到 {HTML_FILE} 文件。", 500
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        return f.read()


@app.route("/background.png")
def background():
    """返回背景图片"""
    return send_from_directory(".", BACKGROUND_FILE)


# ─────────────────────────────────────────────
# 路由区：数据接口
# ─────────────────────────────────────────────
@app.route("/get_data")
def get_data():
    """GET /get_data - 获取所有账单数据"""
    print(f"{Colors.GRAY}[GET ]{Colors.RESET} /get_data  → 返回全部账单")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"{Colors.GREEN}[成功]{Colors.RESET} 共 {len(data)} 条记录")
    return jsonify(data)


@app.route("/save_data", methods=["POST"])
def save_data():
    """POST /save_data - 保存账单数据（整体替换）"""
    try:
        data = request.json
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"{Colors.GREEN}[POST ]{Colors.RESET} /save_data → 已保存 {len(data)} 条记录")
        return jsonify({"status": "success"})
    except Exception as e:
        print(f"{Colors.RED}[错误]{Colors.RESET} /save_data → {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/health")
def health():
    """健康检查接口"""
    return jsonify({"status": "ok", "data_file": DATA_FILE})


# ─────────────────────────────────────────────
# 启动区
# ─────────────────────────────────────────────
def print_banner(port: int):
    """打印启动横幅"""
    local_ip = get_local_ip()
    bar = "─" * 50

    print()
    print(f"{Colors.CYAN}{Colors.BOLD}╔{'═' * 48}╗{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.BOLD}云端玻璃账本{Colors.RESET} {Colors.GRAY}v1.0{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}╠{'═' * 48}╣{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.GRAY}📍 本机访问：{Colors.RESET} http://127.0.0.1:{port}")
    print(f"{Colors.CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.GRAY}📱 局域网：{Colors.RESET} http://{local_ip}:{port}")
    print(f"{Colors.CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.GRAY}📂 数据文件：{Colors.RESET} {os.path.abspath(DATA_FILE)}")
    print(f"{Colors.CYAN}{Colors.BOLD}╚{'═' * 48}╝{Colors.RESET}")
    print()
    print(f"{Colors.YELLOW}[提示]{Colors.RESET} 按 {Colors.BOLD}Ctrl + C{Colors.RESET} 停止服务器")
    print(f"{Colors.GRAY}{'─' * 50}{Colors.RESET}")
    print()


def run_server(port: int, debug: bool):
    """启动 Flask 服务器"""
    init_data_file()
    print_banner(port)
    app.run(host="0.0.0.0", port=port, debug=debug)


# ─────────────────────────────────────────────
# 入口
# ─────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="云端玻璃账本 - Flask 服务器",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例：
  python main.py                 # 默认端口 5000
  python main.py -p 8080         # 使用端口 8080
  python main.py --debug         # 开启调试模式
  python main.py --port 3000     # 端口 3000 + 调试模式
        """
    )
    parser.add_argument(
        "-p", "--port",
        type=int,
        default=5000,
        help="服务器端口（默认：5000）"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="开启 Flask 调试模式（自动重载）"
    )
    args = parser.parse_args()

    try:
        run_server(port=args.port, debug=args.debug)
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[退出]{Colors.RESET} 服务器已停止")
        sys.exit(0)
