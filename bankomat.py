import json
import datetime
import time
from functions import MainMenu
from functions import AccountMenu
from termcolor import colored,cprint #färger används för snygg "GUI"
accounts = {} #konton
log_list = {} #loggar transaktioner i trans.json

with open("log.json") as json_file: #öppnar fil för kontonr och tillhörande saldo
    accounts = json.load(json_file)


with open("trans.json") as json_file: #öppnar fil för transaktioner
     log_list = json.load(json_file)


#start, såg mer fördelar köra inputsen som string, om man skrev fel så loopas menyn bara om, förutom belopp körs med INT
while True:
    anykey_text = colored("Tryck enter för att fortsätta: ", color="green", attrs=["bold"])#färg och atr för anykey
    anykey = input(anykey_text)#gör så att det blir snyggare med outputen, men kan bli tjatigt kanske
    MainMenu()
    val_text = colored("Ange menyval: ", color="green", attrs=["bold"]) #val styling
    val = input(val_text)

    if val == "3": #Avslutar bankomaten
        break
    if val == "1":
        while True:
            kontonummer = input(colored("Ange ett nytt kontonr: ", 'green', attrs=['bold'])) #annan metod för styling
            if kontonummer in accounts:
                cprint("Kontonummret finns redan!", 'red', attrs=['bold'])
                tryAgain = input(colored("Vill du prova ett annat kontonummer, (j/n): ", 'green', attrs=['bold']).lower()) #om kontonr nr redan finns = felmed
                if tryAgain != "j":
                    break
            else:
                cprint(f"Du har skapat ett konto med kontonr: {kontonummer}", 'green', attrs=['bold'])
                accounts[kontonummer] = 0  # Skapar ett nytt kontonummer i accounts med 0 saldo i dictionaryn (accounts[key] = value)
                log_list[kontonummer] = [] # lägger in en tom lista i dict value (nesting). Tex kontonr "123" = [tom lista]
                break
    if val != "3" and val != "2" and val != "1": #felmed om ej valt rätt menyval
        print(colored("Du måste välja en siffra mellan 1-3", 'red', attrs=['bold']))
    if val == "2":
        kontonummer = input(colored("Ange kontonummer: ", 'green', attrs=['bold']))
        while True:
            if kontonummer in accounts:
                anykey_text = colored("Tryck enter för att fortsätta: ", color="green", attrs=["bold"])
                anykey = input(anykey_text)
                AccountMenu()
                val_text2 = colored("Ange menyval: ", color="green", attrs=["bold"]) #val styling
                val = input(val_text2)
                
                if val == "5": #Avsluta
                    break
                if val == "1": #Ta ut pengar
                    uttag = input(colored("Ange belopp: ", 'green', attrs=['bold']))
                    if uttag.isnumeric(): #kollar att det är siffror
                        uttag = int(uttag) #gör om inputen till en int
                        saldo = accounts[kontonummer]
                        if uttag > saldo:
                            print(colored(f"Du har inte tillräckligt på kontot, ditt saldo är {saldo}", 'red', attrs=['bold']))
                        elif uttag == 0:
                            print(colored("Du måste ange högre än 0kr", "red", attrs=['bold']))
                        else:
                            accounts[kontonummer] = saldo - uttag
                            print(colored(f"Du har gjort ett uttag på: {uttag}", 'green', attrs=['bold']))
                            log_list[kontonummer].append(colored(f"{datetime.date.today()}, {time.strftime('%H:%M')}, UTTAG: {uttag}kr", 'red', attrs=['bold']))
                    else:
                        cprint("Endast siffror tillåtna, ej bokstäver och specialtecken!", 'red', attrs=['bold']) #kodat så att man ej kan skriva +,- eller andra bokstäver

                if val == "3": #Visa saldo
                    saldo = accounts[kontonummer]
                    print(colored(f"Ditt saldo är: {saldo}", 'green', attrs=['bold']))

                if val == "2": #Sätt in pengar
                    insattning = input(colored("Ange belopp: ", 'green', attrs=['bold']))
                    if insattning.isnumeric(): #kollar att det är siffror
                        insattning = int(insattning)
                        saldo = accounts[kontonummer]
                        accounts[kontonummer] = saldo + insattning
                        print(colored(f"Du har gjort en insattning på: {insattning}kr på ditt konto", 'green', attrs=['bold']))
                        log_list[kontonummer].append(colored(f"{datetime.date.today()}, {time.strftime('%H:%M')}, INSÄTTNING: {insattning}kr", 'green', attrs=['bold']))
                    elif insattning == 0:
                            print(colored("Du måste ange högre än 0kr", "red", attrs=['bold']))
                    else:
                        cprint("Endast siffror tillåtna, ej bokstäver och specialtecken!", 'red', attrs=['bold']) #kodat så att man ej kan skriva +,- eller andra bokstäver
                    
                if val == "4": #Loopar igenom trans.json filen och printar transaktionshistoriken för aktuellt konto
                    for trans in log_list[kontonummer]:
                        print(f"{trans}\n")

                if val != "1" and val != "2" and val != "3" and val != "4" and val != "5": #felmed om ej valt rätt menyval
                    print(colored("Du måste välja en siffra mellan 1-5", 'red', attrs=['bold']))
               
            else:
                cprint("Du har angivit fel kontonr, går tillbaka till huvudmeny", 'red', attrs=['bold'])
                break

    #döpte variablerna bara till random bokstäver, har inge större betydelse, bara komma ihåg att skriva dem rätt
    j = json.dumps(accounts)
    with open("log.json", "w") as f: #sparar kontonr och tillhörande saldo
        f.write(j)
    
    t = json.dumps(log_list)
    with open("trans.json", "w") as f: #spara transaktioner
        f.write(t)

