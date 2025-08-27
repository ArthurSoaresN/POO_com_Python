from NumberDisplay import NumberDisplay
from ClockDisplay import ClockDisplay

def main():
    print("")
    display = ClockDisplay()
    testeMinuto = ClockDisplay()
    print("Testando minuto")

    print(testeMinuto.getTime())
    cont = 0
    while cont <= 60:
        print(testeMinuto.getTime())
        testeMinuto.timeMinute()
        cont +=1


    print("Criou ClockDisplay")
    print(display.getTime())
    display.setTime(00,59,59)
    print("Setou 00 e 59 e 59 para o display")    
    print(display.getTime())
    display.timeTick()
    print("Um timeTick")
    print(display.getTime())
    
    




if __name__ == "__main__":
    main()        

