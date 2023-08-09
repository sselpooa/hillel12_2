import os
import string
from titles import films_titles
from awards import films_awards

# Крок 1
path = os.getcwd()
if not os.path.exists('Harry Potter'):
    os.mkdir('Harry Potter')

os.chdir('Harry Potter')

for film in films_titles['results']:
    title = film['title']
    title = title.replace(':', '').strip()
    title_dir = os.path.join(os.getcwd(), title)

    if not os.path.exists(title_dir):
        os.mkdir(title_dir)
    #Krok 2
    for letter in string.ascii_uppercase:
        letter_dir = os.path.join(title_dir, letter)
        if not os.path.exists(letter_dir):
            os.mkdir(letter_dir)
    #Krok 3
    film_awards = []
    for results in films_awards:
        for movie in results["results"]:
            if movie["movie"]["title"] == title:
                film_award = {
                    "type": movie["type"],
                    "award_name": movie["award_name"],
                    "award": movie["award"],
                }
                film_awards.append(film_award)
    #Krok 4
            film_awards_sorted = sorted(film_awards, key=lambda award: award['award_name'])

            # Крок 5
            for award in film_awards_sorted:
                file_path = os.path.join(title, award['award_name'][0].upper(), f"{award['award_name']}.txt")
                with open(file_path, "w", encoding="utf-8"):
                    pass

            # Крок 6
            for award in film_awards_sorted:
                file_path = os.path.join(title, award['award_name'][0].upper(), f"{award['award_name']}.txt")
                with open(file_path, "a", encoding="utf-8") as file_obj:
                    file_obj.write(f"{award['award']}\n")


