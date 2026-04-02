import streamlit.web.cli as stcli
import os, sys

def resolve_path(path):
    resolved_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.join(resolved_path, path)

if __name__ == "__main__":
    # coursera_pro.py faylini ishga tushirish buyrug'i
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("coursera_pro.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())