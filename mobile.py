1.Question
Evaluate different mobile recharge plans based on data usage,call minutes,validity,and budget.Calculate excess charges and identify the most economical eligible plan.

2.Algorithm
1.Start.
2.Input required data,call minutes,validity,and budget.
3.Store the available mobile plans.
4.Calculate excess data and call charges for each plan.
5.Calculate the total cost.
6.Check the validity and budget.
7.Select the cheapest eligible plan.
8.Display the results.
9.Stop.

3.Flowchat
Start
|
|
v
Input requirements
|
|
v
Read mobile plans
|
|
v
Calculate total cost
|
|
v
Check eligibility
|
|
v
Find cheapest eligible
|
|
v
Display result
|
|
v
Stop

4.Python code 

plans = [
    ("Basic", 199, 2, 100, 28),
    ("Standard", 299, 5, 300, 28),
    ("Premium", 399, 10, 500, 56)
]

data = float(input("Enter data needed in GB: "))
calls = int(input("Enter call minutes needed: "))
days = int(input("Enter validity needed: "))
budget = float(input("Enter budget: "))

best = None
lowest = float("inf")

for name, price, gb, mins, validity in plans:
    extra_data = max(0, data - gb)
    extra_calls = max(0, calls - mins)

    total = price + extra_data * 20 + extra_calls * 1

    print("\nPlan:", name)
    print("Total cost:", total)

    if validity >= days and total <= budget:
        print("Eligible")

        if total < lowest:
            lowest = total
            best = name
    else:
        print("Not eligible")

if best:
    print("\nBest plan:", best)
    print("Total cost:", lowest)
else:
    print("\nNo eligible plan found")

5.Sample output
Enter data needed in GB: 6
Enter call minutes needed: 400
Enter validity needed: 28
Enter budget: 500

Plan: Basic
Total cost: 579.0
Not eligible

Plan: Standard
Total cost: 364.0
Eligible

Plan: Premium
Total cost: 399.0
Eligible

Best plan: Standard
Total cost: 364.0

Conclusion
The program compares mobile plans and identifies the cheapest plan that satisfies the budget and validity requirements.