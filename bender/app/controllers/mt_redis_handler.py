""" Handle redis connection """
from models.mt_redis import MTRedis


REDIS = None


def get_redis():
    """ Return redis connection """
    global REDIS
    REDIS = MTRedis()
    return REDIS.get_redis()
