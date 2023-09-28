
def calculator():
    print("-------------PLEASE ENTER THE VALUES------------")
    while True:

        A=int(input("Enter the value of A: "))
        B=int(input("Enter the value of B: "))


        print("-------------Select the operator to perform operation---------")
        operator=int(input("Press 1 for ADDITION \nPress 2 for SUBTRACTION \nPress 3 for MULTIPLICATION \nPress 4 for DIVISION \nPress 5 for quit \n"))
        if operator ==1:
            result=float(A + B)
            print("ADDITION OF A AND B : ",result)

        elif operator==2:
            result= float(A - B)
            print("SUBTRACTION OF A AND B : ",result)

        elif operator==3:
            result= float(A * B)
            print("MULTIPLICATION OF A AND B : ",result)

        elif operator==4:
            result=float( A / B)
            print("DIVISION OF A AND B : ",result)

        elif operator==5:
            print("------------Thank you for using calculator------------")
            return 0

        else:
            print("ERROR")


calculator()