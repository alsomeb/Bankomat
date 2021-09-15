accounts = {} # dictionary    #TERMCOLOR? för snygg GUI

def MainMenu():
    print("****HUVUDMENY****")
    print("1. Skapa konto")
    print("2. Administrera konto")
    print("3. Avsluta")

def AccountMenu():
    print("****KONTOMENY*****")
    print("1. Ta ut pengar")
    print("2. Sätt in pengar")
    print("3. Visa saldo")
    print("4. Avsluta")

while True:
    anykey = input("Tryck enter för att fortsätta: ")
    MainMenu()
    val = input("Ange menyval: ")

    if val == "3": #Avslutar bankomaten
        break

    if val == "1":
        while True:
            kontonummer = input("Ange ett nytt kontonr: ")
            if kontonummer in accounts:
                print("Kontonummret finns redan!")
                tryAgain = input("Vill du prova ett annat kontonummer, (j/n): ").lower()
                if tryAgain != "j":
                    break
            else:
                accounts[kontonummer] = 0  # Skapar ett nytt kontonummer i accounts med 0 saldo i dictionaryn (accounts[key] = value)
                break
    if val == "2":
        kontonummer = input("Ange kontonummer: ")
        while True:
            if kontonummer in accounts:
                anykey = input("Tryck enter för att fortsätta: ")
                AccountMenu()
                val = input("Ange menyval: ")
                
                if val == "4": #Avsluta
                    break
                if val == "1": #Ta ut pengar
                    uttag = int(input("Ange belopp: "))
                    saldo = accounts[kontonummer]
                    if uttag > saldo:
                        print(f"Du har inte tillräckligt på kontot, ditt saldo är {saldo}")
                    else:
                        accounts[kontonummer] = saldo - uttag
                        print(f"Du har gjort ett uttag på: {uttag}")

                if val == "3": #Visa saldo
                    saldo = accounts[kontonummer]
                    print(f"Ditt saldo är: {saldo}")

                if val == "2": #Sätt in pengar
                    insattning = int(input("Ange belopp: "))
                    saldo = accounts[kontonummer]
                    accounts[kontonummer] = saldo + insattning
                    print(f"Du har gjort en insattning på: {insattning}kr på ditt konto")
               
            else:
                print("Du har angivit fel kontonr, går tillbaka till huvudmeny")
                break