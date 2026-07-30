print("************Trafic signal simulastion system************")

signal=input("enter a signal color:")

if signal=="red":
    print("signal is red")
    print( "action: STOP")
    
elif signal=="yellow":
    print("signal is yellow")
    print("action: GET READY")
    
elif signal=="green":
    print("signal is green") 
    print("action: GO") 
    
else:
    print("invalid color enter red,yellow,green:")         