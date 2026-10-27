1. Question

Develop a Python program that simulates ATM deposits and withdrawals, maintains the account balance, rejects invalid transactions, and displays the final balance.

2. Algorithm

1. Start.
2. Input the initial balance.
3. Input the number of transactions.
4. For each transaction, select deposit or withdrawal.
5. Check whether the transaction amount is valid.
6. Add deposits to the balance.
7. Allow withdrawals only when sufficient funds are available.
8. Display the final balance.
9. Stop.

3. Flowchart

START
         |
         v
put initial balance
         |
         v
   Input transactions
         |
         v
   Deposit or withdraw?
      /          \
  Deposit      Withdraw
     |              |
     v              v
 Add amount     Check balance
     |              |
     |         Sufficient funds?
     |           /       \
     |         Yes        No
     |          |          |
     |          v          v
     |       Deduct     Reject
     |          |          |
     └──────────┴──────────┘
                |
                v
         More transactions?
                |
                v
         Display balance
                |
                v
               STOP

4. Python Code


balance = float(input("Enter initial balance: "))
n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")

    elif choice == 1:
        balance += amount
        put initial balance
         |
         v
   Input transactions
         |
         v
   Deposit or withdraw?
      /          \
  Deposit      Withdraw
     |              |
     v              v
 Add amount     Check balance
     |              |
     |         Sufficient funds?
     |           /       \
     |         Yes        No
     |          |          |
     |          v          v
     |       Deduct     Reject
     |          |          |
     └──────────┴──────────┘
                |
                v
         More transactions?
                |
                v
         Display balance
                |
                v
               STOP

4. Python Code

Save as atm.py.

balance = float(input("Enter initial balance: "))
n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")

    elif choice == 1:
        balance += amount
        print("Deposit successful")

    elif choice == 2:
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    else:
        print("Invalid choice")

print("\nFinal balance:", balance)

5. Sample Output

Enter initial balance: 1000
Enter number of transactions: 3

1. Deposit
2. Withdraw
Enter choice: 1
Enter amount: 500
Deposit successful

1. Deposit
2. Withdraw
Enter choice: 2
Enter amount: 200
Withdrawal successful

1. Deposit
2. Withdraw
Enter choice: 2
Enter amount: 2000
Insufficient balance

Final balance: 1300.0

Conclusion:
The program simulates basic ATM transactions and prevents withdrawals that exceed the available balance.