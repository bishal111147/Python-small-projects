def myAddition(a,b):
	return a+b
def mySubtraction(a,b):
	return a-b
def myMultiplication(a,b):
	return a*b
def myDivision(a,b):
	return a/b
while 1:
    x=int(input("Enter a number: "))
    y=int(input("Enter a another number: "))
    operator=input("Enter a operator (+,-,*,/): ")
    if operator=="+" or operator=="-" or operator=="*" or operator=="/":
	   if operator=="+":
		   result=myAddition(x,y)
	   elif operator=="-":
		   result=mySubtraction(x,y)
	   elif operator=="*":
		   result=myMultiplication(x,y)
	   elif operator=="/":
		   if y!=0:
		       result=myDivision(x,y)
		   else:
			    print("Division by zero is not possible mathematically!")
			    result=None
    else:
	    print(f"{operator} following operator is not available at this moment!")
	    result=None
	if result is not None:
     print(f"{x} {operator} {y} = {result}")
