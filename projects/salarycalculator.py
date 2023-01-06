from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    salary: float
    hoursperday: float
    daysforweek: int

    def employee_information(self):
        return f'===============Employee Information===============\n\nName: {self.name}\nWorked hours per day: {self.hoursperday}\nWorked days per week: {self.daysforweek}'
