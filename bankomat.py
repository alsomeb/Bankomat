import json
import datetime
import time
accounts = {} #konton, finns ett 123 test konto i log.json, den måste finnas där annars körs ej programmet
log_list = {} #loggar transaktioner i trans.json, samma som ovan

with open("log.json") as json_file: #öppnar fil för kontonr och tillhörande saldo
    accounts = json.load(json_file)

with open("trans.json") as json_file: #öppnar fil för transaktioner
    log_list = json.load(json_file)

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
    print("4. Lista transaktioner")
    print("5. Avsluta")

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
                tryAgain = input("Vill du prova ett annat kontonummer, (j/n): ").lower() #om kontonr nr redan finns = felmed
                if tryAgain != "j":
                    break
            else:
                accounts[kontonummer] = 0  # Skapar ett nytt kontonummer i accounts med 0 saldo i dictionaryn (accounts[key] = value)
                log_list[kontonummer] = [] # lägger in en tom lista i dict value (nesting). Tex kontonr "123" = []
                break
    if val == "2":
        kontonummer = input("Ange kontonummer: ")
        while True:
            if kontonummer in accounts:
                anykey = input("Tryck enter för att fortsätta: ")
                AccountMenu()
                val = input("Ange menyval: ")
                
                if val == "5": #Avsluta
                    break
                if val == "1": #Ta ut pengar
                    uttag = input("Ange belopp: ")
                    if uttag.isnumeric() == True:
                        uttag = int(uttag) #gör om inputen till en int
                        saldo = accounts[kontonummer]
                        if uttag > saldo:
                            print(f"Du har inte tillräckligt på kontot, ditt saldo är {saldo}")
                        else:
                            accounts[kontonummer] = saldo - uttag
                            print(f"Du har gjort ett uttag på: {uttag}")
                            log_list[kontonummer].append(f"{datetime.date.today()}, {time.strftime('%H:%M')}, UTTAG: {uttag}kr")
                    else:
                        print("Endast siffror tillåtna, ej bokstäver och specialtecken!") #kodat så att man ej kan skriva +,- eller andra bokstäver

                if val == "3": #Visa saldo
                    saldo = accounts[kontonummer]
                    print(f"Ditt saldo är: {saldo}")

                if val == "2": #Sätt in pengar
                    insattning = input("Ange belopp: ")
                    if insattning.isnumeric() == True:
                        insattning = int(insattning)
                        saldo = accounts[kontonummer]
                        accounts[kontonummer] = saldo + insattning
                        print(f"Du har gjort en insattning på: {insattning}kr på ditt konto")
                        log_list[kontonummer].append(f"{datetime.date.today()}, {time.strftime('%H:%M')}, INSÄTTNING: {insattning}kr")
                    else:
                        print("Endast siffror tillåtna, ej bokstäver och specialtecken!") #kodat så att man ej kan skriva +,- eller andra bokstäver
                    
                if val == "4": #Loopar igenom trans.json filen och printar transaktionshistoriken för aktuellt konto
                    for trans in log_list[kontonummer]:
                        print(f"{trans}\n")
               
            else:
                print("Du har angivit fel kontonr, går tillbaka till huvudmeny")
                break

    j = json.dumps(accounts)
    with open("log.json", "w") as f: #sparar kontonr och tillhörande saldo
        f.write(j)
    
    t = json.dumps(log_list)
    with open("trans.json", "w") as f: #spara transaktioner
        f.write(t)

