#!/usr/bin/env python3
""" View module for Classificator """
from app.controllers.mt_utils import classify_issue
from flask import render_template, jsonify


class Classificator(object):
    """ View handler for classification """
    def return_view(self, issue=None):
        """ Return classification page """
        if issue:
            classfication = classify_issue(issue)
            return render_template('classify.html', classifying_dict=classfication)
        else:
            return render_template('classify.html')


    def return_json_view(self, issue=None):
        """ Return json classification """
        if issue:
            classification = classify_issue(issue)
            return jsonify(classification)
        else:
            return jsonify({})
