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
        label="Nachdem Sie mit den anderen Personen Ihrer Gruppe neue Informationen zu den infrage kommendenden Bewerbern/Bewerberinnen geteilt haben, für welchen Bewerber/welche Bewerberin wollen Sie nun Ihre Stimme abgeben?",
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
        label="Die Entscheidungen wurden aufgrund von Fakten und nicht aufgrund von persönlichen Vorurteilen und Meinungen getroffen.",
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
        label="Die Regeln und das Verfahren waren für alle gleichermaßen fair.",
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
        label="Die Regeln und das Verfahren waren einheitlich für alle Beteiligten angewandt.",
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
        label="Die Rechte der Beteiligten wurden berücksichtigt. ",
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
        label="Die Beteiligten wurden mit Respekt behandelt.",
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
        label="Die Bedürfnisse der Beteiligten wurden berücksichtigt.",
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
        label="Die Beteiligten haben das Ergebnis des Auswahlverfahrens verdient.",
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
        label="Wie fair waren die Entscheidungsregeln und das Entscheidungsverfahren in dem Auswahlverfahren?",
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
        label="Wie fair war das Ergebnis des Auswahlverfahrens?",
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

def group_by_arrival_time_method(subsession, waiting_players):
    import random
    import datetime

    print(len(waiting_players))
    print(len(subsession.get_players()))

    if len(waiting_players) == len(subsession.get_players()):

        treatment = random.choice([True, False])

        for player in subsession.get_players():
            player.gender_based = treatment
            player.time_start = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        return subsession.get_players()

#    waiting = True
#    for player in waiting_players:
#        if not waiting_too_long(player):
#            waiting = False

#    if waiting == True:
#        return subsession.get_players()

def live_chat(player: Player, data):
    my_id = player.id_in_group
    response = dict(id_in_group=my_id, msg=data)
    return{0: response}

def set_payoffs(group):
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

# PAGES
class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True
    body_text = "Bitte warten Sie einen Moment, bis das Experiment losgeht."

    #def vars_for_template(self):
     #   return {'body_text': 'Sobald die anderen Teilnehmer eintreffen, geht es los.',
     #           'title_text': 'Bitte warten Sie.'}

class ProcedureDescription(Page):
    pass

class ProcedureTask(Page):
    form_model = 'player'
    form_fields = ['describe_procedure']

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

class HiddenProfileWaitPage(WaitPage):
    body_text = "Bitte warten Sie einen Moment, bis das Experiment weitergeht."

class HiddenProfileTask(Page):
    form_model = 'player'
    form_fields = ['hidden_profile_task']

class DiscussionWaitPage(WaitPage):
    body_text = "Bitte warten Sie einen Moment, bis das Experiment weitergeht."

class Discussion(Page):
    timeout_seconds = 600000
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

class Voting(Page):
    form_model = 'player'
    form_fields = ['voted_candidate']

class VotingWaitPage(WaitPage):
    body_text = "Wir bitten Sie um ein bisschen Geduld. Sobald alle Gruppenmitglieder mit der Abstimmung für einen Bewerber/eine Bewerberin fertig sind, können Sie das Experiment fortsetzen."
    after_all_players_arrive = 'set_payoffs'

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

class GeneralAssessment(Page):
    form_model = 'player'
    form_fields = ['groupinteraction1', 'groupinteraction2', 'groupinteraction3']

class FairnessQuiestionnaire(Page):
    form_model = 'player'
    form_fields = ['fairness1', 'fairness2', 'fairness3', 'fairness4', 'fairness5', 'fairness6','fairness7', 'fairness8', 'fairness9']

class Results(Page):
    pass

class Payment(Page):
    form_model = 'player'
    form_fields = ['comments']

class EndOfStudy(Page):
    pass


page_sequence = [
    GroupingWaitPage,
    #ProcedureDescription,
    #ProcedureTask,
    #GroupDisplay,
    #HiddenProfileWaitPage,
    #HiddenProfileTask,
    #DiscussionWaitPage,
    #Discussion,
    Voting,
    VotingWaitPage,
    #Helpfulness,
    #Competence,
    #Competitiveness,
    #Independence,
    #GeneralAssessment,
    #FairnessQuiestionnaire,
    Results,
    Payment,
    EndOfStudy
]