n=True
number=0
choice=""
while n is True:
    choice= input("Would you like to convert to radians or degrees: ")
    
    if choice=="radians":
        number=input("Enter the number of degrees: ")
        try:
            convert=(float(number)*3.1415)/180
        except:
            convert= 0
        print("Calculated "+str(convert)+" radians!")

    elif choice=="degrees":
        number=input("Enter the number of radians: ")
        try:
            convert=(float(number)*180)/3.1415
        except:
            convert=0
        print("Calculated "+str(convert)+" degrees!")

    else:
        print("Please enter 'radians' or 'degrees'.")

    n=input("Do you want another conversion (y/n): ")
    print("")

    if  n=="n":
        n=False
    elif n=="y":
        n=True
