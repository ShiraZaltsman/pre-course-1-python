from workers.person import Person


class Group:

    def __init__(self, name, desc, parentgrop=None):
        self.name = name
        self.description = desc
        self.parent = parentgrop
        self.subgroups = []
        self.workers = []

    def getworkers(self):
        for w in self.workers:
            yield w
        return self.workers #todo should return list with all workers in subgrop generat exprssion

    def getparen(self):
        p = self.parent
        while not p is None:
            yield self.parent.name
            p = p.parent

        return self.parent #todo should return list with all parent

    def setparent(self, par):
        self.parent = par

    def addworker(self, wor):
        self.workers.append(wor)


class Worker(Person):
    def __init__(self, fName, lName, email, phones, address, YoB, salary):
        super().__init__(fName, lName, email, phones, address, YoB)
        self.salary=int(salary)

    def getSalary(self):
        return self.salary


class Engineer(Worker):
    def __init__(self, fName, lName, email, phones, address, YoB, salary, bonus):
        super().__init__(fName, lName, email, phones, address, salary,  YoB)
        self.bonus = int(bonus)

    def getSalary(self):
        return super().getSalary() + self.bonus


class SalesPerson(Worker):
    def __init__(self, fName, lName, email, phones, address, YoB, salary, commission, deals):
        super().__init__(fName, lName, email, phones, address, salary,  YoB)
        self.commission = float(commission)
        self.deals = list(map(int, deals))

    def getSalary(self):
        return super().getSalary() + sum(self.deals)*self.commission



