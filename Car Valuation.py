print ("Welcome to the second hand car valuation tool.")

initialValue = int(input("What was the car worth when you bought it? "))

age = int(input("How many years old is the car? "))

for i in range(age):
    initialValue = round(initialValue * 0.90,2)

print ("Your car is now worth £", initialValue)

MOT = input("Does your car have a valid MOT certificate? ").upper()

if MOT == "YES" or MOT == "Y":
    print ("Your car is now worth £", initialValue)
elif MOT == "NO" or MOT == "N":
    initialValue = round(initialValue * 0.75,2)
    print ("Your car is now worth £", initialValue)
else:
    ("That was not a valid answer.")

damage = input("Is there any damage on the car? ").upper()

if damage == "YES" or damage == "Y":
    damageQuantity = int(input("How many instances of damage is there to the car? "))
    initialValue = round(initialValue * 0.95,2) 
    print ("Your car is now worth £", initialValue)
elif damage == "NO" or damage == "N": 
    print ("Your car is now worth £", initialValue)
else:
    ("That was not a valid answer.")

rarity = input("Is your car considered to be rare? ").upper()

if rarity == "YES" or rarity == "Y":
    initialValue = round(initialValue * 1.60,2) 
    print ("Your car is now worth £", initialValue)
elif rarity == "NO" or rarity == "N": 
    print ("Your car is now worth £", initialValue)

mileage = int(input("How many miles your car has done? "))

mileage = int(round(mileage / 10000,0))

for i in range(mileage):
    initialValue = round(initialValue * 0.96,2)

print ("Your car is now worth £", initialValue)
