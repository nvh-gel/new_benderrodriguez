from redis import Redis
from redis import exceptions
from mt_config import get_config_section


class MTRedis(object):
    _redis = None

    def get_redis(self):
        if not self._redis:
            redis_config = get_config_section('redis')
            self._redis = Redis(redis_config['host'], redis_config['port'])
        return self._redis
