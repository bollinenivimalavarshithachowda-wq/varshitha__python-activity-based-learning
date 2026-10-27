1. Question

Develop a Python program to compare a student's marks across multiple examinations, calculate improvements or declines, identify weak subjects, and calculate the average marks.

2. Algorithm

1. Start.
2. Input the number of subjects.
3. Input the subject names and marks from two examinations.
4. Calculate the average marks for both examinations.
5. Compare the marks in each subject.
6. Identify improvements, declines, and weak subjects.
7. Display the results.
8. Stop.

3. Flowchart

START
          |
          v
   Input subject marks
          |
          v
  Calculate averages
          |
          v
 Compare subject marks
          |
          v
  Marks increased?
      /        \
    Yes         No
     |           |
     v           v
 Improvement   Decline
      \          /
       v        v
 Identify weak subjects
          |
          v
    Display results
          |
          v
         STOP

4. Python Code


n = int(input("Enter number of subjects: "))

subjects = []
exam1 = []
exam2 = []

for i in range(n):
    name = input("Enter subject name: ")
    m1 = float(input("Enter first exam marks: "))
    m2 = float(input("Enter second exam marks: "))

    subjects.append(name)
    exam1.append(m1)
    exam2.append(m2)

print("\n--- Performance Report ---")

for i in range(n):
    difference = exam2[i] - exam1[i]

    print("\nSubject:", subjects[i])
    print("First exam:", exam1[i])
    print("Second exam:", exam2[i])

    if difference > 0:
        print("Improved by:", difference)
    elif difference < 0:
        print("Declined by:", abs(difference))
    else:
        print("No change")

    if exam2[i] < 40:
        print("Weak subject")

avg1 = sum(exam1) / n
avg2 = sum(exam2) / n

print("\nFirst exam average:", round(avg1, 2))
print("Second exam average:", round(avg2, 2))

5. Sample Output

Enter number of subjects: 3
Enter subject name: Python
Enter first exam marks: 60
Enter second exam marks: 75
Enter subject name: Maths
Enter first exam marks: 80
Enter second exam marks: 70
Enter subject name: English
Enter first exam marks: 35
Enter second exam marks: 38

--- Performance Report ---

Subject: Python
First exam: 60.0
Second exam: 75.0
Improved by: 15.0

Subject: Maths
First exam: 80.0
Second exam: 70.0
Declined by: 10.0

Subject: English
First exam: 35.0
Second exam: 38.0
Improved by: 3.0
Weak subject

First exam average: 58.33
Second exam average: 61.0

Conclusion:
The program compares examination results, identifies weak subjects, and measures the student's overall performance.
