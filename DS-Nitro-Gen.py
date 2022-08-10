import ctypes
import string
import os
import time
import sqlite3

USE_WEBHOOK = True

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

try:
    from discord_webhook import DiscordWebhook
except ImportError:
    input(
        f"Модуль discord_webhook не установлен, для установки запустите '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nВы можете игнорировать эту ошибку, если не собираетесь использовать веб-перехватчик..\nНажмите Enter, чтобы продолжить."
    )
    USE_WEBHOOK = False
try:
    import requests
except ImportError:
    input(
        f"Запросы модуля не установлены, для установки запустите '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nНажмите Enter, чтобы выйти"
    )
    exit()
try:
    import numpy
except ImportError:
    input(
        f"Модуль numpy не установлен, для установки запустите '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nНажмите Enter, чтобы выйти"
    )
    exit()

url = "https://github.com"
try:
    response = requests.get(url)
    print("проверка интернета")
    time.sleep(.4)
except requests.exceptions.ConnectionError:

    input(
        "Вы не подключены к Интернету, проверьте подключение и повторите попытку..\nНажмите Enter, чтобы выйти"
    )
    exit()


class NitroGen:
    def __init__(self):
        self.fileName = "Nitro Codes.txt"

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generator and Checker - Создал 童磨#2478")
        else:
            print(f'\33]0;Nitro Generator and Checker - Создал 童磨#2478\a',
                  end='',
                  flush=True)

        print(""" █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗██╗  ██╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██║╚██╗██╔╝
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║██║ ╚███╔╝
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██║ ██╔██╗
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║██║██╔╝ ██╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
                                                        """)
        time.sleep(2)
        self.slowType("Создал: 童磨#2478 ", .02)
        time.sleep(1)
        self.slowType("\nВведите количество кодов для генерации и проверки: ",
                      .02,
                      newLine=False)

        try:
            num = int(input(''))
        except ValueError:
            input("Указанный ввод не был числом.\nНажмите Enter, чтобы выйти")
            exit()

        if USE_WEBHOOK:

            self.slowType(
                "Если вы хотите использовать веб-хук Discord, введите его здесь или нажмите Enter, чтобы игнорировать: ",
                .02,
                newLine=False)
            url = input('')
            webhook = url if url != "" else None

            if webhook is not None:
                DiscordWebhook(
                    url=url,
                    content=
                    f"```Начал проверять URL\nЯ отправлю все действительные коды здесь```"
                ).execute()

        valid = []
        invalid = 0
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        c = numpy.random.choice(chars, size=[num, 23])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except KeyboardInterrupt:

                print("\nПрервано пользователем")
                break

            except Exception as e:
                print(f" Error | {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Создал 童磨#2478"
                )
                print("")
            else:
                print(
                    f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Создал 童磨#2478\a',
                    end='',
                    flush=True)

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid)}""")

        input("\nКонец! Нажмите Enter 5 раз, чтобы закрыть программу.")
        [input(i) for i in range(4, 0, -1)]

    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:
            print(i, end="", flush=True)
            time.sleep(speed)
        if newLine:
            print()

    def quickChecker(self, nitro: str, notify=None):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f" Valid | {nitro} ",
                  flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:
                file.write(nitro)

            if notify is not None:
                DiscordWebhook(
                    url=url,
                    content=
                    f"Обнаружен действительный код Nito! @everyone \n{nitro}"
                ).execute()

            return True
        else:
            print(f" Invalid | {nitro} ",
                  flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False


if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()