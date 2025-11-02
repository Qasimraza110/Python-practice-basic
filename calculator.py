print (" QASIM SHEIKH !!)")
print("            ***** HELLO GUYS *****\n        Welcome To Programming World")
print("Now you can easily perform some basic calculation through this calculator....\n")
while True:
 print("          ***** SELECT THE OPERATOR *****   ")
 print("Press 1----Addition(+)\nPress 2----Subtraction(-)\nPress 3----Multipliication(*)")
 print("Press 4----Division(/)\nPress 5----Square Root\nPress 6----Mode")
 print("Press 7----Developer of caculator\nPress 8----Exit\n")
 print("        you an also select option and operation         ")
 choice = input("Select the operator : ")

 if choice in ('1','2','3','4','+','-','*','/'):
  a = float(input("Enter a number : "))
  b= float(input("Enter a number :  "))

 def sum(a,b):
     return a+b
 def sub(a,b):
     return a-b
 def mul(a,b):
     return a*b
 def division(a,b):
     try:
        return  a/b
     except Exception as e:
        print(e)
        return "Error: Division by zero"
         
 
 if choice=='1' or choice=='+':
      c=sum(a,b)
      print(f"sum={c}")
 elif choice=='2'or choice=='-':
      d=sub(a,b)
      print(f"subtraction={d}")
 elif choice=='3'or choice=='*': 
      e=mul(a,b)
      print(f"multiplication={e}")
 elif choice=='4'or choice=='/':
      div=division(a,b)
      print(f"Division : {div}")
 elif choice=='5':
      c=float(input("enter a number : "))
      print(f"Square root ={c*c}")
 elif choice=='6':
     d=int(input("Enter a Number : "))
     print(f"Mode ={d/2}")
 elif choice =='7':
     print("****** DEVELOPER IS SHEIKH QASIM RAZA ******")
 elif choice =='8':
     print("Exit, calculator is OFF")
     break
 else:
     print("ENTER VALID OPTION, THANKS.....")
 
 if choice != '7' or choice=='7':
        again = input("Do you want to perform another operation? (yes/no): ")
        if  again== 'yes':
            continue
        else:
            break