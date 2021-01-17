import requests
import json
import os

def get_movie(query):
  request_string = "https://api.themoviedb.org/3/search/movie?api_key="+os.getenv('TMDB_KEY')+"&language=en-US&query="+str(query)
  print(request_string)
  response = requests.get(request_string)
  json_data = json.loads(response.text)
  results = json_data['results']
  movies = ""
  for result in results:
    title = result['original_title']
    movies = movies + title
    try:
      releaseDate = result['release_date']
      movies = movies + "(" +releaseDate+ ")"
    except:
      movies = movies + "(no release date info)"
    movies = movies + "\n"
  if json_data['page']<json_data['total_pages']:
    movies = movies + "..\n..try refine search ko."
  return(movies)


