import src.PDDL.fields as fields


class POP:
    def __init__(self, problem):
        start_action = fields.Action()
        start_action.name = 'initial'
        start_action.parameters = problem.task.objects
        start_action.effect = problem.task.init
        initial = Step(start_action)

        end_action = fields.Action()
        end_action.name = 'goal'
        end_action.parameters = problem.task.objects
        end_action.quantify_for_effect = problem.task.quantify_for_goal
        end_action.precondition = problem.task.goal
        goal = Step(end_action)

        agenda = Agenda()
        partial_plan = PartialPlan()

        for i in goal.action.precondition:
            agenda.open_links.add(i)

        for i in problem.domain.actions:
            partial_plan.steps.add(Step(i))

        print(agenda.open_links)
        for i in partial_plan.steps:
            i.action.print()


class Step:
    def __init__(self, action):
        self.action = action
        self.time_start = 0
        self.time_end = 0


class Threat:
    def __init__(self):
        self.threatening_step = ''
        self.casual_link = ''


class OpenLink:
    def __init__(self):
        self.end_step = ''
        self.reached_literal = ''


class CasualLink:
    def __init__(self):
        self.beg_step = ''
        self.end_step = ''
        self.reached_literal = ''


class Agenda:
    def __init__(self):
        self.open_links = set()
        self.threats = set()


class PartialPlan:
    def __init__(self):
        self.steps = set()
        self.order = set()

    def make_order(self, first_step, second_step):
        self.order.add([first_step, second_step])
