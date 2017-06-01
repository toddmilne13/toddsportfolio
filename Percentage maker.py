def compute_percentage():
    print("Example...Say you want to know 20% of 100.. Type 100 press enter then 20 then enter :0")
    x = input("Give me the percentage to compute(only the number without %): ")
    number=int(x)
    y = input("Give me what you got in your test: ")
    percentage = int(y)
    result = (number * percentage)/100
    print("{0}% of {1} is: {2}".format(percentage,number,result))
    print("\n")
 
 
def find_percentage():
    print("Example... You did a test and got x out of y")
    first = input("Give me x: ")
    x=int(first)
    second = input("Give me y: ")
    y = int(second)
    result = (x*100)/y
    print("{0}% of {1} represents the {2}%".format(x,y,result))
    print("\n")

    
print("This is a small program that you can use to compute and find the percentage of a number...")
y=2
while(y!=0):
    x = input("Insert 1 to compute a percentage\n"
              "Insert 2 to find the percentage\n"
              "Insert 0 to exit\n")
    choice = int(x)
 
    if (choice==1):
        compute_percentage()
    elif (choice==2):
        find_percentage()
    elif (choice==0):
        print("Bye bye :-)....")
        y=0
    else:
        print("You enter a wrong number...")
        evaluation = input("Insert 0 to exit or what you want to continue")
        y = int(evaluation)
