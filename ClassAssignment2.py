class Assignment2():
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
    def OddEven():
        num=int(input("Enter a number:"))
        if (num % 2 == 0):
            print( num, "is Even number")
        else:
             print("The number is odd")
    def MarriageEligable():
        gender=input("Enter the Gender")
        Age=int(input("Enter the age"))
        if (gender == "Male" and Age >=21):
            print("Eligable")
        elif (gender == "Female" and Age >=18):
            print("Eligable")
        else:
            print("Not Eligable")
    def PercentageofMarks():
         S1=int(input("subject1="))
         S2=int(input("subject2="))
         S3=int(input("subject3="))
         S4=int(input("subject4="))
         S5=int(input("subject5="))
         Total=S1+S2+S3+S4+S5
         print("Total :",Total)
         Percentage=Total/5
         print("Percentage:",Percentage)
    def Triangle():
        h=int(input('Height:'))
        b=int(input('Breadth:'))
        area=(h*b)/2
        print('Area of Triangle:',area)
        h1=int(input('Height1:'))
        h2=int(input('Height2:'))
        b1=int(input('Breadth:'))
        perimeter=h1+h2+b1
        print('Perimeter of Traingle:',perimeter)
    