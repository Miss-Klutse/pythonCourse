def gladys():
  numbers=[]

  while True:
    try:
      # Taking input from the user 
      userInput = input("Enter numbers or (type done) to complete: ")
      if userInput.lower() == 'done':
        break
      num = float(userInput)
      numbers.append(num)
    except ValueError:
      print("Invalid input. Try again!")
    
  total = sum(numbers)
  print(f"The total is {total}")
gladys()      

    