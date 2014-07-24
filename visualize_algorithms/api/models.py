from django.db import models

class AlgoResult(object):

    def __init__(self, steps):
        super(AlgoResult, self).__init__()
        self.steps = steps
