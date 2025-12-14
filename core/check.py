import os
from colorama import Fore, Style

def check_core():
    onering_arm = "/data/data/com.termux/files/usr/bin/xray.linux.arm64.64bit"
    onering_amd = "/data/data/com.termux/files/usr/bin/xray.linux.amd64.64bit"
    
    if os.path.exists(onering_arm) or os.path.exists(onering_amd):
        print(f"{Fore.GREEN}> ONERING✅{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}> ONERING🟥{Style.RESET_ALL}")
    
    xray_normal = "/data/data/com.termux/files/usr/bin/xray"
    if os.path.exists(xray_normal):
        print(f"{Fore.GREEN}> XRAY✅{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}> XRAY🟥{Style.RESET_ALL}")