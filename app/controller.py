import app.view
import app.account
import sys
import sqlite3
     
def main_menu_control():
    while True:
        answer = app.view.main_menu()
        if answer == "3":
            app.view.program_end()
            sys.exit()
        elif answer == "2":
            username = app.view.username_inpt()
            pword = app.view.password_inpt()  
            acct_login = app.account.Account.login(username, pword)
            app.view.saving_change()
            app.view.main_menu()
        elif answer == "2":
            currentaccount = model.account_login()
            if currentaccount is False:
                return main_menu()
            else:
                break
        elif answer == "1":
            currentaccount = model.get_inputs()
            if currentaccount is False:       #prompts to create account or returning False to exit
                return main_menu()
            else:
                sqlite.sql_record(currentaccount)
                view.acc_created(currentaccount[0])
                break
        else:
            view.choose_valid()
            continue
    
    currentcustom = model.Customer(currentaccount[1],currentaccount[2],\
                    currentaccount[0],currentaccount[3],currentaccount[4],currentaccount[5]) #class

    while True:
        pickup = view.banking_options(currentcustom.first_name, currentcustom.account_number)
        if pickup == "1":
            view.balance_statement(currentcustom.balance_fun())
            continue
        elif pickup == "2":
            while True:
                try: # checking if input is decimal
                    amount = int(view.deposit_inpt()) #input amount
                    break
                except ValueError:
                    view.choose_valid()
                    continue
                    
            currentcustom.deposit(amount)   # class deposit function
            sqlite.sql_update(currentcustom.account_number,currentcustom.balance)                # SQL update
            view.deposit_outp(amount)
            view.newbalance_statement(currentcustom.balance_fun()) # print new balance
            continue
        elif pickup == "3":
            while True:
                try:
                    amount = float(view.withdrawal_inpt())
                    break
                except ValueError:
                    view.choose_valid()
                    continue
            if amount > currentcustom.balance:
                view.not_funds(amount)
                view.balance_statement(currentcustom.balance_fun())
                continue
            else:
                currentcustom.withdrawal(amount) # class withdrawal function
                sqlite.sql_update(currentcustom.account_number,currentcustom.balance)                # SQL update
                view.withdrawal_outp(amount)
                view.newbalance_statement(currentcustom.balance_fun()) # print new balance
                continue
        elif pickup == "4":
            break
        else:
            view.choose_valid()
            continue
    main_menu_control()

app.view.welcome()
main_menu_control()

