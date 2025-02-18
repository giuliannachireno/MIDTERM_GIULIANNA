import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))


EVENNUMBER = [] #first just do a list of the even numbers of the random number selected
for num in random_numbers:
    if num % 2 == 0: #if the remainder of a division is 0 then it means that the number is even so that is what is being done here
        EVENNUMBER.append(num)
for i in range(len(EVENNUMBER)):
    EVENNUMBER[i] = EVENNUMBER[i] * 2 #the next step is to replace said even numbers with the double of its value AKA multiply times 2

print("OG list:", random_numbers)
print("OG list * 2 (only even removed):", EVENNUMBER)