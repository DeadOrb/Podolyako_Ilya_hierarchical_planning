import pddl.parser.myparser as mp


class Domain:
    def __init__(self, file):
        self.name = ''
        self.requirements = []
        self.types = []
#        self.constants = [] not today
        self.predicates = []
        self.actions = []

        file = mp.take_part(file)
        file = file[file.find('('):]
        for_name = mp.take_part(file).split()
        name = ''
        for i in range(1, len(for_name)):
            name += for_name[i]
        self.name = name
        file = mp.delete_part(file)

        while file.find('(') != -1:
            flag_requirements = mp.take_part(file).split()

            if flag_requirements[0] == ":requirements":
                self.requirements = flag_requirements[1:]

            elif flag_requirements[0] == ":types":
                self.types = flag_requirements[1:]

            elif flag_requirements[0] == ":constants":
                self.constants = flag_requirements[1:]

            elif flag_requirements[0] == ":predicates":
                def_predicates = mp.take_part(file)
                while def_predicates.find('(') != -1:
                    self.predicates.append(Predicate(mp.take_part(def_predicates)))
                    def_predicates = mp.delete_part(def_predicates)

            elif flag_requirements[0] == ":action":
                def_action = mp.take_part(file)
                self.actions.append(Action(def_action))

            file = mp.delete_part(file)


class Predicate:
    def __init__(self, data):
        self.name = ''
        self.quantify = ''
        self.params = []

        if data.find("and ") != -1 or \
                data.find("or ") != -1 or \
                data.find("not ") != -1 or \
                data.find("exists ") != -1 \
                or data.find("forall ") != -1:

            self.quantify = data.split()[0]
            data = mp.take_part(data)


        formal_view = data.split()
        self.name = formal_view[0]
        for i in range(1, len(formal_view)):

            if formal_view[i].find('?') != -1:
                self.params.append(formal_view[i])

            if formal_view[i] == '-':
                self.params[-1] = (self.params[-1], formal_view[i + 1])



class Action:
    def __init__(self, data):
        self.name = ''
        self.parameters = []
        self.quantifier_for_pre = ''
        self.precondition = []
        self.quantifier_for_eff = ''
        self.effect = []

        if data.find(":action") != -1:
                if data[data.find(':') + 1:].find(':') != -1:
                    end_of_part = data[data.find(':') + 1:].find(':')
                    self.name = data[:end_of_part].split()[1]
                    data = data[end_of_part:]
                else:
                    self.name = data.split()[1]
                    data = ''

        if data.find(":parameters") != -1:
                begin_of_part = data.find(":parameters")
                if data[begin_of_part + 1:].find(':') != -1:
                    end_of_part = data[begin_of_part + 1:].find(':')
                    formal_view = mp.take_part(data[begin_of_part: end_of_part]).split()
                    for i in range(0, len(formal_view)):

                        if formal_view[i].find('?') != -1:
                            self.parameters.append(formal_view[i])

                        if formal_view[i] == '-':
                            self.parameters[-1] = (self.parameters[-1], formal_view[i + 1])
                    data = data[end_of_part:]

                else:
                    formal_view = mp.take_part(data[begin_of_part:]).split()
                    for i in range(1, len(formal_view)):

                        if formal_view[i].find('?') != -1:
                            self.parameters.append(formal_view[i])

                        if formal_view[i] == '-':
                            self.parameters[-1] = (self.parameters[-1], formal_view[i + 1])
                        data = ''

        if data.find(":precondition") != -1:
                begin_of_part = data.find(":precondition")
                if data[begin_of_part + 1:].find(':') != -1:
                    end_of_part = data[begin_of_part + 1:].find(':')
                    formal_view = data[begin_of_part + 1:end_of_part]

                    if formal_view.find("and ") != -1 or \
                            formal_view.find("or ") != -1 or \
                            formal_view.find("not ") != -1 or \
                            formal_view.find("exists ") != -1 \
                            or formal_view.find("forall ") != -1:
                        formal_view = mp.take_part(formal_view)
                        self.quantifier_for_pre = (formal_view.split()[0])

                    while formal_view.find('(') != -1:
                        pre = mp.take_part(formal_view)
                        self.precondition.append(Predicate(pre))
                        formal_view = mp.delete_part(formal_view)
                    data = data[end_of_part:]

                else:
                    formal_view = data[begin_of_part + 1:]

                    if formal_view.find("and ") != -1 or \
                            formal_view.find("or ") != -1 or \
                            formal_view.find("not ") != -1 or \
                            formal_view.find("exists ") != -1 \
                            or formal_view.find("forall ") != -1:
                        formal_view = mp.take_part(formal_view)
                        self.quantifier_for_pre = (formal_view.split()[0])

                    while formal_view.find('(') != -1:
                        pre = mp.take_part(formal_view)
                        self.precondition.append(Predicate(pre))
                        formal_view = mp.delete_part(formal_view)
                    data = ''




                    print(formal_view)

        if data.find(":effect"):
                formal_view = data[data.find(":effect"):]
                if formal_view.find("and ") != -1 or \
                        formal_view.find("or ") != -1 or \
                        formal_view.find("not ") != -1 or \
                        formal_view.find("exists ") != -1 \
                        or formal_view.find("forall ") != -1:
                    formal_view = mp.take_part(formal_view)
                    self.quantifier_for_eff = (formal_view.split()[0])
                while formal_view.find('(') != -1:
                    pre = mp.take_part(formal_view)
                    self.effect.append(Predicate(pre))
                    formal_view = mp.delete_part(formal_view)
                data = ''

        data = ''
