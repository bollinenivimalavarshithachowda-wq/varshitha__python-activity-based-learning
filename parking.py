 1. Question

Calculate parking charges based on the vehicle category and parking duration. Apply different hourly rates and identify the total fee payable.

2. Algorithm

1. Start.
2. Input the vehicle category and parking duration in hours.
3. Validate the inputs.
4. Select the hourly rate according to the vehicle category.
5. Calculate the parking fee.
6. Display the vehicle category, duration, and fee.
7. Stop.

3. Flowchart

START
         |
         v
  Input vehicle category
  and parking duration
         |
         v
    Validate inputs
         |
         v
   Select hourly rate
         |
         v
 Calculate parking fee
         |
         v
Display total fee
         |
         v
        STOP

Assumption: Cars cost ₹30 per hour, bikes cost ₹15 per hour, and buses cost ₹50 per hour. Any fraction of an hour is charged as a full hour.

vehicle = input("Enter vehicle (car/bike/bus): ").lower()
hours = float(input("Enter parking hours: "))

rates = {
    "car": 30,
    "bike": 15,
    "bus": 50
}

if hours <= 0:
    print("Invalid parking duration")

elif vehicle not in rates:
    print("Invalid vehicle category")

else:
    charged_hours = int(hours)

    if hours > charged_hours:
        charged_hours += 1

    fee = charged_hours * rates[vehicle]

    print("Vehicle:", vehicle)
    print("Charged hours:", charged_hours)
    print("Parking fee: Rs.", fee)

5. Sample Output

Enter vehicle (car/bike/bus): car
Enter parking hours: 2.5

Vehicle: car
Charged hours: 3
Parking fee: Rs. 90

Conclusion: 
The program calculates parking charges according to the vehicle category and parking duration.
