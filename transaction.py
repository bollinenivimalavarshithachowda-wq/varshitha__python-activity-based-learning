1. Question

Develop a Python program to process a list of transaction IDs, identify duplicate transactions, and display the repeated IDs.

2. Algorithm

1. Start.
2. Input the number of transactions.
3. Store the transaction IDs in a list.
4. Create an empty list for duplicate IDs.
5. Check each transaction ID.
6. If an ID occurs more than once, add it to the duplicate list only once.
7. Display the transaction IDs and duplicates.
8. Stop.

3. Flowchart

START
          |
          v
   Input transaction IDs
          |
          v
   Check each transaction
          |
          v
     ID repeated?
       /      \
     Yes       No
      |         |
      v         |
 Add to duplicate list
      \         /
       v       v
   Display duplicates
          |
          v
         STOP

4. Python Code


n = int(input("Enter number of transactions: "))

transactions = []

for i in range(n):
    tid = input("Enter transaction ID: ")
    transactions.append(tid)

duplicates = []

for tid in transactions:
    if transactions.count(tid) > 1:
        if tid not in duplicates:
            duplicates.append(tid)

print("\nAll transactions:", transactions)

if duplicates:
    print("Duplicate transactions:", duplicates)
else:
    print("No duplicate transactions found")

5. Sample Output

Enter number of transactions: 5
Enter transaction ID: T101
Enter transaction ID: T102
Enter transaction ID: T101
Enter transaction ID: T103
Enter transaction ID: T102

All transactions: ['T101', 'T102', 'T101', 'T103', 'T102']
Duplicate transactions: ['T101', 'T102']

Conclusion:
The program identifies repeated transaction IDs using Python lists and conditional statements.
