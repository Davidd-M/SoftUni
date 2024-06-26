import os
from datetime import timedelta, date

import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Artist, Song, Product, Review, DrivingLicense, Driver, Owner, Registration, Car


def show_all_authors_with_their_books() -> str:
    authors_with_books = []
    authors = Author.objects.all().order_by('id')

    for author in authors:
        books = Book.objects.filter(author=author)

        if books:
            authors_with_books.append(f"{author.name} has written - {', '.join(b.title for b in books)}!")

    return '\n'.join(authors_with_books)


def delete_all_authors_without_books() -> None:
    Author.objects.filter(book__isnull=True).delete()


# # Create authors
# author1 = Author.objects.create(name="J.K. Rowling")
# author2 = Author.objects.create(name="George Orwell")
# author3 = Author.objects.create(name="Harper Lee")
# author4 = Author.objects.create(name="Mark Twain")
#
# # Create books associated with the authors
# book1 = Book.objects.create(
#     title="Harry Potter and the Philosopher's Stone",
#     price=19.99,
#     author=author1
# )
# book2 = Book.objects.create(
#     title="1984",
#     price=14.99,
#     author=author2
# )
#
# book3 = Book.objects.create(
#     title="To Kill a Mockingbird",
#     price=12.99,
#     author=author3
# )
#
# # Display authors and their books
# authors_with_books = show_all_authors_with_their_books()
# print(authors_with_books)

# # Delete authors without books
# delete_all_authors_without_books()
# print(Author.objects.count())


def add_song_to_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str) -> QuerySet[Song]:
    artist = Artist.objects.get(name=artist_name)
    return artist.songs.all().order_by("-id")


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


# # Create artists
# artist1 = Artist.objects.create(name="Daniel Di Angelo")
# artist2 = Artist.objects.create(name="Indila")
# # Create songs
# song1 = Song.objects.create(title="Lose Face")
# song2 = Song.objects.create(title="Tourner Dans Le Vide")
# song3 = Song.objects.create(title="Loyalty")
#
# # Add a song to an artist
# add_song_to_artist("Daniel Di Angelo", "Lose Face")
# add_song_to_artist("Daniel Di Angelo", "Loyalty")
# add_song_to_artist("Indila", "Tourner Dans Le Vide")
#
# # Get all songs by a specific artist
# songs = get_songs_by_artist("Daniel Di Angelo")
# for song in songs:
#     print(f"Daniel Di Angelo: {song.title}")
#
# # Get all songs by a specific artist
# songs = get_songs_by_artist("Indila")
# for song in songs:
#     print(f"Indila: {song.title}")
#
# # Remove a song from an artist
# remove_song_from_artist("Daniel Di Angelo", "Lose Face")
#
# # Check if the song is removed
# songs = get_songs_by_artist("Daniel Di Angelo")
#
# for song in songs:
#     print(f"Songs by Daniel Di Angelo after removal: {song.title}")


def calculate_average_rating_for_product_by_name(product_name: str) -> float:
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()
    total_sum = 0

    for review in reviews:
        total_sum += review.rating

    return total_sum / len(reviews)


def get_reviews_with_high_ratings(threshold: int) -> QuerySet:
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews() -> QuerySet[Product]:
    return Product.objects.filter(reviews__isnull=True).order_by("-name")


def delete_products_without_reviews() -> None:
    Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates() -> str:
    result = []

    for license_record in DrivingLicense.objects.order_by("-license_number"):
        exp_date = license_record.issue_date + timedelta(days=365)
        result.append(f'License with number: {license_record.license_number} expires on {exp_date}!')

    return '\n'.join(result)


def get_drivers_with_expired_licenses(due_date: date) -> [Driver]:
    due_date = due_date - timedelta(days=365)
    expired_licenses = Driver.objects.filter(license__issue_date__gt=due_date)

    return list(expired_licenses)


def register_car_by_owner(owner: Owner) -> str:
    free_reg = Registration.objects.filter(car__isnull=True).first()
    free_car = Car.objects.filter(registration__isnull=True).first()

    free_car.owner = owner
    free_car.registration = free_reg

    free_car.save()

    free_reg.car = free_car
    free_reg.registration_date = date.today()

    free_reg.save()

    return f"Successfully registered {free_car.model} to {free_car.owner.name} with registration number {free_reg.registration_number}."


# # Create owners
# owner1 = Owner.objects.create(name='Ivelin Milchev')
# owner2 = Owner.objects.create(name='Alice Smith')
#
# # Create cars
# car1 = Car.objects.create(model='Citroen C5', year=2004)
# car2 = Car.objects.create(model='Honda Civic', year=2021)
# # Create instances of the Registration model for the cars
# registration1 = Registration.objects.create(registration_number='TX0044XA')
# registration2 = Registration.objects.create(registration_number='XYZ789')

# print(register_car_by_owner(owner1))
