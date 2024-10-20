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
    
    def get_rental_points(self, days):
        """other rentals earn 1 point for each day rented."""     
        return 1
    
    def get_price(self, days):
        # Three days for $1.50, additional days 1.50 per day.
        amount = 1.5
        if days > 3:
            amount += 1.5*(days-3)
        return amount