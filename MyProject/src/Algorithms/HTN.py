import pddl.parser.domain as dm
import pddl.parser.problem as pb

class Metod:
    def __init__(self, action, domain, task):
        self.actions = []
        precondition = set(action.precondition)
        for subgoal in precondition:
            for act in domain.actions:
                for eff in act.effect:
                    if eff.name == subgoal.name and eff.quantify == subgoal.quantify and action.name != act.name\
                            and not eff in task.init:
                        self.actions.append(act)
        for i in self.actions:
            print(i.name)
        print("Я тут был")







def HTN(domain, task):
    for i in domain.actions:
        if i.name == "destroy_tower":
            domain.methods.append(Metod(i, domain, task))
