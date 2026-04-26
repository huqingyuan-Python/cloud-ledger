"""
CyberLedger - Flask Backend Server
Provides API endpoints for the accounting system.
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
import socket
import argparse
import sys
import logging
from datetime import datetime, timedelta
from functools import wraps

# Initialize Flask app with CORS
app = Flask(__name__)
CORS(app)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ============================================
# Configuration
# ============================================
DATA_FILE = "data.json"
HTML_FILE = "index.html"
BACKGROUND_FILE = "background.png"
VERSION = "2.0.0"
API_VERSION = "v1"

# ============================================
# ANSI Colors (with fallback for Windows)
# ============================================
try:
    import colorama
    colorama.init(autoreset=True)
    class Colors:
        RESET   = "\033[0m"
        BOLD    = "\033[1m"
        CYAN    = "\033[96m"
        GREEN   = "\033[92m"
        YELLOW  = "\033[93m"
        RED     = "\033[91m"
        GRAY    = "\033[90m"
        BG_BLUE = "\033[44m"
except ImportError:
    class Colors:
        RESET = CYAN = GREEN = YELLOW = RED = GRAY = BG_BLUE = BOLD = ""


# ============================================
# Helper Functions
# ============================================
def get_local_ip():
    """Get local LAN IP address"""
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except Exception:
        return "127.0.0.1"


def load_data():
    """Load data from JSON file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_data(data):
    """Save data to JSON file"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def log_request(f):
    """Decorator to log API requests"""
    @wraps(f)
    def decorated(*args, **kwargs):
        method = request.method
        path = request.path
        logger.info(f"{Colors.GRAY}[{method}]{Colors.RESET} {path}")
        result = f(*args, **kwargs)
        return result
    return decorated


def calculate_stats(data):
    """Calculate statistics from data"""
    now = datetime.now()
    current_month = now.strftime("%Y-%m")
    last_month = (now.replace(day=1) - timedelta(days=1)).strftime("%Y-%m")

    stats = {
        "total_income": 0,
        "total_expense": 0,
        "balance": 0,
        "month_income": 0,
        "month_expense": 0,
        "month_balance": 0,
        "last_month_income": 0,
        "last_month_expense": 0,
        "categories": {},
        "daily_stats": [],
        "record_count": len(data)
    }

    # Group by date for daily stats
    daily_data = {}

    for item in data:
        amount = item.get("amount", 0)
        date = item.get("date", "")[:10]  # YYYY-MM-DD
        category = item.get("catName", "其他")
        month = date[:7] if len(date) >= 7 else ""

        # Update totals
        if amount > 0:
            stats["total_income"] += amount
            if month == current_month:
                stats["month_income"] += amount
            elif month == last_month:
                stats["last_month_income"] += amount
        else:
            stats["total_expense"] += abs(amount)
            if month == current_month:
                stats["month_expense"] += abs(amount)
            elif month == last_month:
                stats["last_month_expense"] += abs(amount)

        # Update category stats
        if category not in stats["categories"]:
            stats["categories"][category] = {"income": 0, "expense": 0}
        if amount > 0:
            stats["categories"][category]["income"] += amount
        else:
            stats["categories"][category]["expense"] += abs(amount)

        # Daily aggregation
        if date:
            if date not in daily_data:
                daily_data[date] = {"income": 0, "expense": 0}
            if amount > 0:
                daily_data[date]["income"] += amount
            else:
                daily_data[date]["expense"] += abs(amount)

    stats["balance"] = stats["total_income"] - stats["total_expense"]
    stats["month_balance"] = stats["month_income"] - stats["month_expense"]

    # Convert daily data to list
    stats["daily_stats"] = [
        {"date": date, **values}
        for date, values in sorted(daily_data.items())
    ]

    return stats


# ============================================
# Static Routes
# ============================================
@app.route("/")
@log_request
def index():
    """Serve main HTML page"""
    if not os.path.exists(HTML_FILE):
        logger.error(f"{Colors.RED}Error:{Colors.RESET} {HTML_FILE} not found")
        return f"Error: {HTML_FILE} not found", 500

    with open(HTML_FILE, "r", encoding="utf-8") as f:
        return f.read()


@app.route("/background.png")
@log_request
def background():
    """Serve background image"""
    return send_from_directory(".", BACKGROUND_FILE)


@app.route("/manifest.json")
@log_request
def manifest():
    """Serve PWA manifest"""
    manifest_data = {
        "name": "CyberLedger",
        "short_name": "Ledger",
        "description": "Local cloud accounting system",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#1a1a2e",
        "theme_color": "#007aff",
        "icons": [
            {
                "src": "/background.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ]
    }
    return jsonify(manifest_data)


# ============================================
# API Routes
# ============================================
@app.route(f"/api/{API_VERSION}/data")
@log_request
def get_data():
    """GET /api/v1/data - Get all account data"""
    try:
        data = load_data()
        logger.info(f"{Colors.GREEN}Success:{Colors.RESET} Loaded {len(data)} records")
        return jsonify({
            "status": "success",
            "version": VERSION,
            "api_version": API_VERSION,
            "data": data
        })
    except Exception as e:
        logger.error(f"{Colors.RED}Error:{Colors.RESET} {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route(f"/api/{API_VERSION}/data", methods=["POST"])
@log_request
def save_data_api():
    """POST /api/v1/data - Save all account data"""
    try:
        data = request.json
        if not isinstance(data, list):
            return jsonify({"status": "error", "message": "Data must be an array"}), 400

        save_data(data)
        logger.info(f"{Colors.GREEN}Success:{Colors.RESET} Saved {len(data)} records")
        return jsonify({"status": "success", "count": len(data)})
    except Exception as e:
        logger.error(f"{Colors.RED}Error:{Colors.RESET} {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route(f"/api/{API_VERSION}/stats")
@log_request
def get_stats():
    """GET /api/v1/stats - Get statistics"""
    try:
        data = load_data()
        stats = calculate_stats(data)
        return jsonify({
            "status": "success",
            "stats": stats
        })
    except Exception as e:
        logger.error(f"{Colors.RED}Error:{Colors.RESET} {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route(f"/api/{API_VERSION}/export")
@log_request
def export_data():
    """GET /api/v1/export - Export data as JSON"""
    try:
        data = load_data()
        export = {
            "exported_at": datetime.now().isoformat(),
            "version": VERSION,
            "record_count": len(data),
            "data": data
        }
        return jsonify(export)
    except Exception as e:
        logger.error(f"{Colors.RED}Error:{Colors.RESET} {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route(f"/api/{API_VERSION}/import", methods=["POST"])
@log_request
def import_data():
    """POST /api/v1/import - Import data with merge"""
    try:
        imported = request.json
        if not isinstance(imported, list):
            return jsonify({"status": "error", "message": "Data must be an array"}), 400

        existing = load_data()
        existing_ids = {item.get("id") for item in existing}

        # Filter out duplicates and merge
        new_items = [item for item in imported if item.get("id") not in existing_ids]
        merged = existing + new_items

        # Sort by date descending
        merged.sort(key=lambda x: x.get("date", ""), reverse=True)

        save_data(merged)

        logger.info(f"{Colors.GREEN}Success:{Colors.RESET} Merged {len(new_items)} new records")
        return jsonify({
            "status": "success",
            "imported": len(new_items),
            "total": len(merged)
        })
    except Exception as e:
        logger.error(f"{Colors.RED}Error:{Colors.RESET} {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route(f"/api/{API_VERSION}/health")
@log_request
def health():
    """GET /api/v1/health - Health check"""
    data_file_exists = os.path.exists(DATA_FILE)
    data_count = len(load_data()) if data_file_exists else 0

    return jsonify({
        "status": "healthy",
        "version": VERSION,
        "api_version": API_VERSION,
        "data_file_exists": data_file_exists,
        "record_count": data_count,
        "server_time": datetime.now().isoformat()
    })


# Legacy routes for backward compatibility
@app.route("/get_data")
@log_request
def get_data_legacy():
    """Legacy: GET /get_data"""
    return get_data()


@app.route("/save_data", methods=["POST"])
@log_request
def save_data_legacy():
    """Legacy: POST /save_data"""
    return save_data_api()


@app.route("/health")
@log_request
def health_legacy():
    """Legacy: GET /health"""
    return health()


# ============================================
# Server Startup
# ============================================
def print_banner(port: int):
    """Print startup banner"""
    local_ip = get_local_ip()

    print()
    print(f"{Colors.CYAN}{Colors.BOLD}╔{'═' * 50}╗{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.BOLD}CyberLedger{Colors.RESET} {Colors.GRAY}v{VERSION}{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}╠{'═' * 50}╣{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.GRAY}API:       {Colors.RESET} http://127.0.0.1:{port}/api/{API_VERSION}")
    print(f"{Colors.CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.GRAY}Local:     {Colors.RESET} http://127.0.0.1:{port}")
    print(f"{Colors.CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.GRAY}Network:   {Colors.RESET} http://{local_ip}:{port}")
    print(f"{Colors.CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.GRAY}Data:      {Colors.RESET} {os.path.abspath(DATA_FILE)}")
    print(f"{Colors.CYAN}{Colors.BOLD}╚{'═' * 50}╝{Colors.RESET}")
    print()
    print(f"{Colors.YELLOW}Tip:{Colors.RESET} Press {Colors.BOLD}Ctrl + C{Colors.RESET} to stop the server")
    print(f"{Colors.GRAY}{'-' * 52}{Colors.RESET}")
    print()


def run_server(port: int, debug: bool):
    """Start the Flask server"""
    # Ensure data file exists
    if not os.path.exists(DATA_FILE):
        save_data([])
        logger.info(f"{Colors.GREEN}Created:{Colors.RESET} {DATA_FILE}")

    print_banner(port)
    app.run(host="0.0.0.0", port=port, debug=debug)


# ============================================
# Entry Point
# ============================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CyberLedger - Local Cloud Accounting System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                  # Default (port 5000)
  python main.py -p 8080         # Custom port
  python main.py --debug          # Debug mode
  python main.py -p 3000 --debug # Port + debug
        """
    )
    parser.add_argument(
        "-p", "--port",
        type=int,
        default=5000,
        help="Server port (default: 5000)"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable Flask debug mode (auto-reload)"
    )
    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="Host to bind (default: 0.0.0.0)"
    )
    args = parser.parse_args()

    try:
        run_server(port=args.port, debug=args.debug)
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Exiting:{Colors.RESET} Server stopped")
        sys.exit(0)
