string = input("Enter your sentence ")

s = string.split()[::-1]

l = []

for i in s:
    l.append(i)

print(" ".join(l))