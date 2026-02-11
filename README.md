# 🦊 ComFox Terminal
ComFox is a modern, colorful, animated Python terminal emulator featuring custom commands, system‑info scanning, fox themes, and an optional admin mode.  
It blends functionality with personality, offering a playful yet powerful command‑line experience.

---

## ✨ Features

### 🔸 Custom Command System
ComFox includes its own built‑in commands:
- `help` — list all available commands  
- `clear` / `cls` — clear the screen  
- `exit` — close the terminal  
- `reset` — restart the program  
- `echo <text>` — print text  
- `changefox --1/--2` — switch between fox styles  
- `foxcore` / `foxfetch` — deep system scan with animations  
- `update` — Runs the update process

### 🔸 System Commands
Basic shell‑like functionality:
- `cd <path>` — change directory  
- `ls` / `dir` — list files  
- `mkdir <name>` — create folder  
- `rmdir <name>` — remove folder  
- `del <file>` — delete file  
- `cat <file>` — display file contents  
- `pwd` — show current directory  

### 🔸 FoxCore System Scanner
A full animated system information module:
- CPU model, cores, usage per core  
- RAM, swap, storage, partitions  
- Network interfaces, local/public IP  
- GPU detection (NVIDIA via `nvidia-smi`)  
- Boot time, uptime, running processes  
- OS, platform, Python version  
- Active fox theme  

### 🔸 Visual & Aesthetic Features
- Colorful ANSI‑styled UI  
- Animated fox logos  
- Fun ASCII animations  
- Customizable prompt with username  

---

## 🛠 Requirements
- Python 3.8+  
- Modules:
  - `psutil`
  - `requests`
  - `argparse`
  - Standard library modules (os, sys, subprocess, socket, etc.)

Install missing dependencies:
```bash
pip install psutil requests
