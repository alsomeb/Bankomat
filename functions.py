from termcolor import colored,cprint
#Funktioner som används i bankomaten, tänkte lägga till mer men blev termcolor istället

def MainMenu(): #Med termcolor
    menu = colored("****HUVUDMENY****", color="green", attrs=["reverse", "bold"])
    print(menu)
    print("1. Skapa konto")
    print("2. Administrera konto")
    print("3. Avsluta")

def AccountMenu():
    acc_menu = colored("****KONTOMENY****", color="green", attrs=["reverse", "bold"])
    print(acc_menu)
    print("1. Ta ut pengar")
    print("2. Sätt in pengar")
    print("3. Visa saldo")
    print("4. Lista transaktioner")
    print("5. Avsluta")
