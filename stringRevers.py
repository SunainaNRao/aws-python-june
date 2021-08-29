# input → ‘This is a sample program’
# Output → ‘program sample a is This’

# input="this is a sample program"
# >>> s=input.split()
# >>> print(" ".join(s[::-1]))
# O/P:
# program sample a is this

input = "This is a Sample program"
s = input.split()
print(''.join(s[::-1]))