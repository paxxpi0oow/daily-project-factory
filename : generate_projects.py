import os
import random
from datetime import datetime

BASE_DIR = "projects"
DATE_STR = datetime.now().strftime("%Y-%m-%d")
TARGET_DIR = os.path.join(BASE_DIR, DATE_STR)

TEMPLATES = {
    "python": {
        "folder": "01-python-calculator",
        "readme": "# Python CLI Calculator\n\nKalkulator sederhana.\n",
        "files": {
            "main.py": 'def hitung(a, b, op):\n    if op == "+": return a + b\n    elif op == "-": return a - b\n    elif op == "*": return a * b\n    elif op == "/": return a / b if b != 0 else "Error"\n    else: return "Error"\n\nprint("=== Kalkulator ===")\na = float(input("Angka 1: "))\nop = input("Operator (+, -, *, /): ")\nb = float(input("Angka 2: "))\nprint("Hasil:", hitung(a, b, op))\n'
        }
    },
    "javascript": {
        "folder": "02-js-todo-cli",
        "readme": "# JavaScript To-Do CLI\n\nAplikasi to-do list terminal.\n",
        "files": {
            "index.js": 'const rl = require("readline").createInterface({input:process.stdin,output:process.stdout});\nconst todos = [];\nfunction menu() {\n  console.log("\\n1. Lihat\\n2. Tambah\\n3. Keluar");\n  rl.question("Pilih: ", p => {\n    if (p === "1") { console.log(todos.join("\\n") || "Kosong"); menu(); }\n    else if (p === "2") { rl.question("Tugas: ", t => { todos.push(t); menu(); }); }\n    else rl.close();\n  });\n}\nmenu();\n'
        }
    },
    "go": {
        "folder": "03-go-http-server",
        "readme": "# Go Simple HTTP Server\n\nServer HTTP sederhana.\n",
        "files": {
            "main.go": 'package main\n\nimport (\n    "encoding/json"\n    "net/http"\n)\n\nfunc handler(w http.ResponseWriter, r *http.Request) {\n    w.Header().Set("Content-Type", "application/json")\n    json.NewEncoder(w).Encode(map[string]string{"message": "Hello from Go!"})\n}\n\nfunc main() {\n    http.HandleFunc("/", handler)\n    http.ListenAndServe(":8080", nil)\n}\n'
        }
    },
    "rust": {
        "folder": "04-rust-guess-game",
        "readme": "# Rust Guessing Game\n\nGame tebak angka.\n",
        "files": {
            "main.rs": 'use std::io;\nuse rand::Rng;\n\nfn main() {\n    println!("Tebak angka 1-100");\n    let angka = rand::thread_rng().gen_range(1..=100);\n    loop {\n        let mut tebakan = String::new();\n        io::stdin().read_line(&mut tebakan).unwrap();\n        let tebakan: u32 = tebakan.trim().parse().unwrap_or(0);\n        if tebakan < angka { println!("Kecil!"); }\n        else if tebakan > angka { println!("Besar!"); }\n        else { println!("Benar!"); break; }\n    }\n}\n'
        }
    },
    "bash": {
        "folder": "05-bash-system-info",
        "readme": "# Bash System Info\n\nInfo sistem sederhana.\n",
        "files": {
            "script.sh": '#!/bin/bash\necho "=== Info Sistem ==="\necho "Host: $(hostname)"\necho "OS: $(uname -s)"\necho "RAM: $(free -h | awk \'/^Mem:/ {print $2}\')"\n'
        }
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
        print(f"Projek {lang} dibuat")

if __name__ == "__main__":
    buat_projek()
