import math

class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(math.ceil(photos_count/4))

    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            for slot in range(4):

                if len(self.photos[page]) < 4:
                    self.photos[page].append(label)
                    
                    return f"{label} photo added successfully on page {page + 1} slot {slot + 1}"

        return "No more free slots"

    def display(self):
        result = "-----------\n"
        if len(self.photos) <= 0:
            result = []
        for sublist in self.photos:
            result += ("[] "*len(sublist)).rstrip()
            result += "\n-----------\n"

        return result


album = PhotoAlbum(0)

# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
print(album.display())

