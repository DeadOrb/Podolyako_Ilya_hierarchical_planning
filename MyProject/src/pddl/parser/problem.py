import pddl.parser.myparser as mp


class Problem:
    def __init__(self, file):
        self.name = ''
        self.domain_name = ''
        self.objects = []
        self.init = set()
        self.goal_quantify = ''
        self.goal = set()

        file = mp.take_part(file)
        self.name = mp.take_part(file)
        file = mp.delete_part(file)

        while file.find('(') != -1:
            flag_requirements = mp.take_part(file).split()

            if flag_requirements[0] == ":domain":
                self.domain_name = flag_requirements[1]

            elif flag_requirements[0] == ":objects":
                begin = 0;
                for i in range(0, len(flag_requirements)):
                    if flag_requirements[i] == '-':
                        for j in range(begin + 1, i):
                            self.objects.append((flag_requirements[j], flag_requirements[i + 1]))
                        begin = i + 1

            elif flag_requirements[0] == ":init":
                formal_view = mp.take_part(file)
                while formal_view.find('(') != -1:
                    self.init.add(Predicate(mp.take_part(formal_view)))
                    formal_view = mp.delete_part(formal_view)

            elif flag_requirements[0] == ":goal":
                formal_view = mp.take_part(file)
                if formal_view.find("and ") != -1 or \
                        formal_view.find("or ") != -1 or \
                        formal_view.find("not ") != -1 or \
                        formal_view.find("exists ") != -1 \
                        or formal_view.find("forall ") != -1:
                    formal_view = mp.take_part(formal_view)
                    print(formal_view)
                    self.goal_quantify = (formal_view.split()[0])

                while formal_view.find('(') != -1:
                    self.goal.add(Predicate(mp.take_part(formal_view)))
                    formal_view = mp.delete_part(formal_view)

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
            self.params.append(formal_view[i])

            # if formal_view[i].find('?') != -1:
            #     self.params.append(formal_view[i])
            #
            # if formal_view[i] == '-':
            #     self.params[-1] = (self.params[-1], formal_view[i + 1])