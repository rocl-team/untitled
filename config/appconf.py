import os

class AppConf:
    db_url = os.environ.get('DATABASE_URL')
    redis_url = os.environ.get('REDIS_URL')
    rq_result_ttl = os.environ.get('RQ_RESULT_TTL') or 7*24*60*60
    rq_timeout = os.environ.get('RQ_TIMEOUT') or 30*60
    slack_callback = os.environ.get('SLACK_CALLBACK')
