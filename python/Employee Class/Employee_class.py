class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__salary = salary
    def getID(self):
        return int(self.__id)
    def getFirstName(self):
        return str(self.__first_name)
    def getLastName(self):
        return str(self.__last_name)
    def getName(self):
        return str(self.__first_name+" "+self.__last_name)
    def getSalary(self):
        return int(self.__salary)
    def setSalary(self, amt):
        self.__salary=int(amt)
    def getAnnualSalary(self):
        return int(self.__salary*12)
    def raiseSalary(self, percent):
        salary_percent=int(self.getSalary()*(percent/100+1))
        return salary_percent
    def toString(self):
        print("Employee[ID={}, Name={}, Salary={}]".format(self.getID(), self.getName(), self.getSalary()))
