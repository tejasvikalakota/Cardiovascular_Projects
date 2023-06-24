#Author:Tejasvi Kalakota
import statistics
'''Inhertiance is used here because I made the
mean median and mode class inheirt from the parent class statistics'''
class Statistic:
    def __init__(self, data):
        self.data = data

    def calculate(self):
        pass

class Mean(Statistic):
    def calculate(self):
        return statistics.mean(self.data)

class Median(Statistic):
    def calculate(self):
        return statistics.median(self.data)

class Mode(Statistic):
    def calculate(self):
        return statistics.mode(self.data)


