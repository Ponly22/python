print("Hello (^_^)")
exi = True
while exi == True:
    print("----MENU----\n1.Register\n2.Login\n3.Exit")
    menu = int(input())
    if menu==1:
        print("--REGISTER--")
        userR = str(input("USERNAME:"))
        plassR = str(input("PLASSWORD:"))
        print("Register successfuly")
    elif menu==2:
        print("--LOGIN--")
        userL = str(input("USERNAME:"))
        plassL = str(input("PLASSWORD:"))
        if userL==userR and plassL==plassR:
            print("Login successfuly")
            exi = False
        else:
            print("Try it again")
    elif menu==3:
        print("END")
        exi = False
    else:
        print("ERROR\nplease try it again")