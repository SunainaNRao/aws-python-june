fname = input("Enter the name of the file:")
file = open(fname, 'r')
lines = 0
words = 0
characters = 0
for line in file:
    wlist = line.split()
    lines = lines + 1
    words = words + len(wlist)
    characters = characters + len(line)
print(lines)
print(words)
print(characters)
