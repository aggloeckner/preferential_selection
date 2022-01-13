from os import environ

SESSION_CONFIGS = [
    dict(
        name='real_effort_task',
        app_sequence=[
#            'informed_consent_online',
#            'LabIds',
            'realefforttask',
        ],
        num_demo_participants=1,
        max_number_participants=2000,
    ),
    dict(
        name='preferential_selection',
        app_sequence=[
            'informed_consent_lab',
            'LabIds',
            'demographics',
            'main_experiment'
        ],
        num_demo_participants=5,
        max_number_participants=2000,
    ),
    dict(
        name='test',
        app_sequence=[
#            'informed_consent_lab',
#            'LabIds',
            'demographics',
            'main_experiment'
        ],
        num_demo_participants=10,
        max_number_participants=2000,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [ 'p_gender', 'letters_choices', 't1_results', 'expiry_timestamp', 'endgame', 'letters_choices_made', 'letters_choices' ]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '9272369364628'
