n = int(input('Enter numbers in list: '))
first_number = int(input('Enter start index number: '))
second_number = int(input('Enter finish index number: '))
i = 1
mass = []

while i <= n:
    mass.append(i)
    i+=2

print(*mass)

for i in range(len(mass)):
    if mass[i] >first_number and mass[i] < second_number:
        print(mass[i], i)




