fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
words=list()
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith('From '):
        continue
    words=line.split()
    print(words[1])
    count+=1

print("There were", count, "lines in the file with From as the first word")
