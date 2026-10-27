1. Question

Develop a Python program to evaluate manufacturing production by checking available raw materials, planned production quantity, defective units, and customer order demand. Identify material shortages and determine whether the order can be fulfilled.

2. Algorithm

1. Start.
2. Input available raw materials.
3. Input material required per product.
4. Input planned production quantity.
5. Input defective units and customer demand.
6. Calculate the total material required.
7. Calculate the material shortage.
8. Calculate good units produced.
9. Compare good units with customer demand.
10. Display production feasibility and quality status.
11. Stop.

3. Flowchart

START
          |
          v
    Input production data
          |
          v
 Calculate material required
          |
          v
  Check material shortage
          |
          v
 Calculate good units
          |
          v
 Good units >= demand?
      /         \
    Yes          No
     |            |
     v            v
 Order can      Order cannot
 be fulfilled   be fulfilled
      \           /
       v         v
    Display report
          |
          v
         STOP

4. Python Code


available = int(input("Enter available raw materials: "))
required = int(input("Enter material needed per product: "))
quantity = int(input("Enter planned production quantity: "))
defects = int(input("Enter defective units: "))
demand = int(input("Enter customer demand: "))

total_required = required * quantity
shortage = max(0, total_required - available)

print("\n--- Production Report ---")
print("Total material required:", total_required)
print("Material shortage:", shortage)

if defects < 0 or defects > quantity:
    print("Invalid defective quantity")

else:
    good_units = quantity - defects

    print("Good units produced:", good_units)

    if shortage == 0:
        print("Material availability: Sufficient")
    else:
        print("Material availability: Insufficient")

    if shortage == 0 and good_units >= demand:
        print("Order status: Can be fulfilled")
    else:
        print("Order status: Cannot be fulfilled")

5. Sample Output

Enter available raw materials: 500
Enter material needed per product: 5
Enter planned production quantity: 80
Enter defective units: 5
Enter customer demand: 70

--- Production Report ---
Total material required: 400
Material shortage: 0
Good units produced: 75
Material availability: Sufficient
Order status: Can be fulfilled

Conclusion:
The program evaluates material availability, calculates production shortages, and determines whether the manufacturing order can be fulfiled.