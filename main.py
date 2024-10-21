# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer

def make_movies_and_price_code():
    """Some sample movies."""
    movies = [
        [Movie("Air"), Rental.NEW_RELEASE],
        [Movie("Oppenheimer"), Rental.REGULAR],
        [Movie("Frozen"), Rental.CHILDRENS],
        [Movie("Bitconned"), Rental.NEW_RELEASE],
        [Movie("Particle Fever"), Rental.REGULAR]
    ]
    return movies

if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies_and_price_code():
        customer.add_rental(Rental(movie[0], days, movie[1]))
        days = (days + 2) % 5 + 1
    print(customer.statement())
