from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'informed_consent_on'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    informed_consent_on = models.BooleanField(
        choices=[
            [True, 'Ja, ich stimme zu.'],
            [False, 'Nein, ich stimme nicht zu.']
        ],
        label=""
    )


# PAGES
class InformedConsent(Page):
    form_model = 'player'
    form_fields = ['informed_consent_on']

    @staticmethod
    def error_message(player, values):
        if(values['informed_consent_on'] == False):
            return "Um fortzufahren müssen Sie der Datenschutzerklärung zustimmen."



page_sequence = [
    InformedConsent
]
