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
    hidden_profile_task = models.IntegerField(
        label="Wen würden Sie auf Basis der Ihnen aktuell vorliegenden Informationen für die Besetzung der Professur auswählen?",
        choices=[
            [1, 'Bewerber/in A'],
            [2, 'Bewerber/in B'],
            [3, 'Bewerber/in C'],
            [4, 'Bewerber/in D'],
            [5, 'Bewerber/in E'],
            [6, 'Bewerber/in F'],
        ],
        widget=widgets.RadioSelect
    )
    voted_candidate = models.IntegerField(
        label="Nachdem Sie mit den anderen Personen Ihrer Gruppe neue Informationen zu den infrage kommendenden Bewerbern/Bewerberinnen geteilt haben, für welche/n Bewerber/in wollen Sie nun Ihre Stimme abgeben?",
        choices=[
            [1, 'Bewerber/in A'],
            [2, 'Bewerber/in B'],
            [3, 'Bewerber/in C'],
            [4, 'Bewerber/in D'],
            [5, 'Bewerber/in E'],
            [6, 'Bewerber/in F'],
        ],
        widget=widgets.RadioSelect
    )

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

def live_chat(player: Player, data):
    my_id = player.id_in_group
    response = dict(id_in_group=my_id, msg=data)
    return{0: response}

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
    form_fields = ['hidden_profile_task']

class DiscussionWaitPage(WaitPage):
    pass

class Discussion(Page):
    timeout_seconds = 600
    timer_text = 'Verbleibende Zeit: <br>'
    live_method = 'live_chat'

class Voting(Page):
    form_model = 'player'
    form_fields = ['voted_candidate']

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
    DiscussionWaitPage,
    Discussion,
    Voting,
    GeneralAssessment,
    InformationRelevance,
    FairnessQuiestionnaire,
    Results,
    Payment
]