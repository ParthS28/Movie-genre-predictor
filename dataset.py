import numpy as np
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import re, csv

dataset = pd.read_csv('movies.csv', skipinitialspace=True)

data = dataset.to_dict("records")

movies = []

# Iterate through original dataset and add valid records
for movie in data:
    try:
        tid = str(movie["tid"])
        url = str(movie["url"])
        year = int(movie["year"])
        action = bool(movie["Action"])
        scifi = bool(movie["SciFi"])
        drama = bool(movie["Drama"])
        romance = bool(movie["Romance"])
    except:
        continue
    if url.find("http") != -1 and year > 2000 and (action or scifi or romance or drama):
        movies.append({"tid": tid, "title": movie["title"], "url": movie["url"], "year": movie["year"], "action": action, "scifi": scifi, "drama": drama, "romance": romance})


# Write the title of each columns
with open('movie_poster.csv', 'w', newline='') as out_csv:
    writer = csv.writer(out_csv, delimiter=',')
    writer.writerow(["tid", "title", "url", "image_url", "year", "action", "scifi", "drama", "romance"])


# Fetch all the movie posters and and name by scraping IMDB
for movie in movies:
        tid = str(movie["tid"])
        url = str(movie["url"])
        year = int(movie["year"])
        action = bool(movie["action"])
        scifi = bool(movie["scifi"])
        drama = bool(movie["drama"])
        romance = bool(movie["romance"])
        print(url, end = " ")
        try:
            with urllib.request.urlopen(url) as response:
                html = response.read()
                soup = BeautifulSoup(html, 'html.parser')
                # Get url of poster image
                title_tag = soup.find("div", class_="title_wrapper").findChild().text
                title = re.sub("\([^)]*\)", "", title_tag)
                print(title, end = " ")
                try:
                    image_url = soup.find('div', class_='poster').a.img['src']
                    extension = '.jpg'
                    image_url = ''.join(image_url.partition('_')[0]) + extension
                    filename = 'posters/' + tid + extension
                    with urllib.request.urlopen(image_url) as response:
                        with open(filename, 'wb') as out_image:
                            out_image.write(response.read())
    
                        with open('movie_poster.csv', 'a', newline='') as out_csv:
                            writer = csv.writer(out_csv, delimiter=',')
                            writer.writerow([tid, title, url, image_url, year, action, scifi, drama, romance])
                    print("Success")
                # Ignore cases where no poster image is present
                except AttributeError:
                    pass
        except urllib.error.HTTPError as e:
            print("\n\
=============================================================================\n\
    An ERROR has occured.\n\
    Please contact your mentor and send them a screenshot of the error\n\
=============================================================================\n")
            input("Press ENTER to continue")
