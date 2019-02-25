import src.PDDL.grounder as gr


class Problem:
    def __init__(self, domain, task):
        self.domain = gr.make_domain(domain)
        self.task = gr.make_task(task)
