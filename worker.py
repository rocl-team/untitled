from config.appconf import AppConf as conf
from logzero import logger
import multiprocessing as mp
from redis import Redis
from rq import Connection, Worker

redis_conn = Redis.from_url(conf.redis_url)

if __name__ == '__main__':
    motd = f"""This is a worker
    DATABASE URL: {conf.db_url}
    REDIS URL: {conf.redis_url}
    """
    logger.info(motd)
    queues = ['default','high','low']
    Worker(queues, connection=redis_conn).work(burst=False)
