#Last Project
#CurrencyConverter #Wichaphon Buathong 6/1 No.2

#FunctionMenu
def MenuSelect():
    print("------------------------")
    print("[1] ดอลลาร์สหรัฐ (USD)")
    print("[2] ยูโร (EUR)")
    print("[3] ปอนด์อังกฤษ (GBP)")
    print("[4] เยนญี่ปุ่น (JPY)")
    print("[5] ดอลลาร์แคนาดา (CAD)")
    print("------------------------")
    

#StartMenuFunc
def Interface() :
    print()
    print("[Welcome to currency converter]")
    print("[To start program or not? press (y/n)]")
    print()
    

#CurrencyFunc-----------------------------------------------------------

#USD
def USD_List() :
    print("----[Select List]----")
    print("    [1] USD --> THB")
    print("    [2] THB --> USD")
    print()
    select = input("Select [1] or [2] : ")
    if select == '1' :
        money = float(input("Input your money [USD] : "))
        THB = money * 36.26
        lim_THB = round(THB,2)
        print("--->",money,"USD","is",lim_THB,"THB.")
        print()

    elif select == '2' :
        money = float(input("Input your money [THB] : "))
        USD = money / 36.26
        lim_USD = round(USD,2)
        print("--->",money,"THB","is",lim_USD,"USD.")
        print()
    else :
        print("Invalid Option!")

#EUR
def EUR_List() :
    print("----[Select List]----")
    print("    [1] EUR --> THB")
    print("    [2] THB --> EUR")
    print("")
    select = input("Select [1] or [2] : ")
    if select == '1' :
        money = float(input("Input your money [EUR] : "))
        THB = money * 36.78
        lim_THB = round(THB,2)
        print("--->",money,"EUR","is",lim_THB,"THB.")
        print()

    elif select == '2' :
        money = float(input("Input your money [THB] : "))
        EUR = money / 36.78
        lim_EUR = round(EUR,2)
        print("--->",money,"THB","is",lim_EUR,"EUR.")
        print()
    else :
        print("Invalid Option!")

#GBP
def GBP_List() :
    print("----[Select List]----")
    print("    [1] GBP --> THB")
    print("    [2] THB --> GBP")
    print()
    select = input("Select [1] or [2] : ")
    if select == '1' :
        money = float(input("Input your money [GBP] : "))
        THB = money * 42.48
        lim_THB = round(THB,2)
        print("--->",money,"GBP","is",lim_THB,"THB.")
        print()

    elif select == '2' :
        money = float(input("Input your money [THB] : "))
        GBP = money / 42.48
        lim_GBP = round(GBP,2)
        print("--->",money,"THB","is",lim_GBP,"GBP.")
        print()
    else :
        print("Invalid Option!")

#JPY
def JPY_List() :
    print("----[Select List]----")
    print("    [1] JPY --> THB")
    print("    [2] THB --> JPY")
    print()
    select = input("Select [1] or [2] : ")
    if select == '1' :
        money = float(input("Input your money [JPY] : "))
        THB = money * 0.25
        lim_THB = round(THB,2)
        print("--->",money,"JPY","is",lim_THB,"THB.")
        print()

    elif select == '2' :
        money = float(input("Input your money [THB] : "))
        JPY = money / 0.25
        lim_JPY = round(JPY,2)
        print("--->",money,"THB","is",lim_JPY,"JPY.")
        print()
    else :
        print("Invalid Option!")

# CAD
def CAD_List() :
    print("----[Select List]----")
    print("    [1] CAD --> THB")
    print("    [2] THB --> CAD")
    print()
    select = input("Select [1] or [2] : ")
    if select == '1' :
        money = float(input("Input your money [CAD] : "))
        THB = money * 27.97
        lim_THB = round(THB,2)
        print("--->",money,"CAD","is",lim_THB,"THB.")
        print()

    elif select == '2' :
        money = float(input("Input your money [THB] : "))
        CAD = money / 27.97
        lim_CAD = round(CAD,2)
        print("--->",money,"THB","is",lim_CAD,"CAD.")
        print()
    else :
        print("Invalid Option!")

#-----------------------------------------------------------------------



#Start
Interface()
user_input = input("----------> (y/n)? : ")

while user_input != 'n' :
    if user_input == 'y' :
        MenuSelect()
        category = input("Enter your category : ")
        if category == '1' :
            print()
            print(">>>> [1] ดอลลาร์สหรัฐ (USD)")
            USD_List()
        elif category == '2' :
            print()
            print(">>>> [2] ยูโร (EUR)")
            EUR_List()
        elif category == '3' :
            print()
            print(">>>> [3] ปอนด์อังกฤษ (GBP)")
            GBP_List()
        elif category == '4' :
            print()
            print(">>>> [4] เยนญี่ปุ่น (JPY)")
            JPY_List()
        elif category == '5' :
            print()
            print(">>>> [5] ดอลลาร์แคนาดา (CAD)")
            CAD_List()
        else :
            print("Invalid option!")
            print("------------------------")
            print()

    
    else :
        print()
        print("[Error please press (y/n) only!!!!!!!]")
        print()
    
    user_input = input("Want to try more (y/n)? : ")

print()
print("Exit Program ~ ~ ~ ~")
print()
print("-------------------------------")








    



