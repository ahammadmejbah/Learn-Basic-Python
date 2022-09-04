""" Deep Neuron AI"""
class employee:
    slno=200

    def __init__(self):
        self.empno = employee.slno
        employee.slno += 1
    
    def store(self):
        self.name=input("name?")
        self.salary=input("salary")
        print("...stored...")
    
    def display(self):
        print("Emp no:%d , Name:%s , Salary:%s"%(self.empno,self.name,self.salary))

s1=employee()
s1.store()
s1.display()