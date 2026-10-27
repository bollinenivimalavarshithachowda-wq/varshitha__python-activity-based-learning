1. Question

Calculate a student's current attendance percentage and determine the minimum number of consecutive classes the student must attend to reach the required attendance percentage.

2. Algorithm

1. Start.
2. Input classes attended, total classes, and required attendance percentage.
3. Calculate current attendance percentage.
4. If attendance is already sufficient, display the result.
5. Otherwise, calculate the minimum additional classes needed, assuming the student attends every upcoming class.
6. Display the result.
7. Stop.

3. Flowchart

START
         |
         v
   Input attendance
         |
         v
 Calculate percentage
         |
         v
 Attendance sufficient?
      /       \
    Yes        No
     |          |
     v          v
 Display     Calculate
 current     extra classes
 attendance      |
      \         /
       v       v
      Display result
            |
            v
           STOP

4. Python Code
attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))
required = float(input("Enter required attendance %: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details")

else:
    percentage = attended / total * 100

    print("Current attendance:", round(percentage, 2), "%")

    if percentage >= required:
        print("Attendance requirement satisfied")

    else:
        extra = 0

        while (attended + extra) / (total + extra) * 100 < required:
            extra += 1

        print("Additional classes required:", extra)
Conclusion: 
The program calculates attendance and determines the minimum additional classes needed to meet the required percentage.