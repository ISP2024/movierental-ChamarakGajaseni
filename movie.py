import logging
from abc import ABC, abstractmethod
class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2
    
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
            amount = 2.0
            if days > 2:
                amount += 1.5*(days-2)
        elif self.get_price_code() == Movie.CHILDRENS:
                # Three days for $1.50, additional days 1.50 per day.
            amount = 1.5
            if days > 3:
                amount += 1.5*(days-3)
        elif self.get_price_code() == Movie.NEW_RELEASE:
                # Straight $3 per day charge
            amount = 3*days
        else:
            log = logging.getLogger()
            log.error(f"Movie {self} has unrecognized priceCode {self.get_price_code()}")
        return amount
    
    def get_freq_renter_points(self, days):
        frequent_renter_points = 0
        if self.get_price_code() == Movie.NEW_RELEASE:
                # New release earns 1 point per day rented
            frequent_renter_points += days
        else:
                # Other rentals get only 1 point
            frequent_renter_points += 1
         
        return frequent_renter_points
    
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