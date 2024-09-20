import requests
import json
import time
import random
import base64
import os
import glob
import string
import asyncio
import aiohttp
from datetime import datetime
from itertools import cycle
from colorama import init, Fore, Style
from fake_useragent import UserAgent
from requests_html import HTMLSession

# Proxy setup
PROXY = 'http://yqw84fw7yvwqhty-country-id:x19mey9a78ah61n@rp.proxyscrape.com:6060'

# Initialize file paths for existing and new voucher files
file_akun = 'initdata.txt'
file_vc_tile = 'voucher_tile.txt'
file_vc_zoo = 'voucher_zoo.txt'
file_vc_twerk = 'voucher_twerk.txt'
file_vc_poly = 'voucher_poly.txt'
file_vc_fluf = 'voucher_fluff.txt'
file_vc_cube = 'voucher_chain.txt'
file_vc_trim = 'voucher_mow.txt'
file_vc_train = 'voucher_train.txt'
file_vc_stone = 'voucher_stone.txt'
file_vc_merge = 'voucher_merge.txt'
file_vc_bounc = 'voucher_bounce.txt'
file_vc_hide = 'voucher_hide.txt'
file_vc_count = 'voucher_count.txt'
file_vc_pin = 'voucher_pin.txt'
file_vc_infect = 'voucher_infect.txt'
file_vc_among = 'voucher_among.txt'


# Create a session with proxy support
session = HTMLSession()
session.proxies = {
    'http': PROXY,
    'https': PROXY,
}
ua = UserAgent()

# Initialize colorama
init(autoreset=True)

def load_tokens(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return []

def get_headers(token: str) -> dict:
    return {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': f'Bearer {token}',
        'Connection': 'keep-alive',
        'Origin': 'https://hamsterkombatgame.io',
        'Referer': 'https://hamsterkombatgame.io/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': ua.random
    }

def get_token(init_data_raw):
    url = 'https://api.hamsterkombatgame.io/auth/auth-by-telegram-webapp'
    headers = {
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Origin': 'https://hamsterkombatgame.io',
        'Referer': 'https://hamsterkombatgame.io/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': ua.random,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    data = json.dumps({"initDataRaw": init_data_raw})
    res = session.post(url, headers=headers, data=data)
    if res.status_code == 200:
        return res.json()['authToken']
    else:
        error_data = res.json()
        if "invalid" in error_data.get("error_code", "").lower():
            print(Fore.LIGHTRED_EX + "\rFailed Get Token. Invalid init data", flush=True)
        else:
            print(Fore.LIGHTRED_EX + f"\rFailed Get Token. {error_data}", flush=True)
        return None

def authenticate(token):
    url = 'https://api.hamsterkombatgame.io/auth/me-telegram'
    headers = get_headers(token)
    response = session.post(url, headers=headers)
    return response

def klaim_voucher(token, pocer):
    url = 'https://api.hamsterkombatgame.io/clicker/apply-promo'
    headers = get_headers(token)
    headers['accept'] = 'application/json'
    headers['content-type'] = 'application/json'
    data = json.dumps({"promoCode": pocer})
    response = session.post(url, headers=headers, data=data)
    return response

def main():
    print_welcome_message()
    print(Fore.LIGHTGREEN_EX + "Bot dijalankan....")
    init_data = load_tokens(file_akun)
    token_cycle = cycle(init_data)
    token_dict = {}  # Dictionary to store successful tokens
    voucher_files = {
        "Tile": file_vc_tile,
        "Zoo": file_vc_zoo,
        "Twerk": file_vc_twerk,
        "Poly": file_vc_poly,
        "Fluf": file_vc_fluf,
        "Cube": file_vc_cube,
        "Trim": file_vc_trim,
        "Train": file_vc_train,
        "Stone": file_vc_stone,
        "Merge": file_vc_merge,
        "Bounc": file_vc_bounc,
        "Hide": file_vc_hide,
        "Count": file_vc_count,
        "Pin": file_vc_pin,
        "Infect": file_vc_infect,
        "Among": file_vc_among
    }

    while True:
        init_data_raw = next(token_cycle)
        token = token_dict.get(init_data_raw)
        if token:
            print(Fore.LIGHTRED_EX + f"\n\n\n\rAkun: Diulang", flush=True)
        else:
            token = get_token(init_data_raw)
            if token:
                token_dict[init_data_raw] = token
                print(Fore.LIGHTGREEN_EX + f"\n\n\rAkun: Aktif", flush=True)
            else:
                print(Fore.LIGHTRED_EX + f"\rBeralih ke akun selanjutnya\n", flush=True)
                continue

        response = authenticate(token)
        if response.status_code == 200:
            user_data = response.json()
            username = user_data.get('telegramUser', {}).get('username', 'Username Kosong')
            firstname = user_data.get('telegramUser', {}).get('firstName', 'Kosong')
            lastname = user_data.get('telegramUser', {}).get('lastName', 'Kosong')
            print(Fore.LIGHTYELLOW_EX + f"~~~~~~~~[{Fore.LIGHTWHITE_EX} {username} | {firstname} {lastname} {Fore.LIGHTYELLOW_EX}]~~~~~~~~\n")

            # Loop through each voucher type and claim vouchers
            for voucher_name, voucher_file in voucher_files.items():
                vsukses = 0
                for x in range(4):
                    count = x + 1
                    with open(voucher_file, "r") as myfile:
                        pocer = myfile.readline().strip('\n')
                    print(Fore.BLUE + f"\r[ {voucher_name} ] : VC-{count}: {pocer}             ", flush=True)
                    response = klaim_voucher(token, pocer)
                    if response.status_code == 200:
                        print(Fore.LIGHTGREEN_EX + f"\r[ {voucher_name} ] : VC-{count} berhasil diklaim", flush=True)
                        with open(voucher_file, "r") as myfile:
                            rows = myfile.readlines()[1:]
                        with open(voucher_file, "w") as myfile:
                            for item in rows:
                                myfile.write(item)
                                vsukses += 1
                        time.sleep(1)
                    elif response.status_code == 400:
                        print(Fore.LIGHTRED_EX + f"\r[ {voucher_name} ] : VC-{count} gagal diklaim", flush=True)
                    else:
                        print(Fore.LIGHTRED_EX + f"\r[ {voucher_name} ] : Gagal ambil status server...", flush=True)
                    count += 1
                print(Fore.LIGHTCYAN_EX + f"\r[ {voucher_name} ] : Berhasil Klaim {vsukses} voucher", flush=True)
            print(Fore.LIGHTYELLOW_EX + "\r=================================================")

        elif response.status_code == 401:
            error_data = response.json()
            if error_data.get("error_code") == "NotFound_Session":
                print(Fore.LIGHTRED_EX + f"=== [ Token Invalid {token} ] ===")
                token_dict.pop(init_data_raw, None)
                token = None
            else:
                print(Fore.LIGHTRED_EX + "Authentication failed with unknown error")
        else:
            print(Fore.LIGHTRED_EX + f"Error with status code: {response.status_code}")
            token = None
        time.sleep(1)

def print_welcome_message():
    print(Fore.LIGHTYELLOW_EX + "\n\rRecode By Una Davina ( https://t.me/unadavina )")
    print(Fore.LIGHTGREEN_EX + "\n=============================================")

if __name__ == "__main__":
    main()
