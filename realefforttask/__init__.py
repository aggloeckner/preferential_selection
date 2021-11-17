from otree.api import *
import time
import random

doc = """
realefforttask
"""

class Constants(BaseConstants):
    name_in_url = 'realefforttask'
    players_per_group = None
    task_timer = 120
    num_rounds = 100
    d_total = 20
    b_total = 60
    total_letters = 80
    fixed_payoff = cu(1.00)
    bonus_payoff = cu(0.15)



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # create choice fields for the letters task
    # ----------------------------------------------------------------------------------------------------------
    for j in range(1, Constants.total_letters + 1):
        locals()['choice_' + str(j)] = models.StringField(blank=True)
    del j

    # create fields for consent
    # ----------------------------------------------------------------------------------------------------------

    submit_noConsent = models.BooleanField(blank=True, initial=False)

    # create fields for demographics questionnaire
    # ----------------------------------------------------------------------------------------------------------

    gender = models.StringField()
    gender_others = models.StringField(blank=True)
    age = models.IntegerField(min=18, max=100)



    # create field for players task timer
    # ----------------------------------------------------------------------------------------------------------
    task_timer = models.IntegerField(initial=Constants.task_timer)


    # create fields for checking correctness of the task
    # ----------------------------------------------------------------------------------------------------------
    d_crossed = models.IntegerField(initial=0)
    b_crossed = models.IntegerField(initial=0)
    total_correct = models.IntegerField(initial=0)
    correct = models.IntegerField(initial=0)
    is_correct = models.BooleanField(initial=False)


    def count_effort(player):
        player.d_crossed = player.participant.letters_choices_made.count('d')
        player.b_crossed = player.participant.letters_choices_made.count('b')

    def check_correctness(player):
        if player.participant.letters_choices_made.count('d') == Constants.d_total \
                and player.participant.letters_choices_made.count('b') == 0:
            player.correct = 1
            player.is_correct = True
        else:
            player.correct = 0
            player.is_correct = False

    def update_endgame(player):
        player.participant.endgame = 1
        print(player.participant.endgame)

def creating_session(subsession):
    n = Constants.total_letters
    for p in subsession.get_players():
        print("Test")
        # create a list of letter choices
        # ----------------------------------------------------------------------------------------------------------
        indices = [j for j in range(1, n + 1)]
        # create a list corresponding to form_field variables including all choices
        # ----------------------------------------------------------------------------------------------------------
        form_fields = ['choice_' + str(k) for k in indices]
        # create a list of letters
        # ----------------------------------------------------------------------------------------------------------
        d_list = ['d'] * Constants.d_total
        b_list = ['b'] * Constants.b_total
        letters_list = d_list + b_list

        p.participant.letters_choices = list(
            zip(
                indices,
                form_fields,
                letters_list
            )
        )

        p.participant.letters_choices_made = [None for j in range(1, n + 1)]
        p.participant.endgame = 0

# variables for all templates
# --------------------------------------------------------------------------------------------------------------------
def vars_for_all_templates(player):
    return {
        'total_letters': Constants.total_letters,
        'd_total': Constants.d_total,
        'b_total': Constants.d_total,
        'num_rounds': Constants.num_rounds,
        'fixed_payoff': Constants.fixed_payoff,
        'bonus_payoff': Constants.bonus_payoff
    }

# ******************************************************************************************************************** #
# *** Welcome *** #
# ******************************************************************************************************************** #

class Welcome(Page):
    vars_for_template = vars_for_all_templates

    # only display Welcome Page in round 1
    # ----------------------------------------------------------------------------------------------------------------


    def is_displayed(player):
        return player.round_number == 1


# ******************************************************************************************************************** #
# *** Demographics *** #
# ******************************************************************************************************************** #
class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'gender_others', 'age']
    vars_for_template = vars_for_all_templates

    # only display Demographics Page in round 1
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(player):
        return player.round_number == 1


# ******************************************************************************************************************** #
# *** Instructions *** #
# ******************************************************************************************************************** #


class Instructions(Page):
    vars_for_template = vars_for_all_templates

    # only display instruction in round 1
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(player):
        return player.round_number == 1

    # start measuring time of a trial round
    # ----------------------------------------------------------------------------------------------------------------
    def before_next_page(player, timeout_happened):
        player.participant.expiry_timestamp = time.time() + player.task_timer


# ******************************************************************************************************************** #
# *** TASK PAGE *** #
# ******************************************************************************************************************** #
class TaskTrial(Page):
    # form model
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'
    # time text
    # ----------------------------------------------------------------------------------------------------------------
    timer_text = 'Verfügbare Zeit, um so viele Matrizen wie möglich zu lösen:'

    # form fields
    # ----------------------------------------------------------------------------------------------------------------
    def get_form_fields(player):
        # unzip list of form_fields from <letters_choices> list
        random.shuffle(player.participant.letters_choices)
        form_fields = [list(t) for t in zip(*player.participant.letters_choices)][1]
        return form_fields

    def vars_for_template(player):
        return{
            'choices': player.participant.letters_choices,
            'choices_0_10': player.participant.letters_choices[0:10],
            'choices_10_20': player.participant.letters_choices[10:20],
            'choices_20_30': player.participant.letters_choices[20:30],
            'choices_30_40': player.participant.letters_choices[30:40],
            'choices_40_50': player.participant.letters_choices[40:50],
            'choices_50_60': player.participant.letters_choices[50:60],
            'choices_60_70': player.participant.letters_choices[60:70],
            'choices_70_80': player.participant.letters_choices[70:80],
            'round_number': player.subsession.round_number,
            'total_letters': Constants.total_letters,
            'd_total': Constants.d_total,
            'b_total': Constants.d_total,
            'num_rounds': Constants.num_rounds,
            'fixed_payoff': Constants.fixed_payoff,
            'bonus_payoff': Constants.bonus_payoff
        }

    # set timer for the Trial Task
    # ----------------------------------------------------------------------------------------------------------------

    def get_timeout_seconds(player):
        return player.participant.expiry_timestamp - time.time()

    def is_displayed(player):
        return player.participant.expiry_timestamp - time.time() > 0

    # get the choice made in a given round
    # ----------------------------------------------------------------------------------------------------------------
    def before_next_page(player, timeout_happened):

        # unzip indices and form fields from <cem_choices> list

        round_number = player.subsession.round_number
        form_fields = [list(t) for t in zip(*player.participant.letters_choices)][1]
        indices = [list(t) for t in zip(*player.participant.letters_choices)][0]

        for j, choice in zip(indices, form_fields):
            choice_i = getattr(player, choice)
            player.participant.letters_choices_made[j - 1] = choice_i

        if player.participant.letters_choices_made is not None:
            player.count_effort()
            player.check_correctness()
        if player.round_number == 1:
            player.total_correct = player.correct
        elif player.round_number > 1:
            player.total_correct = player.in_round(
                round_number - 1).total_correct + player.in_round(player.round_number).correct


class ResultsWaitPage(WaitPage):
    vars_for_template = vars_for_all_templates


class ResultsTrial(Page):

    def is_displayed(player):
        return player.participant.expiry_timestamp - time.time() < 0 \
               and player.participant.endgame != 1

    def before_next_page(player, timeout_happened):
        player.update_endgame()

    def vars_for_template(player):
        table_rows = []
        for prev_player in player.in_all_rounds():
            row = {
                'round_number': prev_player.round_number,
                'd_crossed': round(prev_player.d_crossed),
                'b_crossed': round(prev_player.b_crossed),
                'is_correct': round(prev_player.is_correct),
            }
            table_rows.append(row)

        player.participant.t1_results = table_rows

        return {
            'table_rows': table_rows,
            'total_payoff': player.total_correct,
            'total_letters': Constants.total_letters,
            'd_total': Constants.d_total,
            'b_total': Constants.d_total,
            'num_rounds': Constants.num_rounds,
            'fixed_payoff': Constants.fixed_payoff,
            'bonus_payoff': Constants.bonus_payoff
        }


page_sequence = [
    Welcome,
    Demographics,
    Instructions,
    TaskTrial,
    ResultsTrial,
]