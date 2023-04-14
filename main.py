def countf():
  print("Enter your count of Number")
  count=input()
  count=int(count)
  if count==(2):
    cal()
  else:
    print("Bye")

def cal():
  print("Enter your first number")
  x=input()
  print("Enter your Oparetor")
  y=input()
  print("Enter your second number")
  z=input()
  x=int(x)
  y=str(y)
  z=int(z)
  if   y == ("+"):
    print(x+z)
  elif y==("-"):
    print(x-z)
  elif y==("/"):
    print(x/z)
  elif y==("*"):
    print(x*z)
  else:
    print ("please enter valude key")
  print("Are your calculation over?(Yes or No)")
  ans=input()
  if ans==("Yes"):
   print("Thank You")
  elif ans==("yes"):
    print("Thank you")
  else:
    countf()



print("Enter your count of Number")
count=input()
count=int(count)
if count==(2):
  cal()
else:
  print("Bye")
