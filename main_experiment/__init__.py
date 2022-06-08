from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'main_experiment'
    players_per_group = 5
#    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    votesA = models.IntegerField(initial=0)
    votesB = models.IntegerField(initial=0)
    votesC = models.IntegerField(initial=0)
    votesD = models.IntegerField(initial=0)
    votesE = models.IntegerField(initial=0)
    votesF = models.IntegerField(initial=0)
    winner = models.StringField(initial="")
    clearVote = models.BooleanField()
    correctVote = models.BooleanField()
    player1_gender = models.IntegerField()
    player2_gender = models.IntegerField()
    player3_gender = models.IntegerField()
    player4_gender = models.IntegerField()
    player5_gender = models.IntegerField()

class Player(BasePlayer):
    perfect_group = models.BooleanField()
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
    message_A1_time = models.StringField(blank = True)
    message_A2_time = models.StringField(blank = True)
    message_A3_time = models.StringField(blank = True)
    message_A4_time = models.StringField(blank = True)
    message_A5_time = models.StringField(blank = True)
    message_A6_time = models.StringField(blank = True)
    message_A7_time = models.StringField(blank = True)
    message_A8_time = models.StringField(blank = True)
    message_A9_time = models.StringField(blank = True)
    message_B1_time = models.StringField(blank = True)
    message_B2_time = models.StringField(blank = True)
    message_B3_time = models.StringField(blank = True)
    message_B4_time = models.StringField(blank = True)
    message_B5_time = models.StringField(blank = True)
    message_B6_time = models.StringField(blank = True)
    message_B7_time = models.StringField(blank = True)
    message_B8_time = models.StringField(blank = True)
    message_B9_time = models.StringField(blank = True)
    message_C1_time = models.StringField(blank = True)
    message_C2_time = models.StringField(blank = True)
    message_C3_time = models.StringField(blank = True)
    message_C4_time = models.StringField(blank = True)
    message_C5_time = models.StringField(blank = True)
    message_C6_time = models.StringField(blank = True)
    message_C7_time = models.StringField(blank = True)
    message_C8_time = models.StringField(blank = True)
    message_C9_time = models.StringField(blank = True)
    message_D1_time = models.StringField(blank = True)
    message_D2_time = models.StringField(blank = True)
    message_D3_time = models.StringField(blank = True)
    message_D4_time = models.StringField(blank = True)
    message_D5_time = models.StringField(blank = True)
    message_D6_time = models.StringField(blank = True)
    message_D7_time = models.StringField(blank = True)
    message_D8_time = models.StringField(blank = True)
    message_D9_time = models.StringField(blank = True)
    message_E1_time = models.StringField(blank = True)
    message_E2_time = models.StringField(blank = True)
    message_E3_time = models.StringField(blank = True)
    message_E4_time = models.StringField(blank = True)
    message_E5_time = models.StringField(blank = True)
    message_E6_time = models.StringField(blank = True)
    message_E7_time = models.StringField(blank = True)
    message_E8_time = models.StringField(blank = True)
    message_E9_time = models.StringField(blank = True)
    message_F1_time = models.StringField(blank = True)
    message_F2_time = models.StringField(blank = True)
    message_F3_time = models.StringField(blank = True)
    message_F4_time = models.StringField(blank = True)
    message_F5_time = models.StringField(blank = True)
    message_F6_time = models.StringField(blank = True)
    message_F7_time = models.StringField(blank = True)
    message_F8_time = models.StringField(blank = True)
    message_F9_time = models.StringField(blank = True)
    voted_candidate = models.IntegerField(
        label="Nachdem Sie mit den anderen Personen Ihrer Gruppe neue Informationen zu den infrage kommendenden Bewerber/innen geteilt haben, für welche/n Bewerber/in wollen Sie nun Ihre Stimme abgeben?",
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
    helpfulnessPlayer1 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht hilfreich'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr hilfreich'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    helpfulnessPlayer2 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht hilfreich'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr hilfreich'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    helpfulnessPlayer3 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht hilfreich'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr hilfreich'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    helpfulnessPlayer4 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht hilfreich'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr hilfreich'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    helpfulnessPlayer5 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht hilfreich'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr hilfreich'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    competencePlayer1 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht kompetent'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr kompetent'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    competencePlayer2 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht kompetent'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr kompetent'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    competencePlayer3 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht kompetent'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr kompetent'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    competencePlayer4 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht kompetent'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr kompetent'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    competencePlayer5 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht kompetent'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr kompetent'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    competitivenessPlayer1 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht konkurrenzfähig'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr konkurrenzfähig'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    competitivenessPlayer2 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht konkurrenzfähig'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr konkurrenzfähig'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    competitivenessPlayer3 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht konkurrenzfähig'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr konkurrenzfähig'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    competitivenessPlayer4 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht konkurrenzfähig'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr konkurrenzfähig'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    competitivenessPlayer5 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht konkurrenzfähig'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr konkurrenzfähig'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    independencePlayer1 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht eigenständig'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr eigenständig'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    independencePlayer2 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht eigenständig'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr eigenständig'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    independencePlayer3 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht eigenständig'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr eigenständig'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    independencePlayer4 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht eigenständig'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr eigenständig'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    independencePlayer5 = models.IntegerField(
        label="",
        choices=[
            [1, 'gar nicht eigenständig'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr eigenständig'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    groupinteraction1 = models.IntegerField(
        label="Ich sehe mich selbst als Mitglied meiner 5er-Gruppe.",
        choices=[
            [1, 'sehr wenig'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr stark'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    groupinteraction2 = models.IntegerField(
        label="Würden Sie gerne weitere Aufgaben gemeinsam mit Ihrer Gruppe bearbeiten?",
        choices=[
            [1, 'sehr ungern'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr gern'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    groupinteraction3 = models.IntegerField(
        label="Wie wohl haben Sie sich während der Bearbeitung der Gruppenaufgabe gefühlt?",
        choices=[
            [1, 'sehr unwohl'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, 'sehr wohl'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    fairness1 = models.IntegerField(
        label="Die Entscheidungen bezüglich der Zusammensetzung der Berufungskommission wurden aufgrund von Fakten und nicht aufgrund von persönlichen Vorurteilen und Meinungen getroffen.",
        choices=[
            [1, 'stimme voll zu'],
            [2, 'stimme zu'],
            [3, 'stimme eher zu'],
            [4, 'teils, teils'],
            [5, 'stimme eher nicht zu'],
            [6, 'stimme nicht zu'],
            [7, 'stimme überhaupt nicht zu']
        ],
        widget=widgets.RadioSelect
    )
    fairness2 = models.IntegerField(
        label="Die Regeln und das Verfahren, die zur Auswahl der Mitglieder der Berufungskommission dienten, waren für alle gleichermaßen fair.",
        choices=[
            [1, 'stimme voll zu'],
            [2, 'stimme zu'],
            [3, 'stimme eher zu'],
            [4, 'teils, teils'],
            [5, 'stimme eher nicht zu'],
            [6, 'stimme nicht zu'],
            [7, 'stimme überhaupt nicht zu']
        ],
        widget=widgets.RadioSelect
    )
    fairness3 = models.IntegerField(
        label="Die Regeln und das Verfahren, die zur Auswahl der Mitglieder der Berufungskommission dienten, waren einheitlich für alle Beteiligten angewandt.",
        choices=[
            [1, 'stimme voll zu'],
            [2, 'stimme zu'],
            [3, 'stimme eher zu'],
            [4, 'teils, teils'],
            [5, 'stimme eher nicht zu'],
            [6, 'stimme nicht zu'],
            [7, 'stimme überhaupt nicht zu']
        ],
        widget=widgets.RadioSelect
    )
    fairness4 = models.IntegerField(
        label="Die Rechte der Beteiligten wurden bei der Zusammenstellung der Gruppe berücksichtigt. ",
        choices=[
            [1, 'stimme voll zu'],
            [2, 'stimme zu'],
            [3, 'stimme eher zu'],
            [4, 'teils, teils'],
            [5, 'stimme eher nicht zu'],
            [6, 'stimme nicht zu'],
            [7, 'stimme überhaupt nicht zu']
        ],
        widget=widgets.RadioSelect
    )
    fairness5 = models.IntegerField(
        label="Die Beteiligten wurden bei der Zusammenstellung der Gruppe  mit Respekt behandelt.",
        choices=[
            [1, 'stimme voll zu'],
            [2, 'stimme zu'],
            [3, 'stimme eher zu'],
            [4, 'teils, teils'],
            [5, 'stimme eher nicht zu'],
            [6, 'stimme nicht zu'],
            [7, 'stimme überhaupt nicht zu']
        ],
        widget=widgets.RadioSelect
    )
    fairness6 = models.IntegerField(
        label="Die Bedürfnisse der Beteiligten wurden bei der Zusammenstellung der Gruppe berücksichtigt.",
        choices=[
            [1, 'stimme voll zu'],
            [2, 'stimme zu'],
            [3, 'stimme eher zu'],
            [4, 'teils, teils'],
            [5, 'stimme eher nicht zu'],
            [6, 'stimme nicht zu'],
            [7, 'stimme überhaupt nicht zu']
        ],
        widget=widgets.RadioSelect
    )
    fairness7 = models.IntegerField(
        label="Die Beteiligten haben das Ergebnis des Auswahlverfahrens zur Zusammensetzung der Berufungskommission verdient.",
        choices=[
            [1, 'stimme voll zu'],
            [2, 'stimme zu'],
            [3, 'stimme eher zu'],
            [4, 'teils, teils'],
            [5, 'stimme eher nicht zu'],
            [6, 'stimme nicht zu'],
            [7, 'stimme überhaupt nicht zu']
        ],
        widget=widgets.RadioSelect
    )
    fairness8 = models.IntegerField(
        label="Wie fair waren die Entscheidungsregeln und das Entscheidungsverfahren in dem Auswahlverfahren zur Zusammensetzung Ihrer Gruppe?",
        choices=[
            [1, 'sehr fair'],
            [2, 'fair'],
            [3, 'eher fair'],
            [4, 'weder fair noch unfair'],
            [5, 'eher unfair'],
            [6, 'unfair'],
            [7, 'sehr unfair']
        ],
        widget=widgets.RadioSelect
    )
    fairness9 = models.IntegerField(
        label="Wie fair war das Ergebnis des Auswahlverfahrens zur Zusammensetzung Ihrer Gruppe?",
        choices=[
            [1, 'sehr fair'],
            [2, 'fair'],
            [3, 'eher fair'],
            [4, 'weder fair noch unfair'],
            [5, 'eher unfair'],
            [6, 'unfair'],
            [7, 'sehr unfair']
        ],
        widget=widgets.RadioSelect
    )
    comments = models.LongStringField(
        label = '',
        blank = True
    )

    def waiting_too_long(player):
        participant = player.participant

        import time
        # assumes you set wait_page_arrival in PARTICIPANT_FIELDS.
        return time.time() - participant.wait_page_arrival > 5 * 60

# DEFS

def group_players(subsession):
    import random
    import datetime

    weights = []

    with open('LabIds/CountGenderBased.txt', 'r') as file:
        weights.append(105-int(file.read()))

    with open('LabIds/CountPerformanceBased.txt', 'r') as file:
        weights.append(105-int(file.read()))

    if weights[0] < 0:
        weights[0] = 0
    if weights[1] < 0:
        weights[1] = 0
    if weights[0] == 0 and weights[1] == 0:
        weights[0] = 1
        weights[1] = 1

    print(weights)

    treatment = random.choices([False, True],weights=weights,k=int(len(subsession.get_players())/5))

    males = []
    females = []
    others = []

    for p in subsession.get_players():
        if p.participant.p_gender == 1:
            females.append(p)
        elif p.participant.p_gender == 2:
            males.append(p)
        else:
            others.append(p)

    matrix_of_groups = []
    group = []
    for j in range(int(len(subsession.get_players())/5)):
        if len(females) >= 2 and len(males) >= 3:
            for i in range(2):
                group.append(females[0].id_in_subsession)
                females[0].perfect_group = True
                females[0].gender_based = treatment[j]
                females.pop(0)
            for i in range(3):
                group.append(males[0].id_in_subsession)
                males[0].perfect_group = True
                males[0].gender_based = treatment[j]
                males.pop(0)
        else:
            for i in range(5):
                if len(group) < 5:
                    if len(females) > 0:
                        group.append(females[0].id_in_subsession)
                        females[0].perfect_group = False
                        females[0].gender_based = False
                        females.pop(0)
                    elif len(males) > 0:
                        group.append(males[0].id_in_subsession)
                        males[0].perfect_group = False
                        males[0].gender_based = False
                        males.pop(0)
                    else:
                        group.append(others[0].id_in_subsession)
                        others[0].perfect_group = False
                        others[0].gender_based = False
                        others.pop(0)

        matrix_of_groups.append(group.copy())
        group.clear()

    for p in subsession.get_players():
        p.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    subsession.set_group_matrix(matrix_of_groups)


def live_chat(player: Player, data):
    my_id = player.id_in_group
    response = dict(id_in_group=my_id, msg=data)
    return{0: response}

def live_chatTest(player: Player, data):
    my_id = player.id_in_group
    response = dict(id_in_group=my_id, msg=data)
    return{0: response}

def set_payoffs(group):
    group.player1_gender = group.get_player_by_id(1).participant.p_gender
    group.player2_gender = group.get_player_by_id(2).participant.p_gender
    group.player3_gender = group.get_player_by_id(3).participant.p_gender
    group.player4_gender = group.get_player_by_id(4).participant.p_gender
    group.player5_gender = group.get_player_by_id(5).participant.p_gender

    players = group.get_players()
    for p in players:
        group.votesA += (p.voted_candidate == 1)
        group.votesB += (p.voted_candidate == 2)
        group.votesC += (p.voted_candidate == 3)
        group.votesD += (p.voted_candidate == 4)
        group.votesE += (p.voted_candidate == 5)
        group.votesF += (p.voted_candidate == 6)

    maxVotes = max(group.votesA, group.votesB, group.votesC, group.votesD, group.votesE, group.votesF)
    if group.votesA == maxVotes:
        group.winner = "Bewerber/in A"
    if group.votesB == maxVotes:
        if group.winner != "":
            group.winner += " und "
        group.winner += "Bewerber/in B"
    if group.votesC == maxVotes:
        if group.winner != "":
            group.winner += " und "
        group.winner += "Bewerber/in C"
    if group.votesD == maxVotes:
        if group.winner != "":
            group.winner += " und "
        group.winner += "Bewerber/in D"
    if group.votesE == maxVotes:
        if group.winner != "":
            group.winner += " und "
        group.winner += "Bewerber/in E"
    if group.votesF == maxVotes:
        if group.winner != "":
            group.winner += " und "
        group.winner += "Bewerber/in F"
    group.clearVote = not ("und" in group.winner)
    group.correctVote = "Bewerber/in A" in group.winner and group.clearVote
    print(group.winner)

    for p in players:
        if group.correctVote:
            p.payoff = 13.5
        else:
            p.payoff = 8.5

# ADMINPAGE
def vars_for_admin_report(subsession):
    with open('LabIds/CountGenderBased.txt', 'r') as file:
        completions_gender = int(file.read())

    with open('LabIds/CountPerformanceBased.txt', 'r') as file:
        completions_performance = int(file.read())

    completions = completions_gender + completions_performance

    with open('LabIds/CostsLab.txt', 'r') as file:
        costs = file.read()

    return dict(
        completions = completions,
        completions_gender = completions_gender,
        completions_performance = completions_performance,
        costs = costs
    )

# PAGES
class GroupingWaitPage(WaitPage):
    after_all_players_arrive = group_players
    wait_for_all_groups = True
    body_text = "Bitte warten Sie einen Moment, bis das Experiment losgeht."

    #def vars_for_template(self):
     #   return {'body_text': 'Sobald die anderen Teilnehmer eintreffen, geht es los.',
     #           'title_text': 'Bitte warten Sie.'}

class Instructions(Page):
    @staticmethod
    def vars_for_template(player):
        number_females = 0
        number_males = 0
        number_diverse = 0
        number_others = 0

        for p in player.get_others_in_group():
            if p.participant.p_gender == 1:
                number_females += 1
            if p.participant.p_gender == 2:
                number_males += 1
            if p.participant.p_gender == 3:
                number_diverse += 1
            if p.participant.p_gender == 4:
                number_others += 1

        if player.participant.p_gender == 1:
            number_females += 1
        if player.participant.p_gender == 2:
            number_males += 1
        if player.participant.p_gender == 3:
            number_diverse += 1
        if player.participant.p_gender == 4:
            number_others += 1

        return dict(
            number_females = number_females,
            number_males = number_males,
            number_diverse = number_diverse,
            number_others = number_others,
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")


class DescribeProcedure(Page):
    form_model = 'player'
    form_fields = ['describe_procedure']

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class GroupDisplay(Page):
    @staticmethod
    def js_vars(player):
        return dict(
            player_id=player.id_in_group,
            my_gender=player.participant.p_gender,
            player1_gender=player.group.get_player_by_id(1).participant.p_gender,
            player2_gender=player.group.get_player_by_id(2).participant.p_gender,
            player3_gender=player.group.get_player_by_id(3).participant.p_gender,
            player4_gender=player.group.get_player_by_id(4).participant.p_gender,
            player5_gender=player.group.get_player_by_id(5).participant.p_gender,
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class HiddenProfileWaitPage(WaitPage):
    body_text = "Bitte warten Sie einen Moment, bis das Experiment weitergeht."

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class HiddenProfileTask(Page):
    form_model = 'player'
    form_fields = ['hidden_profile_task']

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class DiscussionTestPage(Page):
    form_model = 'player'
    live_method = 'live_chatTest'
    @staticmethod
    def js_vars(player):
        return dict(
            player_id=player.id_in_group,
            my_gender=player.participant.p_gender,
            player1_gender=player.group.get_player_by_id(1).participant.p_gender,
            player2_gender=player.group.get_player_by_id(2).participant.p_gender,
            player3_gender=player.group.get_player_by_id(3).participant.p_gender,
            player4_gender=player.group.get_player_by_id(4).participant.p_gender,
            player5_gender=player.group.get_player_by_id(5).participant.p_gender,
        )

class DiscussionWaitPage(WaitPage):
    body_text = "Bitte warten Sie einen Moment, bis das Experiment weitergeht."

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Discussion(Page):
    form_model = 'player'
    form_fields = [
        'message_A1_time','message_A2_time','message_A3_time','message_A4_time','message_A5_time','message_A6_time','message_A7_time','message_A8_time','message_A9_time',
        'message_B1_time','message_B2_time','message_B3_time','message_B4_time','message_B5_time','message_B6_time','message_B7_time','message_B8_time','message_B9_time',
        'message_C1_time','message_C2_time','message_C3_time','message_C4_time','message_C5_time','message_C6_time','message_C7_time','message_C8_time','message_C9_time',
        'message_D1_time','message_D2_time','message_D3_time','message_D4_time','message_D5_time','message_D6_time','message_D7_time','message_D8_time','message_D9_time',
        'message_E1_time','message_E2_time','message_E3_time','message_E4_time','message_E5_time','message_E6_time','message_E7_time','message_E8_time','message_E9_time',
        'message_F1_time','message_F2_time','message_F3_time','message_F4_time','message_F5_time','message_F6_time','message_F7_time','message_F8_time','message_F9_time',
    ]

    timeout_seconds = 600
    timer_text = 'Verbleibende Zeit: <br>'
    live_method = 'live_chat'

    @staticmethod
    def js_vars(player):
        return dict(
            player_id = player.id_in_group,
            my_gender = player.participant.p_gender,
            player1_gender = player.group.get_player_by_id(1).participant.p_gender,
            player2_gender = player.group.get_player_by_id(2).participant.p_gender,
            player3_gender = player.group.get_player_by_id(3).participant.p_gender,
            player4_gender = player.group.get_player_by_id(4).participant.p_gender,
            player5_gender = player.group.get_player_by_id(5).participant.p_gender,
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Voting(Page):
    form_model = 'player'
    form_fields = ['voted_candidate']

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class VotingWaitPage(WaitPage):
    body_text = "Wir bitten Sie um ein bisschen Geduld. Sobald alle Gruppenmitglieder mit der Abstimmung für einen Bewerber/eine Bewerberin fertig sind, können Sie das Experiment fortsetzen."
    after_all_players_arrive = 'set_payoffs'

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Helpfulness(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player):
        if player.participant.id_in_session == 1:
            return ['helpfulnessPlayer2','helpfulnessPlayer3','helpfulnessPlayer4','helpfulnessPlayer5']
        elif player.participant.id_in_session == 2:
            return ['helpfulnessPlayer1','helpfulnessPlayer3','helpfulnessPlayer4','helpfulnessPlayer5']
        elif player.participant.id_in_session == 3:
            return ['helpfulnessPlayer1','helpfulnessPlayer2','helpfulnessPlayer4','helpfulnessPlayer5']
        elif player.participant.id_in_session == 4:
            return ['helpfulnessPlayer1','helpfulnessPlayer2','helpfulnessPlayer3','helpfulnessPlayer5']
        else:
            return ['helpfulnessPlayer1','helpfulnessPlayer2','helpfulnessPlayer3','helpfulnessPlayer4']

    @staticmethod
    def js_vars(player):
        return dict(
            player_id = player.id_in_group,
            my_gender = player.participant.p_gender,
            player1_gender = player.group.get_player_by_id(1).participant.p_gender,
            player2_gender = player.group.get_player_by_id(2).participant.p_gender,
            player3_gender = player.group.get_player_by_id(3).participant.p_gender,
            player4_gender = player.group.get_player_by_id(4).participant.p_gender,
            player5_gender = player.group.get_player_by_id(5).participant.p_gender,
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Competence(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player):
        if player.participant.id_in_session == 1:
            return ['competencePlayer2','competencePlayer3','competencePlayer4','competencePlayer5']
        elif player.participant.id_in_session == 2:
            return ['competencePlayer1','competencePlayer3','competencePlayer4','competencePlayer5']
        elif player.participant.id_in_session == 3:
            return ['competencePlayer1','competencePlayer2','competencePlayer4','competencePlayer5']
        elif player.participant.id_in_session == 4:
            return ['competencePlayer1','competencePlayer2','competencePlayer3','competencePlayer5']
        else:
            return ['competencePlayer1','competencePlayer2','competencePlayer3','competencePlayer4']

    @staticmethod
    def js_vars(player):
        return dict(
            player_id = player.id_in_group,
            my_gender = player.participant.p_gender,
            player1_gender = player.group.get_player_by_id(1).participant.p_gender,
            player2_gender = player.group.get_player_by_id(2).participant.p_gender,
            player3_gender = player.group.get_player_by_id(3).participant.p_gender,
            player4_gender = player.group.get_player_by_id(4).participant.p_gender,
            player5_gender = player.group.get_player_by_id(5).participant.p_gender,
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Competitiveness(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player):
        if player.participant.id_in_session == 1:
            return ['competitivenessPlayer2','competitivenessPlayer3','competitivenessPlayer4','competitivenessPlayer5']
        elif player.participant.id_in_session == 2:
            return ['competitivenessPlayer1','competitivenessPlayer3','competitivenessPlayer4','competitivenessPlayer5']
        elif player.participant.id_in_session == 3:
            return ['competitivenessPlayer1','competitivenessPlayer2','competitivenessPlayer4','competitivenessPlayer5']
        elif player.participant.id_in_session == 4:
            return ['competitivenessPlayer1','competitivenessPlayer2','competitivenessPlayer3','competitivenessPlayer5']
        else:
            return ['competitivenessPlayer1','competitivenessPlayer2','competitivenessPlayer3','competitivenessPlayer4']

    @staticmethod
    def js_vars(player):
        return dict(
            player_id = player.id_in_group,
            my_gender = player.participant.p_gender,
            player1_gender = player.group.get_player_by_id(1).participant.p_gender,
            player2_gender = player.group.get_player_by_id(2).participant.p_gender,
            player3_gender = player.group.get_player_by_id(3).participant.p_gender,
            player4_gender = player.group.get_player_by_id(4).participant.p_gender,
            player5_gender = player.group.get_player_by_id(5).participant.p_gender,
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Independence(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player):
        if player.participant.id_in_session == 1:
            return ['independencePlayer2','independencePlayer3','independencePlayer4','independencePlayer5']
        elif player.participant.id_in_session == 2:
            return ['independencePlayer1','independencePlayer3','independencePlayer4','independencePlayer5']
        elif player.participant.id_in_session == 3:
            return ['independencePlayer1','independencePlayer2','independencePlayer4','independencePlayer5']
        elif player.participant.id_in_session == 4:
            return ['independencePlayer1','independencePlayer2','independencePlayer3','independencePlayer5']
        else:
            return ['independencePlayer1','independencePlayer2','independencePlayer3','independencePlayer4']

    @staticmethod
    def js_vars(player):
        return dict(
            player_id = player.id_in_group,
            my_gender = player.participant.p_gender,
            player1_gender = player.group.get_player_by_id(1).participant.p_gender,
            player2_gender = player.group.get_player_by_id(2).participant.p_gender,
            player3_gender = player.group.get_player_by_id(3).participant.p_gender,
            player4_gender = player.group.get_player_by_id(4).participant.p_gender,
            player5_gender = player.group.get_player_by_id(5).participant.p_gender,
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class GeneralAssessment(Page):
    form_model = 'player'
    form_fields = ['groupinteraction1', 'groupinteraction2', 'groupinteraction3']

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class FairnessQuiestionnaire(Page):
    form_model = 'player'
    form_fields = ['fairness1', 'fairness2', 'fairness3', 'fairness4', 'fairness5', 'fairness6','fairness7', 'fairness8', 'fairness9']

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        if(player.participant.label != "1234555"):
            if player.perfect_group and player.gender_based:
                with open('LabIds/CountGenderBased.txt', 'r') as file:
                    txt = int(file.read())
                    txt += 1
                with open('LabIds/CountGenderBased.txt', 'w') as file:
                    file.write(str(txt))
            if player.perfect_group and not player.gender_based:
                with open('LabIds/CountPerformanceBased.txt', 'r') as file:
                    txt = int(file.read())
                    txt += 1
                with open('LabIds/CountPerformanceBased.txt', 'w') as file:
                    file.write(str(txt))
            with open('LabIds/Participated.txt', 'a') as file:
                file.write('\n')
                file.write(player.participant.label)
            with open('LabIds/CostsLab.txt', 'r') as file:
                txt = float(file.read())
                txt += player.payoff
            with open('LabIds/CostsLab.txt', 'w') as file:
                file.write(str(txt))

class Results(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Payment(Page):
    form_model = 'player'
    form_fields = ['comments']

    @staticmethod
    def before_next_page(player, timeout_happened):
        import datetime
        player.participant.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class EndOfStudy(Page):
    pass


page_sequence = [
    GroupingWaitPage,
    Instructions,
    DescribeProcedure,
    GroupDisplay,
    HiddenProfileWaitPage,
    HiddenProfileTask,
    DiscussionTestPage,
    DiscussionWaitPage,
    Discussion,
    Voting,
    VotingWaitPage,
    Helpfulness,
    Competence,
    Competitiveness,
    Independence,
    GeneralAssessment,
    FairnessQuiestionnaire,
    Results,
    Payment,
    EndOfStudy
]