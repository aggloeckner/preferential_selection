from otree.api import *
import time
import random

doc = """
online_experiment
"""

class Constants(BaseConstants):
    name_in_url = 'online_experiment'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    profile_task = models.IntegerField(
        label="Wen würden Sie auf Basis der Ihnen vorliegenden Informationen für die Besetzung der Professur auswählen?",
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
    age = models.IntegerField(
        label="Bitte geben Sie Ihr Alter als ganze Zahl an (z.B. 21):",
        min=18,
        max=99
    )
    gender = models.IntegerField(
        label="Bitte geben Sie das Geschlecht an, dem Sie sich zugehörig fühlen:",
        choices=[
            [1, 'Weiblich'],
            [2, 'Männlich'],
            [3, 'Divers']
        ],
        widget=widgets.RadioSelect
    )
    education = models.IntegerField(
        label="Bitte geben Sie Ihren höchsten Bildungsabschluss an:",
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

# ******************************************************************************************************************** #
# *** Demographics *** #
# ******************************************************************************************************************** #
class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'education']

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Instructions(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class ProfileTask(Page):
    form_model = 'player'
    form_fields = ['profile_task']

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class EndPage(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        if (player.participant.label != "1234555"):
            with open('LabIds/CountParticipation.txt', 'w') as file:
                file.write('\n')
                file.write(player.participant.label)

page_sequence = [
    Demographics,
    Instructions,
    ProfileTask,
    EndPage
]
