import pddl.parser.domain as dm
import pddl.parser.problem as pb
import pddl.parser.myparser as mp


class Method:
    def __init__(self, action, domain):
        finish = dm.Action('')
        finish.name = "finish"
        start = dm.Action('')
        start.name = "start"
        self.actions = {start : ("start", "finish"), finish: None}
        init = set(action.precondition)
        goal = set(action.effect)
        while len(init) != 0:
            i = init.pop()
            if i in goal:
                init.remove(i)
                goal.remove(i)
            for act in domain.actions:
                for eff in act.effect:
                    if eff.name == i.name and eff.quantify == i.quantify and action.name != act.name and Links(init, eff):
                        res = Cor(self.actions, act)
                        if res == '':
                            self.actions[act] = (act.name, "finish")
                        else:
                            self.actions[act] = (act.name, res)
                        init.discard(i)
                        break
        for i in self.actions:
            print(i.name)
            print(self.actions[i])


def HTN(domain):
    for i in domain.actions:
        if i.name == "destroy_tower":
            domain.methods.append(Method(i, domain))


def Cor(dict, act):
    for i in dict:
        for j in act.effect:
            for k in i.effect:
                if i.name == j.name and i.quantify != j.quantify:
                    return i.name
    return ''


def Links(init, eff):
    for i in init:
        if i.quantify != eff.quantify and i.name == eff.name:
            return False
    return True
