import random
import math
class human():
    def __init__(self,is_knight):
        self.is_knight = is_knight
    def get_is_knight(self):
        return self.is_knight
    def set_is_knight(self,is_knight):
        self.is_knight = is_knight
    def __repr__(self):
        return(str(self.is_knight))

number_of_humans = random.randint(3, 50)
half = number_of_humans//2 + 1
number_of_knights = random.randint(half, 50)
number_of_liars = number_of_humans - number_of_knights
