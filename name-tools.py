# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 02:22:55 2020

@author: Morgan
"""
class Name(object):
    def __init__(self, name):
        '''
        Initializes a Name object.
        
        name (string): A name, provided as a string
        
        A Name object has two attributes:
            self.name (string, the name, placed in lowercase and stripped 
            of newline characters.)
            self.alpha_values (dict, a list of alphabetical characters with 
            values as ints)
        '''
        self.name = name.lower().strip()
        self.alpha_values = { 'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
                             'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,
                             'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,
                             'w':23,'x':24,'y':25,'z':26, ' ': 0 }
        
    def get_sum(self):
        '''
        Used to find a sum of letters in the Name object.
        
        Returns: An int, representing the sum of the Name object.
        '''
        name_sum = 0
        for char in self.name:
            name_sum += self.alpha_values[char]
        return name_sum
    
    def get_avg(self):
        '''
        Used to find the average of the letters in the Name object.
        
        Returns: A float with up to one sigfig representing the average values
        in the Name object.
        '''
        return (round(self.get_sum()/len(self.name),1))
    
def average_name_finder(filename, value):
    ''' Takes a file containing a list of names as lines separated by a break.
    Returns a list of all names within file whose average value averages value,
    where each character in the alphabet is valued according to its relative
    position within the alphabet.
    
    filename (file): A file containing a list of names
    value (float): A float of up to one sig figs representing an average
    value to be found for the names
    
    Returns: A list of all names whose average value is equal to value
    '''
    
    match_names = []
    
    name_file = open(filename, 'r')
    names = name_file.read().lower().splitlines()
    
    for name in names:
        TestName = Name(name)
        if TestName.get_avg() == value:
            match_names.append(name)
    
    return match_names

def sum_name_finder(filename, value):
    ''' Takes a file containing a list of names as lines separated by a break.
    Returns a list of all names within file whose sum value equals value,
    where each character in the alphabet is valued according to its relative
    position within the alphabet.
    
    filename (file): A file containing a list of names
    value (int): An int representing a sum to be found for each name.
    
    Returns: A list of all names whose value is equal to value
    '''
    
    match_names = []
    
    name_file = open(filename, 'r')
    names = name_file.read().lower().splitlines()
    
    for name in names:
        TestName = Name(name)
        if TestName.get_sum() == value:
            match_names.append(name)
    
    return match_names