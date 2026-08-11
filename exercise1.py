mark1=float(input("Enter marks for subject1:"))
mark2=float(input("Enter marks for subject2:"))
mark3=float(input("Enter marks for subject3:"))

total=mark1+mark2+mark3
Average=total/3

print("\n------STUDENTSCORECARD------")
print("subject1:",mark1)
print("subject2:",mark2)
print("subject3:",mark3)
print("total mark:",total)
print("Average:",round(Average,2))