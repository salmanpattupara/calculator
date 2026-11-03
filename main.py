from calculator import addition,subtraction

options = {
    "addition": addition,
    "subtraction": subtraction,
    
}

print("calculator v1")

a=input("input a number")
b=input("enter second number")



for index,item in enumerate(list(options.keys()),start=1):
    print(f"{index}. {item}")


i=int(input("select an operation"))
selected=list(options.keys())[i]
print(selected)
