import os

class AppConf:
    db_url = os.environ.get('DATABASE_URL') or 'postgres://127.0.0.1/postgres'
    redis_url = os.environ.get('REDIS_URL') or 'redis://127.0.0.1:6379/'
    rq_result_ttl = os.environ.get('RQ_RESULT_TTL') or 7*24*60*60
    rq_timeout = os.environ.get('RQ_TIMEOUT') or 30*60
    slack_callback = os.environ.get('SLACK_CALLBACK')
