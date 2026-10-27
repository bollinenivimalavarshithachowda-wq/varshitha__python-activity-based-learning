1. Question

Compare opening stock, incoming stock, dispatched stock, and recorded closing stock for multiple products. Identify stock discrepancies and calculate the replenishment quantity required.

2. Algorithm

1. Start.
2. Input the number of products.
3. For each product, input opening, incoming, dispatched, and recorded closing quantities.
4. Calculate expected closing stock.
5. Compare expected stock with recorded stock.
6. Identify discrepancies.
7. If stock is below the required minimum, calculate the replenishment quantity.
8. Display the results.
9. Stop.

3. Flowchart

START
         |
         v
    Input products
         |
         v
 Calculate expected stock
         |
         v
 Compare recorded stock
         |
         v
  Stock discrepancy?
      /       \
    Yes        No
     |          |
     v          v
 Display      Display
 difference   correct stock
      \         /
       v       v
 Check minimum stock
         |
         v
 Calculate shortage
         |
         v
   Display results
         |
         v
        STOP

4. Python Code


n = int(input("Enter number of products: "))
minimum = int(input("Enter minimum stock required: "))

for i in range(n):
    print("\nProduct", i + 1)

    opening = int(input("Opening stock: "))
    incoming = int(input("Incoming stock: "))
    dispatched = int(input("Dispatched stock: "))
    closing = int(input("Recorded closing stock: "))

    expected = opening + incoming - dispatched
    shortage = max(0, minimum - expected)

    print("Expected closing stock:", expected)

    if expected == closing:
        print("Stock is correct")
    else:
        print("Stock discrepancy:", expected - closing)

    print("Replenishment required:", shortage)

5. Sample Output

Enter number of products: 2
Enter minimum stock required: 20

Product 1
Opening stock: 50
Incoming stock: 30
Dispatched stock: 40
Recorded closing stock: 40

Expected closing stock: 40
Stock is correct
Replenishment required: 0

Product 2
Opening stock: 25
Incoming stock: 10
Dispatched stock: 20
Recorded closing stock: 10

Expected closing stock: 15
Stock discrepancy: 5
Replenishment required: 5

Conclusion:
The program identifies inventory discrepancies and calculates how much stock must be replenished to reach the specified minimum.
