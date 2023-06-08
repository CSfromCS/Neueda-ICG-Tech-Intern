import json

class Person:
   
    def __init__(self, name, age, salary): 
       self.name = name
       self.age = age
       self.salary = salary
   
    def payRise(self, amount) :
        self.salary += amount

    def __str__(self):
        return "%s %d %.2f" % (self.name, self.age, self.salary)
        
   
with open("sampledata.json") as fh:

    for line in fh:
        obj = json.loads(line)
        personObj = Person(obj["name"], obj["age"], obj["salary"])
        personObj.payRise(10000)
        print(personObj)
        