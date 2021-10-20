from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'demographics'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(
        label="Bitte geben Sie ihr Alter als ganze Zahl an (z.B. 21):",
        min=18,
        max=99
    )
    gender = models.IntegerField(
        label = "Bitte geben Sie das Geschlecht an, dem Sie sich zugehörig fühlen:",
        choices=[
            [1, 'Weiblich'],
            [2, 'Männlich'],
            [3, 'Divers'],
            [4, 'Anderes'],
        ],
        widget=widgets.RadioSelect
    )
    education = models.IntegerField(
        label = "Bitte geben Sie Ihren höchsten Bildungsabschluss an:",
        choices=[
            [1, '(noch) kein Schulabschluss'],
            [2, 'Grund-/Hauptschulabschluss'],
            [3, 'Realschulabschluss (Mittlere Reife)'],
            [4, 'Abitur/Fachabitur (allgemeine oder fachgebundene Hochschulreife)'],
            [5, 'Abgeschlossene Ausbildung'],
            [6, 'Hochschulabschluss (Bachelor, Master, Diplom, Staatsexamen, Promotion)'],
        ],
        widget=widgets.RadioSelect
    )


# PAGES
class demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education']

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.p_gender = player.gender


page_sequence = [
    demographics
]
