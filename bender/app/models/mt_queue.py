""" Queue object for bender """
import os
from app.models.mt_redis import MTRedis
from rq import Queue


class MTQueue(object):
    """ Class for handling queueing """
    _queue = None
    _async = False
    def get_queue(self):
        """ if queue is not set, set queue
        set async as environment variable in docker-compose.yml
        return queue """
        if not self._queue:
            self._queue = Queue(connection=MTRedis().get_redis())
        self._async = (True if os.environ['ASYNC'] == 1 else False)
        return self._queue
