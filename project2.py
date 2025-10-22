
while True:
                            operand = input("Number 1: ")
                            operand2 = input("Number 2: ")
                            sign = input("Sign")
                            


                            try:
                                operand = float(operand)
                                operand2 = float(operand2)
                                break
                               
                            except:
                                print("Invalid Number")

                                
                                
                                
        


       

 



   



result = None
if sign == "+":
        result = operand + operand2
        print(result)

elif sign == "-":
         result = operand - operand2
         print(result)
elif sign == "*":
     result = operand * operand2
     print(result)
elif sign == "%":
        result = operand % operand2
        print(result)
elif sign == "/":
        if operand2 != 0:
            result = operand / operand2
            print(result)
        else:
            print("Division by zero is not possible")

