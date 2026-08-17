print("--------placement eligiblity validator--------")
name=input("enter your name:")
score=float(input("enter your graduation score (%):"))
backlogs=int(input("enter number of active academic backlogs:"))

if score>=70 and backlogs==0:
    print("candidate is eligible for placement.")
    
else:
    print("candidate is not eligible for placement.")
        