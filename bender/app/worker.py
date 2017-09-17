#!/usr/bin/env python
""" Background bender worker """
import sys
from rq import Connection, Worker
from controllers.mt_redis_handler import get_redis


def main():
    """ Provide queue names to listen to as arguments to this script,
    similar to rq worker
    """
    with Connection(connection=get_redis()):
        queue_string = sys.argv[1:] or ['default']
        worker = Worker(queue_string)
        worker.work()


if __name__ == '__main__':
    main()
