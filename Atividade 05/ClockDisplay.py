from NumberDisplay import NumberDisplay


class ClockDisplay:
    def __init__(self):
        self.__hours = NumberDisplay(24)
        self.__minutes= NumberDisplay(60)
        self.__seconds= NumberDisplay(60)
        self.__updateDisplay()
    def __updateDisplay(self):
        self.__displayString = self.__hours.getDisplayValue() + ":" + self.__minutes.getDisplayValue()+ ":" + self.__seconds.getDisplayValue()    
    def timeTick(self):
        self.__seconds.increment()
        if(self.__seconds.getValue() == 0):
            self.__minutes.increment()
            if(self.__minutes.getValue() == 0):
                self.__hours.increment()
        self.__updateDisplay()
    def timeMinute(self):
            if(self.__seconds.getValue() == 0):
                self.__minutes.increment()
                if(self.__minutes.getValue() == 0):
                    self.__hours.increment()
            self.__updateDisplay()             
    def getTime(self):
        return self.__displayString 
    def setTime(self,hour,minute,second):
        self.__hours.setValue(hour)
        self.__minutes.setValue(minute)
        self.__seconds.setValue(second)
        self.__updateDisplay()