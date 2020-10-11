``
welcomeMsg = "Enter number of rounds"
invalidMsg = "\nInvalid Entry, Try Again\n"
tryagainMsg= "\nTry Again? (yes/no) \n Input:"

def init():
    userInput = input("\nEnter a number of Fib rounds\n:")

    if not userInput.isnumeric():
        print(invalidMsg)
        init()

    userInput = int(userInput)

    result = fib(userInput)

    sequence = ", ".join(map(lambda integer: str(integer), result))

    fibSum = reduce(lambda x,y: x+y, result)

    print(f"\nFibonacci Sequence is... \n\n{sequence}\n Sum of Sequence: {fibSum}")
    tryAgain()

def fib(rounds):

    answer = [0,1]
    counter = 0
    num1 = 0
    num2 = 1

    while(counter < rounds-2):
        counter += 1
        fib = num1 + num2
        num1 = num2
        num2 = fib
        answer.append(fib)
    
    return answer[0:rounds]

def tryAgain():
    ta = input(tryagainMsg)[0].lower()
    if ta == "y":
        init()
    else:
        exit
init()
