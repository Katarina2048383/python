def ypologismos(plith):
    if plith<=3:
        timi=plith*20
    elif plith<=6:
        timi=3*120+(plith-3)*100
    elif plith>6:
        timi=3*120+3*100+(plith-6)*70
    return timi
m=0
s=0
for k in range(3):
    plith=int(input("dose poso temaxion"))
    timi=ypologismos(plith)
    s=s+timi
    if plith>=10:
        m=m+1
print("to xreos tou pelati einai",timi)
print("ta esoda tou magaziou einai",s,"kai eixe",m,"pelates pou piran pano apo 10 temaxia")
