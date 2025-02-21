print("""\n\n=== Exercise 1 ===
Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, 
print out the total, count, and average of the numbers. If the user enters anything other than a 
number, detect their mistake using try and except and print an error message and skip to the next number. 

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333""")

print("""\n=== Answer ===""")


def results():
    global numberList
    return "Total:", sum(numberList), "Count:", len(numberList), "Mean:", sum(numberList) / len(numberList)


numberList = []

while True:
    number = input("Enter a number: ")
    try:
        if number == "done":
            print(results())
            break
        else:
            number = int(number)
            numberList.append(number)
    except:
        print("bad data")
    number = str(number)

print("""\n\n=== Exercise 2 ===
Write another program that prompts for a list of numbers as above and at the end prints out 
both the maximum and minimum of the numbers instead of the average.""")

print("""\n=== Answer ===""")


def results():
    global numberList
    return "Max:", max(numberList), "Min:", min(numberList)


numberList = []

while True:
    number = input("Enter a number: ")
    try:
        if number == "done":
            print(results())
            break
        else:
            number = int(number)
            numberList.append(number)
    except:
        print("bad data")
    number = str(number)
