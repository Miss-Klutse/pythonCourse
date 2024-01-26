# fruits = {"Perishable", "Non-Perishable"}
# fruit = ['banana', 'orange', 'water melon']

# for i in range(0, 10):
#     print(fruit[:3])

try:
    number = int(input("Enter number: "))
    while True:
        if number.isalnum():
            number = int(input("Try again: "))

except ValueError:
    number = int(input("Try again: "))
    
