import requests
from urllib.parse import parse_qs
from colorama import init, Fore
import sys
import time

# Initialize colorama
init(autoreset=True)

def nama():
    art_lines = [
        "   _____         _   _  _____ _______ _    _         _______     __",
        "  / ____|  /\\   | \\ | |/ ____|__   __| |  | |  /\\   |  __ \\ \\   / /",
        " | (___   /  \\  |  \\| | |       | |  | |  | | /  \\  | |__) \\ \\_/ / ",
        "  \\___ \\ / /\\ \\ | . ` | |       | |  | |  | |/ /\\ \\ |  _  / \\   /  ",
        "  ____) / ____ \\| |\\  | |____   | |  | |__| / ____ \\| | \\ \\  | |   ",
        " |_____/_/    \\_\\_| \\_|\\_____|  |_|   \\____/_/    \\_\\_|  \\_\\ |_|   ",
        "                                                                   ",
        "                                                                   "
    ]

    max_length = max(len(line) for line in art_lines)

    border = '#' * (max_length + 4)

    print(border)
    for line in art_lines:
        print(f"# {line} #")
    print(border)

    print(f"{Fore.GREEN}Terima kasih Telah Menggunakan Bot dari Monteksz X Sanctuary Jangan Lupa Bintangnya ^^{Fore.RESET}")
    print(f"{Fore.GREEN}Cek Bot Lainnya di https://github.com/monteksz{Fore.RESET}")
    print(f"{Fore.GREEN}=================================================================================================={Fore.RESET}")

nama()

# Function to read data from akun.txt
def read_akun_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        akun_data_list = [parse_qs(line.strip()) for line in lines if line.strip()]
        return akun_data_list

# Function to clear the current line in the console
def clear_line():
    sys.stdout.write('\r')
    sys.stdout.flush()

# Function to clear the last n lines in the console
def clear_lines(n):
    for _ in range(n):
        sys.stdout.write('\033[F')  # Cursor up one line
        sys.stdout.write('\033[K')  # Clear to the end of line

# Function to animate waiting message
def animate_waiting_message(duration):
    animation = "|/-\\"
    idx = 0
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f'\rMenunggu {int((end_time - time.time()) // 60)} menit {int((end_time - time.time()) % 60)} detik {animation[idx % len(animation)]}')
        sys.stdout.flush()
        idx += 1
        time.sleep(0.2)
    clear_line()

# Path to the akun.txt file
akun_file_path = 'akun.txt'

# Read data from akun.txt
akun_data_list = read_akun_file(akun_file_path)

def process_akun(akun_data):
    # Step 1: Send OPTIONS request
    url = "https://api.prod.piggypiggy.io/tgBot/login"
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "query_id": akun_data["query_id"][0],
        "user": akun_data["user"][0],
        "auth_date": akun_data["auth_date"][0],
        "hash": akun_data["hash"][0]
    }

    response_options = requests.options(url, headers=headers, params=params)

    # Check if OPTIONS request is successful
    if response_options.status_code == 204:
        print(Fore.BLUE + "OPTIONS Berhasil Diterapkan")
        
        # Step 2: Send GET request
        response_get = requests.get(url, params=params)

        # Check if GET request is successful
        if response_get.status_code == 200:
            print(Fore.GREEN + "Token Berhasil Didapatkan!")
            data = response_get.json()
            token = data.get('data', {}).get('token', 'No Token Found')

            # Step 3: Send POST request to /game/GetPlayerBase
            game_url = "https://api.prod.piggypiggy.io/game/GetPlayerBase"
            game_headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9",
                "Authorization": f"bearer {token}",
                "Cache-Control": "no-cache",
                "Content-Length": "0",
                "Content-Type": "application/json",
                "Origin": "https://restaurant-v2.piggypiggy.io",
                "Pragma": "no-cache",
                "Referer": "https://restaurant-v2.piggypiggy.io/",
                "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/126.0.0.0 Safari/537.36"
            }

            response_game = requests.post(game_url, headers=game_headers)

            # Print response from /game/GetPlayerBase
            if response_game.status_code == 200:
                print(Fore.GREEN + "Game data berhasil didapatkan!")
                game_data = response_game.json().get('data', {})
                balance = game_data.get('currency', 'No Balance')
                salary = game_data.get('currrencyPool', 'No Salary')
                print(Fore.WHITE + f"Balance: {balance} | Salary: {salary}")
                player_id = game_data.get('playerID', 0)

                while True:
                    task_success = False
                    last_task_id = None
                    for task_id in range(1000, 1010):
                        task_url = "https://api.prod.piggypiggy.io/game/TakeTask"
                        task_headers = {
                            "Accept": "*/*",
                            "Accept-Encoding": "gzip, deflate, br, zstd",
                            "Accept-Language": "en-US,en;q=0.9",
                            "Authorization": f"bearer {token}",
                            "Cache-Control": "no-cache",
                            "Content-Length": "28",
                            "Content-Type": "application/json",
                            "Origin": "https://restaurant-v2.piggypiggy.io",
                            "Pragma": "no-cache",
                            "Referer": "https://restaurant-v2.piggypiggy.io/",
                            "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            "Sec-Ch-Ua-Mobile": "?0",
                            "Sec-Ch-Ua-Platform": '"Windows"',
                            "Sec-Fetch-Dest": "empty",
                            "Sec-Fetch-Mode": "cors",
                            "Sec-Fetch-Site": "same-site",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/126.0.0.0 Safari/537.36"
                        }

                        task_payload = {"TaskID": task_id, "PlayerID": player_id}
                        response_task = requests.post(task_url, headers=task_headers, json=task_payload)
                        
                        if response_task.status_code == 200:
                            task_response = response_task.json()
                            if task_response.get('code') == 0:
                                clear_line()
                                print(Fore.GREEN + f"Task {task_id} berhasil dikerjakan!")
                                last_task_id = task_id  # Save the successful task ID
                                task_success = True
                                break
                            else:
                                clear_line()
                                print(Fore.YELLOW + f"Task {task_id} Cooldown", end='')
                                time.sleep(1)  # Add a small delay to make it readable
                        else:
                            clear_line()
                            print(Fore.RED + f"Request for Task {task_id} failed with status code: {response_task.status_code}", end='')
                            time.sleep(1)  # Add a small delay to make it readable

                    if task_success and last_task_id:
                        # Animate waiting message
                        animate_waiting_message(30)

                        # Step 5: OPTIONS request to /game/CompleteTask
                        complete_task_url = "https://api.prod.piggypiggy.io/game/CompleteTask"
                        complete_task_headers = {
                            "Accept": "*/*",
                            "Accept-Encoding": "gzip, deflate, br, zstd",
                            "Accept-Language": "en-US,en;q=0.9",
                            "Authorization": f"bearer {token}",
                            "Cache-Control": "no-cache",
                            "Content-Type": "application/json",
                            "Origin": "https://restaurant-v2.piggypiggy.io",
                            "Pragma": "no-cache",
                            "Referer": "https://restaurant-v2.piggypiggy.io/",
                            "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            "Sec-Ch-Ua-Mobile": "?0",
                            "Sec-Ch-Ua-Platform": '"Windows"',
                            "Sec-Fetch-Dest": "empty",
                            "Sec-Fetch-Mode": "cors",
                            "Sec-Fetch-Site": "same-site",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/126.0.0.0 Safari/537.36"
                        }
                        
                        response_options_task = requests.options(complete_task_url, headers=complete_task_headers)
                        
                        if response_options_task.status_code == 204:
                            clear_line()
                            print(Fore.BLUE + "OPTIONS untuk CompleteTask Berhasil Diterapkan")
                            
                            # Step 6: Complete the task using the correct task ID
                            complete_task_payload = {"TaskID": last_task_id, "PlayerID": player_id}
                            response_complete_task = requests.post(complete_task_url, headers=complete_task_headers, json=complete_task_payload)
                            
                            if response_complete_task.status_code == 200:
                                clear_line()
                                print(Fore.GREEN + "Task berhasil diselesaikan!")
                                
                                # Step 7: Get updated game data
                                response_updated_game = requests.post(game_url, headers=game_headers)
                                
                                if response_updated_game.status_code == 200:
                                    updated_game_data = response_updated_game.json().get('data', {})
                                    new_salary = updated_game_data.get('currrencyPool', 'No Salary')
                                    print(Fore.WHITE + f"Salary sekarang adalah {new_salary}")
                                    print(Fore.WHITE + "Melanjutkan ke Task Berikutnya...")
                                else:
                                    print(Fore.RED + "Gagal mendapatkan data game terbaru.")
                            else:
                                print(Fore.RED + "Gagal menyelesaikan task.")
                        else:
                            clear_line()
                            print(Fore.RED + "OPTIONS untuk CompleteTask gagal dengan status code:", response_options_task.status_code)
                    else:
                        clear_line()
                        print(Fore.RED + "Tidak ada task yang berhasil dikerjakan.")
                        break  # If no tasks were successful, break out of the loop
            else:
                print(Fore.RED + "Failed to get game data with status code:", response_game.status_code)
        else:
            print(Fore.RED + "GET request failed with status code:", response_get.status_code)
    else:
        print(Fore.RED + "OPTIONS request failed with status code:", response_options.status_code)

while True:
    for akun_data in akun_data_list:
        process_akun(akun_data)
    
    print(Fore.CYAN + "Semua akun Berhasil Di Check Cooldown...")
    animate_waiting_message(15 * 60)  # Cooldown for 15 minutes
