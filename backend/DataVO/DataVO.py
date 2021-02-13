class DataVO :

    def __init__(self,date,consumption,temperature,humidity,windSpeed,weekday,isHoliday) :

        self.date = date
        self.consumption = consumption
        self.temperature = temperature
        self.humidity = humidity
        self.windSpeed = windSpeed
        self.weekday = weekday
        self.isHoliday = isHoliday

    def getDate(self) : 

        return self.date

    def getConsumption(self) : 

        return self.consumption

    def getTemperature(self) : 

        return self.temperature

    def getHumidity(self) : 

        return self.humidity

    def getWindSpeed(self) : 

        return self.windSpeed

    def getWeekday(self) : 

        return self.weekday

    def getIsHoliday(self) : 

        return self.isHoliday
