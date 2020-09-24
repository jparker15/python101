
def factorial ():

    demo=int(input("enter a number:\n"))
    num=1
    count=1
    while count < demo:
        count += 1
        num *= count
        # print(num)
    return print(f"factorial:{num}")
factorial()