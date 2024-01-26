try:
    phoneNumber = int(input("Enter phone: "))
    print(phoneNumber)

except ValueError:
    print("Hey! You cannot enter a letter! Try again: ")

