
#Take students name,index number and reference number
while True:
    try:
        score = float(input("Enter score :"))
        if 0 <= score <=100 :
            break
        else: print ("Enter score between 0 and 100. Please try again")      
   
    except ValueError:
        print("Enter a numeric value")
if score >= 70:
    print("A")
elif score >=60 :
    print ("B")
elif score >=50 :
    print ("C")
elif score >=40 :
    print ("D")  
else:
 print ("F")          
