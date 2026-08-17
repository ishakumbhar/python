print("---------SCHOLARSHIP ELIGIBLITY CHEAKER---------")

name=input("enter your name:")
age=int(input("enter your age:"))
income=float(input("enter your annual family income ($):"))
caste=input("enter your caste(general /OBC /SC /ST):")

if age <25 and income< 300000:
    print("CONGRATULATIONS")
    print(name,"eligible for the scholarship.")
else:
    print(name,"not eligible for the scholarship.")    