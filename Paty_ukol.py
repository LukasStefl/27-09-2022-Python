list = ['1','2','3','4','5','6']
vlozeni = int(input("Vlož číslo: "))
i = 0
while i < 7:
    if vlozeni == list[i]:
        print("Je stejné.")
        break;
    else:
        print("Není stejné.")
        break;
