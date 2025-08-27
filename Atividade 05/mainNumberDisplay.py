from NumberDisplay import NumberDisplay
from ClockDisplay import ClockDisplay

def main():
    number = NumberDisplay(24)
    print("Criou NumberDisplay")
    print(number.getDisplayValue())
    print("Incrementa 1 ao NumberDisplay")
    number.increment()
    print(number.getDisplayValue())
    print("Seta 19 ao NumberDisplay")
    number.setValue(19)
    print(number.getValue())




if __name__ == "__main__":
    main()        

