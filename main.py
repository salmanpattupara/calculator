from calculator import addition,subtraction,multiplication,division

options = {
    "addition": addition,
    "subtraction": subtraction,
    "multiplication":multiplication,
    "division":division
    
    
}

print("calculator v1")

a=int(input("input a number"))
b=int(input("enter second number"))



for index,item in enumerate(list(options.keys()),start=1):
    print(f"{index}. {item}")


i=int(input("select an operation: "))
selected=list(options.keys())[i-1]
print(selected)

answer=options[selected]
print(answer(a,b))

