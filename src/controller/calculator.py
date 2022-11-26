class Calculator():
    '''Calculator with bitwise operators'''
    def add(self, num1, num2):
        ''' Returns sum of two integers  '''
        while (num2 != 0):
            carry = num1 & num2
            num1 = num1 ^ num2
            num2 = carry << 1
        
        return num1

    def subtract(self, num1, num2):
        ''' Return subtraction of two integers '''
        while (num2 != 0):
            borrow = (~num1) & num2
            num1 = num1 ^ num2
            num2 = borrow << 1
        
        return num1

    def multiplication(self, num1, num2):
        ''' Returns multiplication of two numbers '''
        res = 0
 
        while (num2 > 0):
            if (num2 & 1):
                res = res + num1
    
            num1 = num1 << 1
            num2 = num2 >> 1
        
        return res

    def division(self, num1, num2):
        ''' Returns division of two numbers '''
        sign = -1 if ((num1 < 0) ^ (num2 < 0)) else 1
    
        num1 = abs(num1)
        num2 = abs(num2)
    
        quotient = 0
        while (num1 >= num2):
            num1 -= num2
            quotient += 1
    
    
        if sign == -1:
            quotient = -quotient
        return quotient
    
