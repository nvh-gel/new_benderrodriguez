""" Queue object for bender """
import os
from app.models.mt_redis import MTRedis
from rq import Queue


class MTQueue(object):
    """ Class for handling queueing """
    _queue = None
    _async = False
    def get_queue(self, queuename=None):
        """ if queue is not set, set queue
        set async as environment variable in docker-compose.yml
        return queue """
        self._async = (True if os.environ['ASYNC'] == 1 else False)
        if not self._queue:
            self._queue = Queue(queuename, async=self._async, connection=MTRedis().get_redis())
        return self._queue

    def enqueue(self, task, *args, **kwargs):
        """ put a task on queue """
        if not self._queue:
            self.get_queue()
        self._queue.enqueue(task, args, kwargs)
