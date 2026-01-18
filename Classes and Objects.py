
# classes and objects

#Classes are blueprints
#Objects are the actual things you built
#variables => attributes
#functions => methods


class Movie:
    def __init__(self,title,year,imdb_score,have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen

film_1 = Movie("Life of Brain",1979,8.1,True)
film_2 = Movie("The Holy Grail",1999,8.2,True)


print(film_1.title,film_1.year)
print(film_2.title,film_2.year)



