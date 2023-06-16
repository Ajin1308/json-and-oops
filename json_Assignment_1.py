import json

class Employee:
    def __init__(self, Name, DOB, Height, City, State):
        self.Name = Name
        self.DOB = DOB
        self.Height = Height
        self.City = City
        self.State = State


with open('employee.json',"r") as file:
    data = json.load(file)


employees = []

for item in data:
    employee = Employee(item['Name'], item['DOB'], item['Height'], item['City'], item['State'])
    employees.append(employee)


for employee in employees:
    print(f"Name: {employee.Name}")
    print(f"Height: {employee.Height}")
    print(f"DOB: {employee.DOB}")
    print(f"City: {employee.City}")
    print(f"State: {employee.State}")
    print("------------------------")

