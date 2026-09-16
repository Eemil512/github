import sys  # import
 
ostoslista = []          # variable: list (data type)
lista = True               # variable: bool (data type)
 
while lista:
    print("1-Lisää  2-Näytä  3-Lopeta")   # print()
    choice = input("Valitse: ")       # input(), str (data type)
 
    if choice == "1":
        tavara = input("Tavaran nimi: ")  # str
        kpl = int(input("Määrä: "))  # int (data type)
        ostoslista.append((tavara, kpl))
        print(f"Added {kpl}x {tavara}")
    elif choice == "2":
        if not ostoslista:
            print("List is empty!")
        else:
            for nimi, määrä in ostoslista:   # for-loop
                print(f"- {nimi}: {määrä}")
    elif choice == "3":
        lista = False
        print("Näkemiin!")
    else:
        print("Paina numeroa 1, 2 tai 3")
 
sys.exit()