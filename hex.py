total = 0
index = 0
hex = str(input('Enter a hexadecimal number: '))
length = len(hex)
power = len(hex) - 1

a = 10
b = 11
c = 12
d = 13
e = 14
f = 15

while index < length:
    single = str(hex[index])
   
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
    index += 1
    power -= 1
    
print(hex, "is equal to", total, "in base 10.")
