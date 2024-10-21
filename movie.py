import logging
from abc import ABC, abstractmethod
from pricing import *


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    # REGULAR = RegularPrice()
    # NEW_RELEASE = NewRelease()
    # CHILDRENS = ChildrensPrice()
    
    def __init__(self, title):
        # Initialize a new movie. 
        self.title = title
    
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title

    # def get_price(self,days):
    #      return self.price_code.get_price(days)
    
    # def get_rental_points(self, days):
    #     return self.price_code.get_rental_points(days)
