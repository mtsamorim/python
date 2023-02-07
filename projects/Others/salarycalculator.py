from dataclasses import dataclass

weeks = 52
months = 12


@dataclass
class Employee:
    name: str
    salary: float
    hoursperday: float
    daysforweek: float

    def employee_information(self):
        return print(f'\n===============Employee Information===============\n\nName: {self.name}\nWorked hours per day: {self.hoursperday:.0f}\nWorked days per week: {self.daysforweek:.0f}')

    def salary_for_hour(self):
        return self.salary/((self.hoursperday*self.daysforweek)*weeks)

    def salary_for_day(self):
        return self.salary_for_hour()*self.hoursperday

    def salary_for_week(self):
        return self.salary/weeks

    def salary_for_month(self):
        return self.salary/months

    def salary_information(self):
        return print(f'\n================Salary Information================\n\nSalary per hour: R${self.salary_for_hour():.2f}\nDiary Salary: R${self.salary_for_day():.2f}\nWeek Salary: R${self.salary_for_week():.2f}\nMonth Salary: R${self.salary_for_month():.2f}\nTotal Gross Salary: R${self.salary}\n\n==================================================\n')


name = str(input("\nWhat is your name? : "))

hours = float(input("How many hours do you work a day? : "))

days = float(input("How many days do you work per week? : "))

salary = float(input("What is your Annual Salary? : "))

employee = Employee(name, salary, hours, days)

employee.employee_information()

employee.salary_information()
