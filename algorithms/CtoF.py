import math

#create cli to convert cel to fah
# celsius * 9/5 + 32

cel = int(input("\nEnter a Celsius Temp: "))

fah = math.ceil((cel * (9/5) +32))

print(f'the cel for {cel}: fah = {fah}')

