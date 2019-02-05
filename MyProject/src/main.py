import sys
import logging
import pddl.parser.domain as dm
import pddl.parser.problem as pb
import pddl.parser.myparser as mp




if (len(sys.argv) != 3):
    logging.error("Неверное количество аргументов в параметрах!")
    print(len(sys.argv))
    exit(1)

try:
    domain = open(sys.argv[1], 'r').read()
except FileNotFoundError:
    logging.error("Неверный путь к домену!")
    exit(2)

try:
    task = open(sys.argv[2]).read()
except FileNotFoundError:
    logging.error("Неверный путь к таске!")
    exit(2)

dom = dm.Domain(domain)
prob = pb.Problem(task)


print(domain)
print('________________________________________________________________________________________________________________')
print(dom.name)
print(dom.requirements)
print(dom.types)
for i in dom.predicates:
    print(i.quantify, i.name, i.params)
for i in dom.actions:
    print(i.name, i.parameters)
    print(i.quantifier_for_pre, i.precondition)
    print(i.quantifier_for_eff, i.effect)

print('________________________________________________________________________________________________________________')

print(task)
print('________________________________________________________________________________________________________________')
print(prob.name)
print(prob.domain_name)
print(prob.objects)
for i in prob.init:
    print(i.name, i.quantify, i.params)
print(prob.goal_quantify)
for i in prob.goal:
    print(i.name, i.params)