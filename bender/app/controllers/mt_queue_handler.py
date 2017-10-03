""" handling queue task """
from app.models.mt_queue import MTQueue
# from rq import Queue


class MTQueueHandler(object):
    """ class handler for queued task """
    _queue = None
    _async = False

    def get_queue(self, queuename=None):
        """ if not exist, init queue, else, return queue """
        if not self._queue:
            self._queue = MTQueue(queuename)
        return self._queue

    def enqueue(self, task, *args, **kwargs):
        """ put task on queue """
        if not self._queue:
            self._queue = MTQueue()
        return self._queue.enqueue(task, args, kwargs)
