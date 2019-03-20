#
import src.PDDL.parser as parser
import src.PDDL.grounder as grounder
import src.PDDL.domain as dm
import src.PDDL.task as ts


class Problem:
    def __init__(self, domain_text, task_text):
        self.domain = dm.Domain()
        self.task = ts.Task()

        parsed_domain = parser.ParserForDomain(domain_text)
        parsed_task = parser.ParserForTask(task_text)

        grounder.GrounderForDomain(parsed_domain, self.domain)
        grounder.GrounderForTask(parsed_task, self.task)
