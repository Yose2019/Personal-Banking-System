#python banking system

import datetime
import json
#we will have a wallet class
#we will have a bank class

class transaction:
    def __init__(self,title,amount,typ,note=''):
        self.title=title
        self.amount=amount
        self.typ=typ
        self.note=note

    def display_info(self):
        return f"Transaction:\nExpense:{self.title}\nAmount:{self.amount}\nTyp:{self.typ}\nNote:{self.note}"

class bank:
    def __init__(self):
        self.wallet = []

    def add_transaction(self,transaction):
        self.wallet.append(transaction)

    def remove_transaction(self,title):
        for trans in self.wallet:
            if trans.title==title:
                self.wallet.remove(trans)
                return f"{title} has been removed"
        return f"{title} has not been found"


    def display(self):
        if not self.wallet:
            return f"No transactions available in your wallet"
        return f"\n".join([transaction.display_info() for transaction in self.wallet])

    def search_wallet(self,query):
        found=[trans for trans in self.wallet if query.lower() in trans.title.lower() or query.lower() in trans.typ.lower()]
        if not found:
            return f"No transactions"
        return "\n".join([transaction.display_info() for transaction in found])

    def save_file(self,filename="wallet.json"):
        data=[{'Expense':transaction.title,'Amount':transaction.amount,'Type':transaction.typ,'Note':transaction.note} for transaction in self.wallet]
        with open(filename,'w') as file:
            json.dump(data,file)

    def load_file(self,filename="wallet.json"):
        try:
            with open(filename,'r') as file:
                data=json.load(file)
                self.wallet=[transaction(trans['Expense'],trans['Amount'],trans['Type'],trans['Note']) for trans in data]
        except FileNotFoundError:
            print("We don't have that file")
        

def main():
    wallet=bank()

    while True:
        print("*"*30 + "Personal Banking System"+"*"*30)
        print("1.Add a transaction")
        print("2.Remove a transaction")
        print("3.Display all transaction")
        print("4.Search for a transaction")
        print("5.Save transaction to file")
        print("6.Load transaction to file")
        print("7.Exit")
        choice=input("Enter the operation to be performed 1-7:")

        if choice=='1':
            title=input("Enter the title:")
            amount=float(input("Enter amount:"))
            typ=input("Expense or Deposit:")
            transactn=transaction(title,amount,typ)
            wallet.add_transaction(transactn)
            print(f"{title} added succesfully")
        elif choice=='2':
            title=input("Enter the title:")
            print(wallet.remove_transaction(title))

        elif choice=='3':
            print(wallet.display())

        elif choice=='4':
            query=input("Enter the query:")
            print(wallet.search_wallet(query))
            
        elif choice=='5':
            wallet.save_file()
            print("Saved as JSON")

        elif choice=='6':
            wallet.load_file()
            print("Loaded JSON")

        elif choice=='7':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice")
            
            
if __name__ in '__main__':
    main()
    
