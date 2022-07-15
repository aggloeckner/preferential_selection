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

# ADMINPAGE
def vars_for_admin_report(subsession):
    with open('LabIds/CostsOnline.txt', 'r') as file:
        costs_online = file.read()

    with open('LabIds/CostsLab.txt', 'r') as file:
        costs_lab = file.read()

    with open('LabIds/CountOnlineStudy.txt', 'r') as file:
        completions_online = int(file.read())

    with open('LabIds/CountGenderBased.txt', 'r') as file:
        completions_gender = int(file.read())

    with open('LabIds/CountPerformanceBased.txt', 'r') as file:
        completions_performance = int(file.read())

    completions_lab = completions_gender + completions_performance

    return dict(
        completions_online = completions_online,
        completions_gender = completions_gender,
        completions_performance = completions_performance,
        completions_lab = completions_lab,
        costs_online = costs_online,
        costs_lab = costs_lab
    )


# PAGES

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

        player.payoff = 2

        if (player.participant.label != "1234555"):
            with open('LabIds/OnlineStudy.txt', 'a') as file:
                file.write('\n')
                file.write(player.participant.label)

            with open('LabIds/CountOnlineStudy.txt', 'r') as file:
                txt = int(file.read())
                txt += 1
            with open('LabIds/CountOnlineStudy.txt', 'w') as file:
                file.write(str(txt))

            with open('LabIds/CostsOnline.txt', 'r') as file:
                txt = float(file.read())
                print(txt)
                txt += float(player.payoff)
                print(txt)
            with open('LabIds/CostsOnline.txt', 'w') as file:
                file.write(str(txt))

class EndPage(Page):
    pass

page_sequence = [
    Demographics,
    Instructions,
    ProfileTask,
    EndPage
]