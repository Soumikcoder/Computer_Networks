data_str=input("Enter the data:")
gen_poly_str=input("Enter generator poly:")
data=int('0b'+data_str,base=2)
gen_poly=int('0b'+gen_poly_str,base=2)

def mod2_div (divisor,dividend):
    gen_poly_length=len(bin(dividend)[2:])
    remainder=(divisor<<gen_poly_length-1)
    while len(bin(dividend)[2:]) <= len(bin(remainder)[2:]) :
        remainder_length=len(bin(remainder)[2:])
        temp=dividend<<(remainder_length-gen_poly_length)
        remainder=remainder^temp
    transbit=(divisor<<gen_poly_length-1)+remainder
    return remainder,transbit

#Transmitter
_,transmitted_data=mod2_div(data,gen_poly)
print('CRC codeword',bin(transmitted_data)[2:])

#Noise
err=int(input("Enter some Error:"))

#Receiver
rem,_=mod2_div(transmitted_data+err,gen_poly)

if rem == 0:
    print('Correct message received!')
else:
    print('There is some error!')

# data = "100100"
# key = "1101"