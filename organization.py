from workers.person import StreetAddress, PobAddress, Phone
from workers.structure import Worker, Engineer, SalesPerson, Group


class Employees:

    def __init__(self, all_emp={}):
        self.employees = all_emp


class HelloWorld():

    def __init__(self, inputfile):

        # defind all the groups:
        Engineering = Group("Engineering", "Engineering Department")
        SW = Group("SW", "SW Grope")
        SW.parent = Engineering
        Infrastructure = Group("Infrastructure", "Infrastructure Team")
        Infrastructure.parent = SW
        APP = Group("APP", "APP Team")
        APP.parent = SW
        Drivers = Group("Drivers", "Drivers Team")
        Drivers.parent = SW
        QA = Group("QA", "QA Team")
        QA.parent = SW
        SW.subgroups = [Infrastructure, APP, Drivers, QA]
        HW = Group("HW", "HW Group")
        HW.parent = Engineering
        Chip = Group("Chip", "Chip Team")
        Chip.parent = HW
        Board = Group("Board", "Board Team")
        Board.parent = HW
        Power = Group("Power", "Power Team")
        Power.parent = HW
        HW.subgroups = [Chip, Board, Power]
        CTO = Group("CTO", "CTO Group")
        CTO.parent = Engineering
        System = Group("System", " System Group")
        System.parent = Engineering
        Design = Group("Design", "Design Team")
        Design.parent = System
        Poc = Group("Poc", "Poc Team")
        Poc.parent = System
        System.subgroups = [Design, Poc]
        Engineering.subgroups = [SW, HW, CTO, System]

        ##########################################################

        HR = Group("HR", "HR Department")
        Recruitment = Group("Recruitment", "Recruitment Group")
        Recruitment.parent = HR
        Tech = Group("Tech", "Tech Team")
        Tech.parent = Recruitment
        Staff = Group("Staff", "Staff Team")
        Staff.parent = Recruitment
        Recruitment.subgroups = [Tech, Staff]
        Culture = Group("Culture", "Culture Team")
        Culture.parent = HR
        HR.subgroups = [Recruitment, Culture]

        ######################################################

        Finance = Group("Finance", "Finance Department")
        Salaries = Group("Salaries", "Salaries group")
        Salaries.parent = Finance
        Budget = Group("Budget", "Budget Group")
        Budget.parent = Finance
        Income = Group("Income", "Income Team")
        Income.parent = Budget
        Outcome = Group("Outcome", "Outcome Team")
        Outcome.parent = Budget
        Budget.subgroups = [Income, Outcome]
        Finance.subgroups = [Salaries, Budget]

        #######################################################

        self.input = inputfile
        self.structure = [Engineering, HR, Finance]
        self.dict_employees = Employees()
        employee = None
        with open(self.input) as file:
            for line in file:
                try:
                    line = line.strip()
                    if not line.startswith("#"):
                        empl_details = line.split(",")
                        lname = empl_details[0].strip()
                        fname = empl_details[1].strip()
                        yob = empl_details[2].strip()
                        email = empl_details[3].strip()
                        phones = empl_details[4].strip().split(";")
                        phoneslist = []

                        for p in phones:
                            newp = Phone(p)
                            phoneslist.append(newp)

                        add = empl_details[5].strip().split(";")
                        if len(add) == 4:
                            address = StreetAddress(add[0], add[1], add[2], add[3])
                        if len(add) == 3:
                            address = PobAddress(add[0], add[1], add[2])
                        team = empl_details[6].strip()
                        role = empl_details[7].strip()
                        data = empl_details[8].strip().split(";")
                        if role == "staff":
                            employee = Worker(fname, lname, email, phoneslist, address, yob, data[0])
                        if role == "engineer":
                            employee = Engineer(fname, lname, email, phoneslist, address, yob,
                                                data[0], data[1] if len(data) > 1 else 0)
                        if role == "sales":
                            employee = SalesPerson(fname, lname, email, phoneslist, address, yob,
                                                   data[0], data[1] if len(data) > 1 else '0',
                                                   data[2:] if len(data) > 2 else ['0'])
                        switcher = {
                            "app": APP, "drivers": Drivers, "qa": QA, "chip": Chip, "board": Board, "power": Power,
                            "cto": CTO, "design": Design, "system": System, "poc": Poc, "tech": Tech, "staff": Staff,
                            "culture": Culture, "salaries": Salaries, "income": Income, "outcome": Outcome,
                        }
                        group = switcher.get(team, "Invalid month")

                        group.workers.append(employee)
                        if group.parent is not None:
                            group.parent.workers.append(employee)
                            if group.parent.parent is not None:
                                group.parent.parent.workers.append(employee)

                        self.dict_employees.employees.update({employee.getEmail(): employee.getFirstName()})

                except Exception as inst:
                    print(inst.args)

