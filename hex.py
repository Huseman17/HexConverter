a = 10
b = 11
c = 12
d = 13
e = 14
f = 15

def hexToDec(num):
    total = 0
    index = 0
    length = len(num)
    power = len(num) - 1
    
    while index < length:
        single = str(num[index])
       
        if ((((single == '0' or single == '1') or single == '2') or single == '3') or single == '4'):           #Checks to see if digit is numeral. 
            total += int(single) * (16 ** power)
        elif ((((single == '5' or single == '6') or single == '7') or single == '8') or single == '9'):         #Split into two statements for readability.
            total += int(single) * (16 ** power)
        elif single == 'a':
            total += a * (16 ** power)
        elif single == 'b':
            total += b * (16 ** power)
        elif single == 'c':
            total += c * (16 ** power)
        elif single == 'd':
            total += d * (16 ** power)
        elif single == 'e':
            total += e * (16 ** power)
        elif single == 'f':
            total += f * (16 ** power)
        else:
            total = -1
            break
        
        index += 1 
        power -= 1
        
    if total == -1:
        print('Error: Non-hexadecimal digit entered.')
    else:
        print(num, "is equal to", total, "in base 10.")

def decToHex(num):
    # PROCESS FOR CONVERTING DEC TO HEX
    #
    # http://www.permadi.com/tutorial/numDecToHex/   
    originalNum = num 
    if num == 0:
        print('0')    
    finalResult = str('')
    
    while num != 0:
              
        result = num // 16
        remainder = num % 16
        hexRemainder = str('')
        
        if remainder == a:
            hexRemainder = 'A'
        elif remainder == b:
            hexRemainder = 'B'
        elif remainder == c:
            hexRemainder = 'C'
        elif remainder == d:
            hexRemainder = 'D'
        elif remainder == e:
            hexRemainder = 'E'
        elif remainder == f:
            hexRemainder = 'F'
        elif remainder == 0:
            hexRemainder = '0'
        elif remainder == 1:
            hexRemainder = '1'  
        elif remainder == 2:
            hexRemainder = '2'  
        elif remainder == 3:
            hexRemainder = '3'  
        elif remainder == 4:
            hexRemainder = '4'  
        elif remainder == 5:
            hexRemainder = '5'  
        elif remainder == 6:
            hexRemainder = '6'  
        elif remainder == 7:
            hexRemainder = '7'  
        elif remainder == 8:
            hexRemainder = '8'  
        elif remainder == 9:
            hexRemainder = '9'                     
        else:
            hexRemainder = '-1'
            break
        
        #print(result)
        #print(remainder)
        #print(finalResult)        
        
        finalResult = hexRemainder + finalResult
        remainder = int(remainder)
        num = result
    if hexRemainder == '-1':
        print('Error: Non-base 10 digit entered.')
    else:
        print(originalNum, "is equal to", finalResult, "in hexadecimal.")    
        
def main():
    #option = str(input('Enter "D2H" for decimal to hexadecimal, or "H2D" for hexadecimal to decimal: '))
    option = 'h2d'
    if (((option == 'D2H' or option == 'd2h') or option == 'D2h') or option == 'd2H'):
        num = int(input('Enter a base 10 number: '))        
        total = decToHex(num)
    elif (((option == 'H2D' or option == 'h2d') or option == 'H2d') or option == 'h2D'):
        num = str(input('Enter a hexadecimal number: '))        
        total = hexToDec(num)
    else:
        print('Invalid input.\n')
        main()
        
main()