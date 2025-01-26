import requests
import json
import random
import time
import os
from colorama import init, Fore


init(autoreset=True)
referral_codes = [
    "pljMNeb7",
    "AtnJpFLJ",
    "kt8pTm9H"
# add more codes and replace it with your codes
]

print(Fore.LIGHTGREEN_EX + f"{len(referral_codes)} referral codes available.")

wallet_file = "wallet.txt"
if os.path.exists(wallet_file):
    with open(wallet_file, "r") as file:
        wallet_list = [line.strip() for line in file if line.strip()]
    if not wallet_list:
        print(Fore.LIGHTRED_EX + "wallet.txt is empty. Please add wallet addresses (one per line).")
        exit()
    print(Fore.LIGHTGREEN_EX + f"{len(wallet_list)} wallet addresses loaded from {wallet_file}.")
else:
    print(Fore.LIGHTRED_EX + f"{wallet_file} not found. Please create the file and add wallet addresses (one per line).")
    exit()

proxy_file = "proxy.txt"
if os.path.exists(proxy_file):
    with open(proxy_file, "r") as file:
        proxy_list = [line.strip() for line in file if line.strip()]
    if not proxy_list:
        print(Fore.LIGHTRED_EX + "proxy.txt is empty. Please add valid proxy addresses (one per line).")
        exit()
    print(Fore.LIGHTGREEN_EX + f"{len(proxy_list)} proxies loaded from {proxy_file}.")
else:
    print(Fore.LIGHTRED_EX + f"{proxy_file} not found. Please create the file and add proxy addresses (one per line).")
    exit()
response_file = "response.txt"
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
}
def get_next_proxy():
    if proxy_list:
        proxy = random.choice(proxy_list)
        return {
            "http": proxy,
            "https": proxy,
        }
    return None

for wallet_address in wallet_list:
    referral_code = random.choice(referral_codes)
    print(Fore.LIGHTCYAN_EX + f"Using random referral code: {referral_code}")
    url = f"https://referral.layeredge.io/api/referral/register-wallet/{referral_code}"
    payload = json.dumps({"walletAddress": wallet_address})
    proxies = get_next_proxy()
    try:
        response = requests.post(
            url, headers=headers, data=payload, proxies=proxies, timeout=10, verify=False
        )
        with open(response_file, "a") as file:
            file.write(f"Referral: {referral_code} | Wallet: {wallet_address} | "
                       f"Response: {response.status_code} | {response.text}\n")

        print(Fore.LIGHTGREEN_EX + f"[{response.status_code}] "
              + Fore.LIGHTWHITE_EX + f"Wallet: {wallet_address} | Response: {response.text}")

    except requests.exceptions.ProxyError as proxy_error:
        print(Fore.LIGHTRED_EX + f"Proxy error: {str(proxy_error)}")
        if proxies:
            proxy_address = proxies["http"]
            proxy_list.remove(proxy_address)
            print(Fore.LIGHTRED_EX + f"Removed bad proxy: {proxy_address}. {len(proxy_list)} proxies remaining.")
        if not proxy_list:
            print(Fore.LIGHTRED_EX + "No more proxies available. Exiting.")
            break
    except requests.exceptions.ConnectionError as connection_error:
        print(Fore.LIGHTRED_EX + f"Connection error: {str(connection_error)}")
        break
    except requests.exceptions.Timeout:
        print(Fore.LIGHTRED_EX + "Request timed out. Retrying...")
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Error: {str(e)}")
        break

    delay = random.randint(3, 15)
    print(Fore.LIGHTYELLOW_EX + f"Next request in {delay} seconds...")
    time.sleep(delay)
