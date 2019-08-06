from hwltd.organization import HelloWorld
from workers.structure import Group
from pathlib import Path


def get_num_employees(department, depth):

    switcher = {"engineering": org.structure[0], "hr": org.structure[1], "finance": org.structure[2]}
    depart = switcher.get(department)
    dict = {}
    if depth == 1:
        return {depart.name: str(len(depart.workers))+" workers"}
    if depth == 2:
        dict.update({depart.name: str(len(depart.workers))+" workers"})
        for group in depart.subgroups:
            dict.update({group.name: str(len(group.workers)) + " workers"})
        return dict
    if depth == 3:
        dict.update({depart.name: str(len(depart.workers)) + " workers"})
        for group in depart.subgroups:
            dict.update({group.name: str(len(group.workers)) + " workers"})
            for team in group.subgroups:
                dict.update({team.name: str(len(team.workers)) + " workers"})
        return dict


def get_average_salary(group):
    sumSalary=0
    for w in group.workers:
        sumSalary += int(w.getSalary())
    return sumSalary/len(group.workers)


def get_relational_salary(worker, org):
    t = []
    for dep in org.structure:
        if worker in dep.workers:
            for group in dep.subgroups:
                if worker in group.workers:
                    if not group.subgroups == []:
                        for team in group.subgroups:
                            if worker in team.workers:
                                t = team.workers
                    else:
                        t = group.workers
    dict={}
    dict.keys()
    for teammates in t:
        if teammates is not worker:
            dict.update({teammates.getFirstName(): teammates.getSalary()/worker.getSalary()})
    return dict


if __name__ == "__main__":
    org = HelloWorld("C:/Users/RENT/Desktop/ex1/data.txt")
    w = org.structure[0].subgroups[0].workers[0]
    print(get_relational_salary(w, org))
    print()


