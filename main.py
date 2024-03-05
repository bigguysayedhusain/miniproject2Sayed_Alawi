# INF601 - Advanced Programming in Python
# Sayed Husain Alawi
# Mini Project 2

# TODO finish requirements.txt file


import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from dateutil.parser import parse

try:
    Path('charts').mkdir()
except FileExistsError:
    pass

netflix_movies = pd.read_csv("netflix_titles.csv", index_col=0)


########_First Graph - How many Indian movies are added to Netflix per year?_######

first_filter = netflix_movies.loc[(netflix_movies['country'] == 'India'), ['date_added']]
first_filter['date_added'] = first_filter['date_added'].apply(parse)
first_filter['date_added'] = first_filter['date_added'].dt.year
first_filter = first_filter['date_added'].groupby(first_filter['date_added']).size()

first_filter.plot()
plt.title("Indian Movies Added to Netflix Per Year")
plt.xlabel('Years')
plt.ylabel('Number of Movies')
plt.grid(True)
# plt.savefig(f'charts/Indian Movies.png') TODO add it back
plt.show()


########_Second Graph - What is the total number of movies and shows currently available on Netflix?_######

second_filter = netflix_movies['type'].value_counts()

second_filter.plot.bar(color=['blue', 'red'])
plt.title("Number of Shows & Movies on Netflix")
plt.ylabel('Number of Movies')
plt.show()


########_Third Graph - What are the top five movie categories on Netflix?_######

third_filter = netflix_movies.loc[(netflix_movies['type'] == 'Movie'), ['listed_in']]
third_filter = third_filter['listed_in'].str.split(', ').explode()
third_filter = third_filter.value_counts()

third_filter.head().plot.pie(autopct='%1.1f%%', explode=(0.1, 0.03, 0.03, 0.03, 0.03))
plt.title("Top Five Movie Categories in Netflix")
plt.ylabel('')
plt.show()
