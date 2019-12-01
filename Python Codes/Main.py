# Necessary libraries
import random
import random
from statistics import median
# Common functions
#import numpy as np
#import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
#from scipy import stats


# Class Population
class Population(object):


    def __init__(self, dimensions,activism):
        assert type(dimensions)==int and dimensions>0,"The first argument is not an acceptable input"
        assert type(activism)==float  and 0.0<activism<=1.0,"The third argument is not an acceptable input"
        self.dimensions = dimensions
        self.activism = activism
        self.members = []

    def __str__(self):
        if self.members == []:
            return "<0;" + str(self.dimensions) + "-D;" + str(self.activism * 100) + ">"
        else:
            med = []
            for i in range(self.dimensions):
                x = []
                for j in range(self.size):
                    x.append(j.policies[i])
                med.append(median(x))
            return "<" + str(self.size) + ";" + str(self.dimensions) + "-D; " + str(
                self.activism * 100) + ">. The median policy on each dimension are: " + str(med)

    def get_size(self):
        return self.size

    def get_activism(self):
        return self.size

    def get_dimensions(self):
        return self.dimensions

    def populate(self,size):
        assert type(size)==int and size>2,"The second argument is not an acceptable input"
        self.size = size
        Individual.reset_id()
        for i in range(self.size):
            i = Individual(self.dimensions, st_trunc_gauss(0.5))
            self.members.append(i)
        # return self.members

    def drift(self):
        return None


class Individual(Population):
    """
    The object holds each member of the Population
    :param:
    :insta:
    """
    id = 1

    def __init__(self, dimensions, involvement,activism, parent1=None, parent2=None):
        Population.__init__(self, dimensions, activism)
        self.involvement = involvement
        self.parent1 = parent1
        self.parent2 = parent2
        self.policies = []
        self.values = []
        self.id = Individual.id
        Individual.id += 1
        self.policies, self.values = self.birth()

    def __str__(self):
        return "<" + str(self.id) + ":" + str(self.dimensions) + ":" + str(self.involvement) + ":(" + str(
            self.parent1) + ":" + str(self.parent2) + ")>"

    def __add__(self, other):
        return Individual(self.dimensions,self.involvement, st_trunc_gauss(0.5), self, other)

    def get_involvement(self):
        return self.involvement

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def get_id(self):
        return str(self.id).zfill(4)

    def set_id(self, counter):
        self.id = counter

    def reset_id(self):
        Individual.id = 1

    def birth(self):
        if self.parent1 == None or self.parent2 == None:
            for i in range(self.dimensions):
                preference = st_trunc_gauss(0.5)
                self.policies.append(preference)
                if random.random() < self.involvement:
                    disutility = st_trunc_gauss(0.75)
                else:
                    disutility = st_trunc_gauss(0.25)
                self.values.append(disutility)
        else:
            for i in range(self.dimensions):
                preference = st_trunc_gauss((self.parent1.policies[i] + self.parent2.policies[i]) / 2 + random.random())
                self.policies.append(preference)
                disutility = st_trunc_gauss(0.5)
                self.values.append(disutility)
        return self.policies, self.values

    def update(self):
        old_id = self.get_id()
        self = Individual(self.dimensions, self.involvement, self, self)
        self.set_id(old_id)
        return self

A=Individual(3, 0.9, 0.5)
B=Individual(3, 0.9, 0.8)
C=A+B
C.update()