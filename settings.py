from os import environ

SESSION_CONFIGS = [
    dict(
        name='preferential_selection',
        app_sequence=[
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
#            'LabIds',
            'demographics',
            'main_experiment'
        ],
        num_demo_participants=2,
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

PARTICIPANT_FIELDS = [ 'p_gender' ]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '9272369364628'
