import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie

class CustomerTest(unittest.TestCase): 
    """ Tests of the Customer class"""
    
    def setUp(self):
        """Test fixture contains:
        
        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
        self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
        self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)
        

    def test_billing(self):
        movies = [
        self.new_movie,
        self.regular_movie,
        self.childrens_movie,
        self.new_movie,
        self.regular_movie
        ]
        days = 1
        for movie in movies:
            self.c.add_rental(Rental(movie, days))
            days = (days + 2) % 5 + 1
            
        self.assertEqual(28.00,self.c.get_total())
        self.assertEqual(9 ,self.c.get_total_rental_points())
    
    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4)) # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
