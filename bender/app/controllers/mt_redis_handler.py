from models.mt_redis import MTRedis

REDIS = None

def get_redis():
    global REDIS
    REDIS = MTRedis()
    return REDIS.get_redis()
