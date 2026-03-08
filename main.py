import json

class Wallet:
    def __init__(self, filename):
        self.filename = filename
        self.data = {
            "balance": 0.0,
            "history": []
        }
        # Immediately try to load existing data
        self.load_data()

    def load_data(self):
        """
        Try to open the file 'r'. 
        If FileNotFoundError, we just keep the default data (0 balance).
        If JSONDecodeError, we warn the user.
        """
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)

        except FileNotFoundError:
            print("No previous file found. Starting new wallet.")
        except json.JSONDecodeError:
            print("File corrupted! Starting with empty wallet.")

    def save_data(self):
        """
        Write self.data to the file using json.dump
        """
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)

    def transfer(self, amount, type, desc):
        if type=='income':
            self.data['balance'] += amount
        else:
            if self.data['balance'] < amount:
                print('Transfer failed!')
                return
            self.data['balance'] -= amount

        transaction = {}
        transaction['type'] = type
        transaction['amount'] = amount
        transaction['desc'] = desc.strip().lower()
        self.data['history'].append(transaction)

        self.save_data()
        print(f"Transfered successfully!")
        

    def show_history(self):
        print("\n--- Transaction History ---")
        # TODO: Loop through self.data['history'] and print each item
        for histo in self.data['history']:
            print(f"{histo['type'].upper()}: ${histo['amount']} ({histo['desc'].capitalize()})")
        print(f"Current Balance: {self.data['balance']}")
        print("---------------------------\n")

    def search_history(self, term):
        founded_results = [histo for histo in self.data['history'] if term.lower() in histo['desc']]
        
        if len(founded_results)==0: 
            print("\n--- Transaction History ---")
            print('--- Nothing found! ---')
            print("---------------------------\n")
            return

        print("\n--- Transaction History ---")
        for histo in founded_results:
            print(f"{histo['type'].upper()}: ${histo['amount']} ({histo['desc'].capitalize()})")
        print("---------------------------\n")

# --- MAIN PROGRAM LOOP ---
def main():
    my_wallet = Wallet("my_finance.json")

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Show History")
        print("4. Search")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Amount: "))
                if amount < 0 or amount == 0:
                    print('Amount is not valid!')
                    continue
                reason = input("Description: ")
                my_wallet.transfer(amount, 'income', reason)
            except ValueError:
                print("Invalid number! Please enter a valid amount.")

        elif choice == '2':
            # TODO: Ask for amount and reason, handle ValueError, call add_expense
            try:
                amount = float(input('Amount: '))
                if amount < 0 or amount == 0:
                    print('Amount is not valid!')
                    continue
                reason = input('Reason: ')
                my_wallet.transfer(amount, 'expense', reason)
            except ValueError:
                print('Amount is not number')

        elif choice == '3':
            # TODO: Call the show_history method
            my_wallet.show_history()

        elif choice == '4':
            term = input('Search Term: ')
            my_wallet.search_history(term)

        elif choice == '5':
            print("Goodbye!")
            break

# This makes the script runnable
if __name__ == "__main__":
    main()