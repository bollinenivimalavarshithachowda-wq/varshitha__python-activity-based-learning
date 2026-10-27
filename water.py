1. Question

Develop a Python program to calculate a household's water bill using progressive consumption slabs and a fixed charge.

2. Algorithm

1. Start.
2. Input the water consumption in units.
3. Calculate the charges using progressive slabs.
4. Add the fixed charge.
5. Display the total bill.
6. Stop.

3. Flowchart

START
         |
         v
 Input water consumption
         |
         v
 Calculate slab charges
         |
         v
 Add fixed charge
         |
         v
 Display total bill
         |
         v
        STOP

4. Python Code


Assumptions:

- First 30 units: ₹2 per unit.
- Next 20 units: ₹3 per unit.
- Units above 50: ₹5 per unit.
- Fixed charge: ₹50.

units = float(input("Enter water consumption in units: "))

if units < 0:
    print("Invalid consumption")

else:
    if units <= 30:
        bill = units * 2

    elif units <= 50:
        bill = 30 * 2 + (units - 30) * 3

    else:
        bill = 30 * 2 + 20 * 3 + (units - 50) * 5

    bill += 50

    print("Water consumption:", units)
    print("Total water bill: Rs.", bill)

5. Sample Output

Enter water consumption in units: 60
Water consumption: 60.0
Total water bill: Rs. 280.0

Calculation:

- First 30 units: 30 × ₹2 = ₹60
- Next 20 units: 20 × ₹3 = ₹60
- Remaining 10 units: 10 × ₹5 = ₹50
- Fixed charge: ₹50

Total bill = ₹60 + ₹60 + ₹50 + ₹50 = ₹220.

Correction to the sample output: The correct output is:

Enter water consumption in units: 60
Water consumption: 60.0
Total water bill: Rs. 220.0

Conclusion:
 The program calculates the water bill using progressive tariff rates and a fixed charge.