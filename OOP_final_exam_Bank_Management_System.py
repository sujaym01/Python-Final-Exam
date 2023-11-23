class Bank:
    bank_accounts_list = []         # class attribute
    total_balance = 5000 
    total_loan_amount = 0 
    loan_status = True 
    bankrupt_status = False
    
    def Create_account(self):       # method
        # self.bank_accounts_list.append(self)
        Bank.bank_accounts_list.append(self)

    
    def delete_account(self, account_number):
        for account in Bank.bank_accounts_list:
            if account.accountNo == account_number:
                Bank.bank_accounts_list.remove(account)
                print(f"\n{account} ----->account  object delite successful")

    def show_all_users(self):
        print(f"\n<-------Show All User------->\n")
        for user in Bank.bank_accounts_list:
            print(f"\nName: {user.name}")   
            print(f"Account Number: {user.accountNo}")
            

    def show_total_balance(self):
        print(f"Total Balance Of Bank: {self.total_balance}")

    def show_total_loan(self):
        print(f"Total Loan Balance From Bank : {self.total_loan_amount}") 

    def loan_status_on_off(self,bool_obj):
        # self.loan_status=bool_obj  use korle class attribute update hobe na
        Bank.loan_status = bool_obj

    # def loan_status_off(self,bool_obj):
    #     Bank.loan_status = bool_obj

    def cheek_loan_status(self):
        return self.loan_status
    
    def bankrupt(self,v):
        Bank.bankrupt_status = v

    def cheek_bankrupt_status(self):
        return self.bankrupt_status

class Account(Bank):
    def __init__(self, name, email, password, address, account_type):
        self.name = name
        self.email = email
        self.addre = address
        self.passW = password
        self.balance = 0
        self.atype = account_type
        self.loan_taken = 0
        self.transactions = []
        account_number = len(self.name)+len(self.email)
        self.accountNo=account_number
        print(f"\nYour account number : {self.accountNo}")        # atomatic account number dekhar jonno
        
        # Account.Create_account(self)
        self.Create_account()
        

# ..........1   
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            self.transactions.append({'deposited $':amount})
            Bank.total_balance += amount
            print(f"\n<----Diposited Successful ${amount}. Your New balance: ${self.balance}---->\n")
        else:
            print(f"\nInvalid Deposit Amount: ${amount}")      
            
# .........2
    def withdraw(self,  amount):
        if self.balance >= amount:
            if  Bank.bankrupt_status == False and Bank.total_balance >= amount:
                Bank.total_balance -= amount
                self.transactions.append({'withdrawal $':amount})
                self.balance -= amount
                print(f"\n<----Withdraw Successful ${amount}. Your New balance ${self.balance}---->\n")          
            else:
                print(f"\nYou Have Sufficiant Balance ${self.balance} But The Bank Is Bankrupt.")
        else:
            print(f"\nWithdrawal Amount ${amount} Exceeded.")
            
                        
# .......3
    def take_loan(self, loan_amount):
                if Bank.bankrupt_status==False and Bank.loan_status:
                    if  self.loan_taken < 2:
                        self.balance += loan_amount
                        self.loan_taken += 1
                        # self.transactions.append(f"Loan taken: ${loan_amount}")
                        self.transactions.append({'loan taken $':loan_amount})
                        Bank.total_loan_amount += loan_amount
                        Bank.total_balance -= loan_amount
                        print(f"\n<----Your Loan Amount ${loan_amount} Successful .Your New balance ${self.balance}--->\n")
                    else:
                        print("\nMaximum Loans Taken")
                else:
                    print("\nLoan Feature Disabled")
            

# .........4   
    def transfer_amount(self, receiver, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Transfered ${amount} To Account Number {receiver.accountNo}")
            receiver.balance +=amount
            receiver.transactions.append(f"Received ${amount} From Account Number {self.accountNo}")
            print(f"\n<----Transfered Amount ${amount} Successful.Your New Balance ${self.balance} ---->\n")
        else:
            print("\nInsufficient Funds For Transfer")
         

# .......5 
    def check_balance(self):
        print(f"\nYour Available Balance ${self.balance}")
                

# ........6    
    def check_transactions(self):
        print(f"\nYour Transection History :{self.transactions}")
                
            
# # ........6    
#     def check_transactions(self, account_number):
#         for account in Bank.bank_accounts_list:
#             if account.accountNo == account_number and currentUser.accountNo == account_number:
#                 print(f"Your transection history :{self.transactions}")
#                 # return self.transactions
#             else:
#                 print(f" Your Account Number {account_number} Does Not Exceeded")
#         # return None
    
               

admin_account_number = Account("Admin", "admin@email.com",1234, "Khulna","Admin")

print(f"Admin account number : {admin_account_number.accountNo}")
print(f"Admin password : {admin_account_number.passW}")



currentUser=None

while(True):
    if currentUser==None:
        print("\nWho are you ?")
        print("\n-->1. User")
        print("-->2. Admin")
        op = int(input("\nChoice Option:"))
        if op == 1:
            print("\n-->1. Register")
            print("-->2. Loging")
            op = int(input("\nChoice Option:"))
            if op == 1:
                name = input("Name:")
                email = input("Email:")
                passw = int(input("Password:"))
                addre = input("Address:")
                actype=input("Savings Account or special Account (sv/cu) :")
                if actype == "sv":
                    currentUser = Account(name,email,passw,addre,"Savings")
                else:
                    currentUser = Account(name,email,passw,addre,"Current") 

            elif op == 2:
                no=int(input("Account Number:"))
                pa = int(input("Password:"))
                variable=None
                for account in Bank.bank_accounts_list:
                    if account.accountNo == no and account.passW == pa:
                        currentUser=account
                        variable=no
                        break
                    else:
                        pass
                if variable==None:
                     print(f"Rong Account Number {no} Or Password {pa}")
                               
            else:
                 print("\nInvalid Option")
                 
        elif op == 2:   
                print(f"\n<---------Admin Account Login----------->\n")
                no=int(input("Account Number :"))
                pasword=int(input("Password :"))
                if admin_account_number.passW == pasword and admin_account_number.accountNo == no:
                    admin=None
                    while(True):
                        if admin==None:
                            print(f"\nWelcome {admin_account_number.name} !\n")

                            print("1. Create account")
                            print("2. Delite account")
                            print("3. Get all  account")
                            print("4. Get total balance of bank")
                            print("5. Get total loan amount from bank")
                            print("6. Loan status On")
                            print("7 Loan status Off")
                            print("8 Loan status Cheek")
                            print("9 Bankrupt status on")
                            print("10 Bankrupt status off")
                            print("11 Bankrupt status cheek")
                            print("12. Logout\n")
                                        
                            op = int(input("Choice Option:"))
                            if op == 1:
                                name = input("Name:")
                                email = input("Email:")
                                passw = int(input("Password:"))
                                addre = input("Address:")
                                actype=input("Savings Account or special Account (sv/cu) :")
                                if actype == "sv":
                                    currentUser = Account(name,email,passw,addre,"Savings")
                                else:
                                    currentUser = Account(name,email,passw,addre,"Current") 

                                        
                            elif op == 2:
                                    acno = int(input(" User Account Number :"))
                                    admin_account_number.delete_account(acno)

                            elif op == 3:
                                    admin_account_number.show_all_users()

                            elif op == 4:
                                    admin_account_number.show_total_balance()

                            elif op == 5:
                                    admin_account_number.show_total_loan()

                            elif op == 6:
                                    admin_account_number.loan_status_on_off(True)
                                
                            elif op == 7:
                                    admin_account_number.loan_status_on_off(False)
                            elif op == 8:
                                    status=admin_account_number.cheek_loan_status()
                                    print(f"\nLoan Status : {status}")
                            elif op == 9:
                                    admin_account_number.bankrupt(True)
                                
                            elif op == 10:
                                    admin_account_number.bankrupt(False)
                            elif op == 11:
                                    status=admin_account_number.cheek_bankrupt_status()
                                    print(f"\nBankrupt Status : {status}")

                            elif op == 12:
                                print("\nEXIST")
                                currentUser = None
                                break       
                            else:                  
                                print("\nInvalid Option")             
                else:
                    print("\nAdmin Account Number Or Password Is Rong")
        else:
            print("\nInvalid Option")
    
                    
    else:
        print(f"\nWelcome {currentUser.name} !\n")
        if currentUser.atype=="Savings" or "Current":
             
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Take Loan")
            print("4. Transfer Amount")
            print("5. Check Your Available Balance")
            print("6. Check Transaction History")
            print("7. Logout\n")           
                                                              
            op = int(input("Choice Option: "))
                                
            if op == 1:
                # acno = currentUser.accountNo
                # acno = int(input("Enter Your Account Number :"))
                amount = int(input("Enter Deposit Amount : "))
                currentUser.deposit(amount)
                                
            elif op == 2:
                # acno = int(input("Enter Your Account Number :"))
                amount = int(input("Enter Withdraw Amount : "))
                currentUser.withdraw(amount)
            elif op == 3:
                # acno = int(input("Enter Your Account Number :"))
                amount = int(input("Enter Take Loan Amount : "))
                currentUser.take_loan(amount)
                                
            elif op == 4:
                R = int(input("Enter Receiver Account Number : "))
                amount=int(input("Enter Transfer Amount : "))
                vari=None
                for  receiver in Bank.bank_accounts_list:
                    if  receiver.accountNo == R:
                        currentUser.transfer_amount(receiver,amount)
                        vari = R
                    else:
                        pass
                if vari == None:
                     print(f"\nReceiver Account Number {R} Doesn't Exist ") 


            elif op == 5:
                # acno = int(input("Enter Your Account Number :"))
                currentUser.check_balance()

            elif op == 6:
                # acno = int(input("Enter Your Account Number :"))
                currentUser.check_transactions()

            elif op == 7:
                currentUser = None
                print("EXIST")
            else:
                print("Invalid Option")
        else:
            pass                  


# # 1.self.bank_accounts_list.append(self)
# # 1.Bank.bank_accounts_list.append(self)
# # 2.self.create_account()
# # Account.create_account(self)

# # 2.self.create_account(self)
# # TypeError: Bank.create_account() takes 1 positional argument but 2 were given

#  if Bank.loan_status == True and self.loan_taken < 2: