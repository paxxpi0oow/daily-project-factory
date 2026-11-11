import os
import random
from datetime import datetime

BASE_DIR = "projects"
DATE_STR = datetime.now().strftime("%Y-%m-%d")
TARGET_DIR = os.path.join(BASE_DIR, DATE_STR)

TEMPLATES = {
    "python": {
        "folder": "01-python-calculator",
        "readme": "# Python CLI Calculator\n",
        "files": {"main.py": "print('Hello World')\n"}
    },
    "javascript": {
        "folder": "02-js-todo-cli",
        "readme": "# JavaScript To-Do CLI\n",
        "files": {"index.js": "console.log('Hello World');\n"}
    },
    "go": {
        "folder": "03-go-http-server",
        "readme": "# Go Simple HTTP Server\n",
        "files": {"main.go": "package main\nimport \"fmt\"\nfunc main() { fmt.Println(\"Hello\") }\n"}
    },
    "rust": {
        "folder": "04-rust-guess-game",
        "readme": "# Rust Guessing Game\n",
        "files": {"main.rs": "fn main() { println!(\"Hello\"); }\n"}
    },
    "bash": {
        "folder": "05-bash-system-info",
        "readme": "# Bash System Info\n",
        "files": {"script.sh": "#!/bin/bash\necho 'Hello'\n"}
    }
}

def buat_projek():
    os.makedirs(TARGET_DIR, exist_ok=True)
    pilihan = random.sample(list(TEMPLATES.keys()), k=5)
    for lang in pilihan:
        data = TEMPLATES[lang]
        folder_path = os.path.join(TARGET_DIR, data["folder"])
        os.makedirs(folder_path, exist_ok=True)
        with open(os.path.join(folder_path, "README.md"), "w") as f:
            f.write(data["readme"])
        for nama_file, isi in data["files"].items():
            with open(os.path.join(folder_path, nama_file), "w") as f:
                f.write(isi)

if __name__ == "__main__":
    buat_projek()
