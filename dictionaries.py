
movie  = {
    'title' : 'Life of brain',
    'year' : 1999,
    'cast' : ['sush']
}

for key, value in movie.items():
    print(key, value)
print(movie.values())
print(movie.items())

movie.update({'title' :'Dhammal','year' : 2006,})
year = movie.pop('year')
#del movie['cast']
movie['budget'] = 250000
print(movie)
print(year)