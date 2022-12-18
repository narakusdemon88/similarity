import re

file1lst = []
file2lst = []

with open("doc1.txt") as file1, open("doc2.txt") as file2:
    for file1_line in file1:
        pattern = re.compile(r'\s+')
        file1_line = re.sub(pattern, "", file1_line)

        file1lst.append(file1_line)

    for file2_line in file2:
        pattern = re.compile(r'\s+')
        file2_line = re.sub(pattern, "", file2_line)

        file2lst.append(file2_line)

for line in file1lst:
    if line in file2lst:
        print(line)
