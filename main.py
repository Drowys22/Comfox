from ast import arg
import os
import subprocess
import sys
import time
import threading
import platform
import psutil
import argparse
import socket
import requests
import datetime
import getpass
import random


RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BLACK = "\033[90m"
ORANGE = "\033[38;5;208m"
ORANGE_1 = "\033[38;5;166m"

BG_RED = "\033[41m"
BG_BLUE = "\033[44m"
BG_WHITE = "\033[47m"

ownhostname = socket.gethostname()
ownlocal_ip = socket.gethostbyname(ownhostname)
public_ip = requests.get("https://api.ipify.org").text
admingg = 1

PROMPT = BLUE + f" ┌───> " + RED + "C" + ORANGE + "om" + RED + "F" + ORANGE + "ox" + BLUE + " <────────> " + ORANGE + f"{getpass.getuser()}" + BLUE + " < \n ┇\n └$ " + RED

anim_symbol = "•"
foxcount = 1

# ──── ୨୧ ──── ʕ•ᴥ•ʔ
# 「 ﹂ 【 】┏╰ Ι
# ＄


fox_cute = f"""
{ORANGE}
      /\\_/\\
   (  • ᴥ •  )
   / >  <3   \\
  /           \\
 (   ^     ^   )
  \\   = w =   /
   \\_________/
{RESET}
"""


fox_logo = f"""
{ORANGE}        /\\   /\\
       (  ^_^  )
        )     (
       (       )
        \\__ __/{RESET}
"""
fox = fox_logo
fox_type = "fox_logo"


def cmd_help():
    print("")
    print(MAGENTA + " ● " + ORANGE + "Custom Commands:")
    print(MAGENTA + " ● " + ORANGE_1 + "help      »   list of commands")
    print(MAGENTA + " ● " + ORANGE_1 + "clear     »   clear the screen")
    print(MAGENTA + " ● " + ORANGE_1 + "exit      »   exit the terminal")
    print(MAGENTA + " ● " + ORANGE_1 + "reset     »   reset the terminal")
    print(MAGENTA + " ● " + ORANGE_1 + "echo      »   print text")
    print(MAGENTA + " ● " + ORANGE_1 + "foxcore   »   shows your system's info")
    print(MAGENTA + " ● " + ORANGE_1 + "changefox »   change your fox")
    print("")
    print(MAGENTA + " ● " + ORANGE + "System Commands:")
    print(MAGENTA + " ● " + ORANGE_1 + "cd      »   change directory")
    print(MAGENTA + " ● " + ORANGE_1 + "ls/dir  »   list files")
    print(MAGENTA + " ● " + ORANGE_1 + "mkdir   »   create folder")
    print(MAGENTA + " ● " + ORANGE_1 + "rmdir   »   remove folder")
    print(MAGENTA + " ● " + ORANGE_1 + "del     »   delete file")
    print(MAGENTA + " ● " + ORANGE_1 + "cat     »   display file content")
    print(MAGENTA + " ● " + ORANGE_1 + "pwd     »   show current directory")
    print(MAGENTA + " ● " + ORANGE_1 + "update     »   start update process")
    print("")

def update():
    subprocess.run([sys.executable, "updater.py"])
    print("test")

def cmd_clear():
    os.system("cls" if os.name == "nt" else "clear")

def cmd_exit():
    print("Kilépés...")
    sys.exit()

def cmd_echo(text):
    print(text)

def cmd_cd(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(RED + "Directory not found." + RESET)

def cmd_ls():
    for item in os.listdir():
        print(item)

def cmd_mkdir(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print(RED + "Folder already exists." + RESET)

def cmd_rmdir(name):
    try:
        os.rmdir(name)
    except Exception:
        print(RED + "Cannot remove folder (not empty?)." + RESET)

def cmd_del(name):
    try:
        os.remove(name)
    except Exception:
        print(RED + "Cannot delete file." + RESET)

def cmd_cat(name):
    try:
        with open(name, "r", encoding="utf-8") as f:
            print(f.read())
    except Exception:
        print(RED + "Cannot read file." + RESET)

def cmd_pwd():
    print(os.getcwd())


def anim_ascii():
    frames = [
        " (•_•) ",
        " ( •_•)>⌐■-■ ",
        " (⌐■_■) "
    ]

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        print(frame)
        time.sleep(0.3)

def hel():
    print(RED + f"Unknown Command: 'hel' Did you mean help?" + RESET)

def reset():
    filename = os.path.abspath(__file__)
    subprocess.run(f'start "" "{filename}"', shell=True)
    sys.exit()

def foxcore_scan_anim():
    steps = [
        "Initializing FoxCore modules",
        "Scanning hardware",
        "Collecting OS data",
        "Checking network interfaces",
        "Analyzing storage",
        "Finalizing report"
    ]
    for i, step in enumerate(steps, start=1):
        print(f"{MAGENTA}● {ORANGE}{step}...{RESET}")
        time.sleep(0.15)
    print("")


def foxcore():
    cmd_clear()
    global fox, fox_type

    foxcore_scan_anim()

    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time

    cpu_freq = psutil.cpu_freq()
    cpu_usage_per_core = psutil.cpu_percent(interval=0.5, percpu=True)
    cpu_usage_total = sum(cpu_usage_per_core) / len(cpu_usage_per_core)

    ram = psutil.virtual_memory()
    swap = psutil.swap_memory()
    disk_root = psutil.disk_usage("/")
    net_if_addrs = psutil.net_if_addrs()
    net_if_stats = psutil.net_if_stats()

    try:
        gpu_info = subprocess.check_output(
            "nvidia-smi --query-gpu=name,memory.total,memory.used,utilization.gpu --format=csv,noheader,nounits",
            shell=True
        ).decode().strip()
    except:
        gpu_info = "No GPU / Not detected"

    print(fox)
    print(f"{ORANGE} FoxCore PRO – System Deep Scan")
    print(f"{ORANGE_1}────────────────────────────────────────────────────────{RESET}")

    print(f"{MAGENTA}● {ORANGE}System")
    print(f"{ORANGE}  OS:           {WHITE}{platform.system()} {platform.release()} ({platform.version()})")
    print(f"{ORANGE}  Platform:     {WHITE}{platform.platform()}")
    print(f"{ORANGE}  Machine:      {WHITE}{platform.machine()}")
    print(f"{ORANGE}  Node:         {WHITE}{platform.node()}")
    print(f"{ORANGE}  Hostname:     {WHITE}{ownhostname}")
    print(f"{ORANGE}  User:         {WHITE}{getpass.getuser()}")
    print(f"{ORANGE}  Python:       {WHITE}{platform.python_version()} ({sys.executable})")

    print("")

    print(f"{MAGENTA}● {ORANGE}CPU")
    print(f"{ORANGE}  Model:        {WHITE}{platform.processor()}")
    print(f"{ORANGE}  Cores:        {WHITE}{psutil.cpu_count(logical=False)} physical / {psutil.cpu_count(logical=True)} logical")
    if cpu_freq:
        print(f"{ORANGE}  Frequency:    {WHITE}{cpu_freq.current:.0f} MHz (min {cpu_freq.min:.0f}, max {cpu_freq.max:.0f})")
    print(f"{ORANGE}  Usage total:  {WHITE}{cpu_usage_total:.1f}%")
    print(f"{ORANGE}  Usage per core:")
    for idx, core in enumerate(cpu_usage_per_core):
        print(f"{ORANGE}    Core {idx}:    {WHITE}{core:.1f}%")

    print("")

    print(f"{MAGENTA}● {ORANGE}Memory")
    print(f"{ORANGE}  RAM total:    {WHITE}{ram.total / (1024**3):.2f} GB")
    print(f"{ORANGE}  RAM used:     {WHITE}{ram.used / (1024**3):.2f} GB ({ram.percent}%)")
    print(f"{ORANGE}  RAM free:     {WHITE}{ram.available / (1024**3):.2f} GB")
    print(f"{ORANGE}  Swap total:   {WHITE}{swap.total / (1024**3):.2f} GB")
    print(f"{ORANGE}  Swap used:    {WHITE}{swap.used / (1024**3):.2f} GB ({swap.percent}%)")

    print("")

    print(f"{MAGENTA}● {ORANGE}Storage")
    print(f"{ORANGE}  Root total:   {WHITE}{disk_root.total / (1024**3):.2f} GB")
    print(f"{ORANGE}  Root used:    {WHITE}{disk_root.used / (1024**3):.2f} GB ({disk_root.percent}%)")
    print(f"{ORANGE}  Root free:    {WHITE}{disk_root.free / (1024**3):.2f} GB")

    try:
        partitions = psutil.disk_partitions()
        print(f"{ORANGE}  Partitions:")
        for p in partitions:
            try:
                usage = psutil.disk_usage(p.mountpoint)
                print(f"{ORANGE}    {p.device} {WHITE}-> {p.mountpoint} | {usage.total / (1024**3):.1f} GB, {usage.percent}% used")
            except PermissionError:
                print(f"{ORANGE}    {p.device} {WHITE}-> {p.mountpoint} | access denied")
    except Exception:
        pass

    print("")

    print(f"{MAGENTA}● {ORANGE}Network")
    print(f"{ORANGE}  Local IP:     {WHITE}{ownlocal_ip}")
    print(f"{ORANGE}  Public IP:    {WHITE}{public_ip}")
    print(f"{ORANGE}  Interfaces:")
    for name, addrs in net_if_addrs.items():
        stats = net_if_stats.get(name)
        state = "UP" if stats and stats.isup else "DOWN"
        print(f"{ORANGE}    {name} [{state}]{WHITE}")
        for addr in addrs:
            if addr.family == socket.AF_INET:
                print(f"{ORANGE}      IPv4: {WHITE}{addr.address}")
            elif addr.family == socket.AF_INET6:
                print(f"{ORANGE}      IPv6: {WHITE}{addr.address}")
            elif hasattr(socket, "AF_LINK") and addr.family == socket.AF_LINK:
                print(f"{ORANGE}      MAC:  {WHITE}{addr.address}")

    print("")

    print(f"{MAGENTA}● {ORANGE}GPU")
    print(f"{ORANGE}  Info:         {WHITE}{gpu_info}")

    print("")

    print(f"{MAGENTA}● {ORANGE}Time")
    print(f"{ORANGE}  Boot time:    {WHITE}{boot_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{ORANGE}  Uptime:       {WHITE}{str(uptime).split('.')[0]}")

    print("")

    print(f"{MAGENTA}● {ORANGE}Processes")
    print(f"{ORANGE}  Total:        {WHITE}{len(psutil.pids())}")

    try:
        proc_list = []
        for p in psutil.process_iter(["pid", "name", "cpu_percent"]):
            proc_list.append(p.info)
        top = sorted(proc_list, key=lambda x: x["cpu_percent"], reverse=True)[:5]
        print(f"{ORANGE}  Top CPU:")
        for p in top:
            print(f"{ORANGE}    PID {p['pid']}: {WHITE}{p['name']} ({p['cpu_percent']}%)")
    except Exception:
        pass

    print("")

    print(f"{MAGENTA}● {ORANGE}Misc")
    print(f"{ORANGE}  Working dir:  {WHITE}{os.getcwd()}")
    print(f"{ORANGE}  Theme:        {WHITE}Fox-Orange-{fox_type}")

    print(f"{ORANGE_1}────────────────────────────────────────────────────────{RESET}\n")

def adminpanel(args=""):
    global admingg
    if args == "":
        print("● Missing admin code.")
        return
    if "--" not in args:
        print("● Invalid format.")
        return
    raw = args.replace("--", "")

    if "x" not in raw:
        print("● Invalid format.")
        return

    version, sub = raw.split("x")
    version = int(version)
    sub = int(sub)
    if admingg == 2:
        print("● You already in admin mode.")
    if admingg == 1:
        if version == 1 and sub == 64:
            print("Admin Menu | Beta")
            admingg = 2
        else:
            print("Admin login denied.")
            admingg = 1

def changefox(args=""):
    global foxcount, fox, fox_logo, fox_cute, fox_type

    if args == "":
        print("● Missing argument. Use: changefox --1 or --2")
        return

    if not args.startswith("--"):
        print("● Invalid format. Use: changefox --1 or --2")
        return

    try:
        new_mode = int(args.replace("--", ""))
    except ValueError:
        print("● Invalid number. Use: --1 or --2")
        return

    if new_mode not in [1, 2]:
        print(MAGENTA + "● " + ORANGE_1 + "There are only 2 fox styles available.")
        return

    if new_mode == foxcount:
        print(MAGENTA + "● " + ORANGE_1 + "This fox style is already active.")
        return

    foxcount = new_mode

    if foxcount == 1:
        fox = fox_logo
        fox_type = "fox_logo"
        print(MAGENTA + "● " + ORANGE_1 + "Selected: default fox!")
    elif foxcount == 2:
        fox = fox_cute
        fox_type = "fox_cute"
        print(MAGENTA + "● " + ORANGE_1 + "Selected: cute fox!")


def print_system_info():
    cmd_clear()
    print(" ")
    print(" ")
    print(RED + "[" + RESET + "system" + RED + "]" + RESET + "Hostname: " + RED + ownhostname + BLACK + "   [] " + WHITE + "OS:  " + RED + platform.platform())
    print(RED + "[" + RESET + "system" + RED + "]" + RESET + "Local IP: " + RED + ownlocal_ip + BLACK + "    [] " + WHITE + "CPU: " + RED + platform.processor())
    print(RED + "[" + RESET + "system" + RED + "]" + RESET + "Public IP: " + RED + public_ip + BLACK + "   [] " + WHITE + "User: " + RED + getpass.getuser())
    print(" ")

def admincmd(args=""):
    global admingg
    if args == "":
        print("● Missing admin code.")
        return
    if "--" not in args:
        print("● Invalid format.")
        return
    raw = args.replace("--", "")

    if "x" not in raw:
        print("● Invalid format.")
        return

    version, sub = raw.split("x")
    version = int(version)
    sub = int(sub)
    if admingg == 1:
        print("● You dont have the required permissons.")
        return
    elif admingg == 2:
        if version == 2 and sub == 15:
            cmd_clear()
            print_system_info()
        else:
            print(MAGENTA + "● " + ORANGE_1 + "Invaild command.")


commands = {
    "help": cmd_help,
    "clear": cmd_clear,
    "cls": cmd_clear,
    "exit": cmd_exit,
    "echo": cmd_echo,

    "cd": cmd_cd,
    "ls": cmd_ls,
    "dir": cmd_ls,
    "mkdir": cmd_mkdir,
    "rmdir": cmd_rmdir,
    "del": cmd_del,
    "cat": cmd_cat,
    "pwd": cmd_pwd,
    "anim": anim_ascii,
    "hel": hel,
    "hlep": hel,
    "hlp": hel,
    "hep": hel,
    "hepl": hel,
    "reset": reset,
    "foxfetch": foxcore,
    "foxcore": foxcore,
    "admin": adminpanel,
    "adminpanel": adminpanel,
    "changefox": changefox,
    "admincmd": admincmd,
    "update": update

    


}


def main():
    if os.name == "nt":
        os.system("chcp 65001 > nul")
    cmd_clear()
    print(RED + " ● ComFox started!\n" + RESET)

    while True:
        user_input = input(PROMPT).strip()

        if user_input == "":
            continue

        parts = user_input.split(" ", 1)
        cmd = parts[0]

        if len(parts) > 1:
            args = parts[1]
        else:
            args = ""

        if cmd in commands:
            func = commands[cmd]

            if cmd in ["cd", "mkdir", "rmdir", "del", "cat", "echo", "adminpanel", "changefox", "admincmd"]:
                if args == "":
                    print(RED + "Missing argument." + RESET)
                else:
                    func(args)
            else:
                func()
            continue

        try:
            result = subprocess.run(user_input, shell=True)
            if result.returncode == 0:
                continue
        except:
            pass

        try:
            ps_command = f"powershell -Command \"{user_input}\""
            result = subprocess.run(ps_command, shell=True)
            if result.returncode == 0:
                continue
        except:
            pass

        print(RED + f"Unknown Command: {cmd}. Type: 'help'" + RESET)


if __name__ == "__main__":
    main()
