import pddl.parser.myparser as mp
import logging




class Domain:
    def __init__(self, file):
        self.name = ''
        self.requirements = []
        self.types = []
        self.predicates = []
        self.actions = []

        file = mp.take_part(file)
        file = file[file.find('('):]
        self.name = mp.take_part(file)
        file = mp.delete_part(file)
        flag_requirements = mp.take_part(file).split()

        while(file != ''):
            if (flag_requirements.empty()):
                break

            flag_requirements = mp.take_part(file).split()

            if (flag_requirements[0] == ":requirements"):
                for i  in flag_requirements[1:]:
                    self.requirements.append(i)

            if (flag_requirements[0] == ":types"):
                for i in flag_requirements[1:]:
                    self.types.append(i)

            file = mp.delete_part(file)