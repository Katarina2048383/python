def ypologismos(plithos):
    if plithos >= 1 and plithos <=3:
        poso = plithos * 120
    elif plithos <= 6:
        poso = 3 * 120 + (plithos - 3) * 100
    else:
        poso = 3 * 120 + 3 * 100 + (plithos - 6) * 70
    
    return poso


esoda = 0
count = 0

for i in range(50):
    temaxia = int(input("Dwse arithmo temaxiwn: "))
    xrewsi = ypologismos(temaxia)
    print xrewsi
    esoda += xrewsi
    if temaxia > 10:
        count += 1

print esoda
print(count/50.0)*100

