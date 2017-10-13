#!/usr/bin/env python3
""" Abstract view handler """


class AbstractView(object):
    """ Abstract class for view """
    def return_view(self, *args, **kwargs):
        """ default view """
        raise NotImplementedError

    def return_json_view(self, *args, **kwargs):
        """ json view """
        raise NotImplementedError
