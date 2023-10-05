
def sum(first, second):
    print('The summation is: ',first+second)
sum(4,5)


def subtraction(first, second):
    subtract= first- second
    return subtract
result= subtraction(5,3)
print('The subtraction is : ', result)


def multiplication(first, second, third, fourth):
    multiply= first*second*third*fourth
    print('print this multyply: ',multiply)
    return multiply
result=multiplication(2,3,5,2)
print('The multiplication is : ',result)

def division(first, second):
    divide =first/second
    modulus =first%second
    if(modulus!=0):
        print('The modulus is: ',modulus)
    return divide
result= division(9,4)
print('The division is : ',int(result))