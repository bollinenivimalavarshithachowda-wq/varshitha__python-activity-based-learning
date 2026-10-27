1. Question

Develop a Python program to accept a paragraph, convert it to lowercase, count word occurrences, and identify repeated words.

2. Algorithm

1. Start.
2. Input a paragraph.
3. Convert the paragraph to lowercase.
4. Split the paragraph into individual words.
5. Check the frequency of each word.
6. Identify words appearing more than once.
7. Display the repeated words and their counts.
8. Stop.

3. Flowchart

START
          |
          v
   Input a paragraph
          |
          v
 Convert to lowercase
          |
          v
   Split into words
          |
          v
  Count word frequency
          |
          v
   Frequency > 1?
      /        \
    Yes         No
     |           |
     v           |
 Display repeated words
      \          /
       v        v
         STOP

4. Python Code


text = input("Enter a paragraph: ")

text = text.lower()
words = text.split()

print("\nRepeated words:")

found = False

for word in words:
    count = words.count(word)

    if count > 1:
        if words.index(word) == words.index(word):
            first = True

            for previous in words[:words.index(word)]:
                if previous == word:
                    first = False

            if first:
                print(word, ":", count, "times")
                found = True

if not found:
    print("No repeated words")

5. Sample Output

Enter a paragraph: Python is easy and Python is useful

Repeated words:
python : 2 times
is : 2 times

Conclusion: 
The program processes text and identifies repeated words using string and list operations.
