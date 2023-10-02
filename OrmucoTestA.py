# Question A
# Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) 
# on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps 
# but not (1,5) and (6,8).


# This function is used to determine if the user used the correct format to input the lines
def checkInput(userinput):
    try:
        userinput = userinput.strip("()")
        if userinput == line1:
            x1,x2 = map(float, userinput.split(','))
            if(x1>x2):                                      # I assumed the first number (x1) had to be smaller than the second number (x2) 
                print("x1 must be less than x2")
                return None, None
                return False
            return x1, x2
        else:
            x3,x4 = map(float, userinput.split(','))      
            if(x3>x4):                                      # I assumed the first number (x3) had to be smaller than the second number (x4) 
                print("x3 must be less than x4")
                return None, None
                return False     
            return x3, x4 
        return True

    except ValueError:
        print("Invalid input. Please use the format (x1,x2)")
        return False


line1 = input("Please input a line1 in the form (x1,x2): ") # Get the first line from the user
while(not checkInput(line1)):
    line1 = input("Please input a line1 in the form (x1,x2): ")
x1,x2 = checkInput(line1)


line2 = input("Please input a line2 in the form (x3,x4): ") # Get the second line from the user
while(not checkInput(line2)):
    line2 = input("Please input a line2 in the form (x3,x4): ")
x3,x4 = checkInput(line2)


if(x2>x3):                                      #if x2 is greater than x3 than the lines overlap (this works because of the assumption that x1<x2 and x3<x4)
    print("The two lines overlap")
else:
    print("The two lines do not overlap")






