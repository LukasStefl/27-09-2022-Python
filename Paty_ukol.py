list = [1,2,3,4,5,6]
vlozeni = int(input("Vlož číslo: "))
for i in list:
    if(i == vlozeni):
        print("Je v poli")
    else:
        print("Není v poli.")