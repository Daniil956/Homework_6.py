a = int(input("Enter start number: "))
n = int(input("Many iterate: "))
d = int(input("Difference of numbers: "))
i = 1
mass = []

while n >= i:
    j = a + (i-1)*d
    i+=1
    mass.append(j)

print(*mass)

