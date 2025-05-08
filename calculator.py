print(" Select The Operation\n"\
      "1. Add\n"
"2. Subtration\n" \
"3. Multiply \n" \
"4. Divide\n")
sel =int(input("Select The Operation(1-4): "))
num1 =int(input("Enter The First Number:"))
num2 =int(input("Enter The Second Nnumber:"))
if sel == 1:
    print("The Sum Of ",num1 ,"And", num2 , "=", num1+num2)
elif sel == 2:
    print("The subtration of ", num1,"And",num2 ,"=", num1-num2)
elif sel == 3:
    print("The Multiplication of ", num1,"And",num2 ,"=", num1*num2)
elif sel == 4:
    print("The Divide of ", num1,"And",num2 ,"=", num1/num2)
else:
    print("you have selected the invalid operation \n" \
    "please try again!!!")
   
