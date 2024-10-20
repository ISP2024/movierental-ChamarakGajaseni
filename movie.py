import logging
from abc import ABC, abstractmethod

class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass
    
    # _instance = None

    # @classmethod
    # def __new__(cls):
    #     if not cls._instance:
    #         cls._instance = super(PriceStrategy, cls).__new__(cls)
    #     return cls._instance
    
class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_rental_points(self, days):
        """New release rentals earn 1 point for each day rented."""
        return days
    
    def get_price(self, days):
        return 3*days
    
class RegularPrice(PriceStrategy):
    
    def get_rental_points(self, days):
        """New release rentals earn 1 point for each day rented."""
        return 1
    
    def get_price(self, days):
        amount = 2.0
        if days > 2:
            amount += 1.5*(days-2)
        return amount
    
class ChildrensPrice(PriceStrategy):
    
    def get_rental_points(self):
        """other rentals earn 1 point for each day rented."""     
        return 1
    
    def get_price(self, days):
        # Three days for $1.50, additional days 1.50 per day.
        amount = 1.5
        if days > 3:
            amount += 1.5*(days-3)
        return amount

class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = RegularPrice()
    NEW_RELEASE = NewRelease()
    CHILDRENS = ChildrensPrice()
    
    def __init__(self, title, price_code):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code
    
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title

    def get_price(self,days):
        amount = 0
        if self.get_price_code() == Movie.REGULAR:
                # Two days for $2, additional days 1.50 per day.
            amount = Movie.REGULAR.get_price(days)
        elif self.get_price_code() == Movie.CHILDRENS:
                # Three days for $1.50, additional days 1.50 per day.
            amount = Movie.CHILDRENS.get_price(days)
        elif self.get_price_code() == Movie.NEW_RELEASE:
                # Straight $3 per day charge
            amount = Movie.NEW_RELEASE.get_price(days)
        else:
            log = logging.getLogger()
            log.error(f"Movie {self} has unrecognized priceCode {self.get_price_code()}")
        return amount
    
    def get_rental_points(self, days):
        frequent_renter_points = 0
        if self.get_price_code() == Movie.NEW_RELEASE:
                # New release earns 1 point per day rented
            frequent_renter_points += Movie.NEW_RELEASE.get_rental_points(days)
        else:
                # Other rentals get only 1 point
            frequent_renter_points += Movie.REGULAR.get_rental_points(days)
         
        return frequent_renter_points
