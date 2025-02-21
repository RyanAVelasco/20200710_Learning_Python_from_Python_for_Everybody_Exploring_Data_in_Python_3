import string

print("""


Exercise 1: Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the number of 
messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
""")

print("""
=== Answer ===
""")

d = dict()

fname = open("mbox-short.txt")
for lines in fname:
    if lines.startswith("From"):
        lines = lines.split()
        for addr in lines:
            if "@" not in addr:
                continue
            elif addr not in d:
                d[addr] = 1
            else:
                d[addr] += 1

ol = list()
for (count, emails) in d.items():
    ol.append((emails, count))

ol.sort(reverse=True)

xl = list()

for (count, emails) in ol:
    xl.append((emails, count))

for (x, y) in xl:
    print(x, y)




print("""


Exercise 2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.
python timeofday.py

Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
""")

print("""
=== Answer ===
I ended up getting 'om' (from 'From') in the answer and haven't 
figured out a way to prevent that from happening.. will come 
back to this later on.
""")

fname = open("mbox-short.txt")
hours = {}
for lines in fname:
    if lines.startswith("From"):
        pos = lines.find(":")
        atpos = [pos - 2]
        npos = [pos]
        x = lines[pos - 2:pos]
        if x not in hours:
            hours[x] = 1
        else:
            hours[x] += 1

lst = list(hours.keys())
lst.sort()
for hour in lst:
    print(hour, hours[hour])


print("""


Exercise 3: Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.
""")

print("""
=== Answer ===
""")

fname = open("history_of_mathematics.txt")
letters = dict()
for lines in fname:
    lines = lines.lower()\
        .rstrip()\
        .replace("â€”", "-")\
        .translate(lines.maketrans("", "", string.punctuation))
    for letter in lines:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1

temp = list()
for (letter, count) in letters.items():
    temp.append((letter, count))
temp.sort()

print(temp)