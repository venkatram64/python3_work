from my_db.model.base import Session
from my_db.model.Actor import Actor
from my_db.model.ContactDetails import ContactDetails
from my_db.model.Movie import Movie
from datetime import date

def fetch_data():
    session = Session()
    movies = session.query(Movie).all()

    for movie in movies:
        print(f'{movie.title} was released on {movie.release_date}')

    print('***** ')

    movies = session.query(Movie).filter(Movie.release_date > date(2015, 1, 1)) \
        .all()

    print('Recent movies: ')

    for movie in movies:
        print(f'{movie.title} was released after 2015')

    print('***** ')

    # 6 - movies that Dwayne Johnson participated
    the_rock_movies = session.query(Movie) \
        .join(Actor, Movie.actors) \
        .filter(Actor.name == 'Dwayne Johnson') \
        .all()

    print('### Dwayne Johnson movies:')
    for movie in the_rock_movies:
        print(f'The Rock starred in {movie.title}')
    print('')

    # 7 - get actors that have house in Glendale
    glendale_stars = session.query(Actor) \
        .join(ContactDetails) \
        .filter(ContactDetails.address.ilike('%glendale%')) \
        .all()

    print('### Actors that live in Glendale:')
    for actor in glendale_stars:
        print(f'{actor.name} has a house in Glendale')
    print('')


if __name__ == '__main__':
    fetch_data()