# Для того чтобы код нормально заработал, вам потребуется файл домена в формате .pdll и файл таски в таком же формате.
# Если название домена не будет совпадать с требующимся у таски, программа выкинет ошибку.
import sys
import logging
import src.PDDL.problem as prb


def __main__():
    # TODO: сделать проверку на совместимсоть таски и домена и добавить логи
    # Проверка корректности параметров задачи
    if len(sys.argv) != 3:
        logging.error("Неверное количество аргументов в параметрах!")
        exit(1)

    # Загрузка домена
    try:
        domain = open(sys.argv[1], 'r').read()
    except FileNotFoundError:
        logging.error("Неверный путь к домену!")
        exit(2)

    # Загрузка таски
    try:
        task = open(sys.argv[2]).read()
    except FileNotFoundError:
        logging.error("Неверный путь к таске!")
        exit(2)

    problem = prb.Problem(domain, task)
    # problem.domain.print()
    problem.task.print()


if __name__ == "__main__":
    __main__()
