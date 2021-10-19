from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'main_experiment'
#    players_per_group = 5
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time_start = models.StringField()
    gender_based = models.BooleanField()
    describe_procedure = models.TextField(label="")

# DEFS

def group_by_arrival_time_method(subsession, waiting_players):
    import random
    import datetime

    if len(waiting_players) >= subsession.session.config['num_demo_participants']:

        treatment = random.choice([True, False])

        for player in subsession.get_players():
            player.gender_based = treatment
            player.time_start = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        return subsession.get_players()


# PAGES
class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True

    def vars_for_template(self):
        return {'body_text': 'Sobald die anderen Teilnehmer eintreffen, geht es los.',
                'title_text': 'Bitte warten Sie.'}

class ProcedureDescription(Page):
    pass

class ProcedureTask(Page):
    form_model = 'player'
    form_fields = ['describe_procedure']

class HiddenProfileTask(Page):
    form_model = 'player'
    form_fields = ['describe_procedure']

class Discussion(Page):
    form_model = 'player'
    form_fields = ['describe_procedure']

class Voting(Page):
    form_model = 'player'
    form_fields = ['describe_procedure']

class GeneralAssessment(Page):
    pass

class InformationRelevance(Page):
    pass

class FairnessQuiestionnaire(Page):
    pass

class Results(Page):
    pass

class Payment(Page):
    pass


page_sequence = [
    GroupingWaitPage,
    ProcedureDescription,
    ProcedureTask,
    HiddenProfileTask,
    Discussion,
    Voting,
    GeneralAssessment,
    InformationRelevance,
    FairnessQuiestionnaire,
    Results,
    Payment
]