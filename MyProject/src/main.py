import sys
import logging
import pddl.parser.domain as dm
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

new = dm.Domain(domain)
# for i in new.actions:
#     print(i.name)
#     print(i.parameters)