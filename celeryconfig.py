BROKER_URL = 'amqp://celeryuser:celery@localhost:5672/celeryvhost'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

CELERY_IMPORTS = ('tasks', )