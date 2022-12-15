a = input()

b = 0
for i in a:
    if (b + int(i)) < 10:
        b += int(i)
    else:
        break

print(b)