class atm:
    
    
    def __init__(self):
        self.accountnumber=912
        self.pin=912
        self.balance=5000
        self.menu()
        
        
    def menu(self):
        print("""
        PRESS 1 TO CHECK DETAILS OF YOUR ACCOUNT
        PRESS 2 TO CHANGE PIN OF YOUR ACCOUNT
        PRESS 3 TO WITHDRAWL CASH FROM YOUR ACCOUNT
        PRESS 4 TO ADD DEPOSITS TO YOUR ACCOUNT
        
        """)
        n=int(input("enter your response pls  "))
        
        if n==1:
            self.details()
        if n==2:
            self.pinch()
        if n==3:
            self.witd()
        if n==4:
            self.depos()
        
        
    def details(self):
        getac=int(input("enter your account number : "))
        getp=int(input("enter your pin number : ")) 
        
        if getac==self.accountnumber and getp==self.pin:
            print("you got access of **** \n" )
            print(f"your balance is {self.balance}")
        
        else :
            print("WRONG CREDENTIALSSS")
            
            
    
    def pinch(self):
        getac=int(input("enter your account number : "))
        getp=int(input("enter your pin number : ")) 
        
        if getac==self.accountnumber and getp==self.pin:
            print("you got access of **** \n" )
            print(f"your balance is {self.balance}")
            newpin=int(input("enter your new pin"))
            self.pin=newpin
        
        
            print("\n")
            print("Great your pass is changed now")
        
        else :
            print("WRONG CREDENTIALSSS")
            
    def witd(self):
        getac=int(input("enter your account number : "))
        getp=int(input("enter your pin number : ")) 
        
        if getac==self.accountnumber and getp==self.pin:
            print("you got access of **** \n" )
            print(f"your balance is {self.balance}")
            amt=int(input("enter your cash transaction  "))
            finl=self.balance-amt
            print(f"FINAL AMOUNT IS {finl}")
        
        
            print("\n")
            print("THANKS FOR TRANSACTION WITH US")
        
        else :
            print("WRONG CREDENTIALSSS")    
        
    def depos(self):
        getac=int(input("enter your account number : "))
        getp=int(input("enter your pin number : ")) 
        
        if getac==self.accountnumber and getp==self.pin:
            print("you got access of **** \n" )
            print(f"your balance is {self.balance}")
            amt=int(input("enter amount to deposit  "))
            finl=self.balance+amt
            print(f"FINAL AMOUNT IS {finl}")
        
        
            print("\n")
            print("THANKS FOR TRANSACTION WITH US")
            
        else :
            print("WRONG CREDENTIALSSS")    
            
        
my=atm()