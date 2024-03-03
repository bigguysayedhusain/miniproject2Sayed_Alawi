# INF601 - Advanced Programming in Python
# Sayed Husain Alawi
# Mini Project 2


# TODO finish the README.md file
# TODO finish requirments.txt file


import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from dateutil.parser import parse

try:
    Path('charts').mkdir()
except FileExistsError:
    pass

netflix_movies = pd.read_csv("netflix_titles.csv", index_col=0)


########_____First Graph_____######
first_filter = netflix_movies.loc[(netflix_movies['country'] == 'India'), ['date_added']]
first_filter['date_added'] = first_filter['date_added'].apply(parse)
first_filter['date_added'] = first_filter['date_added'].dt.year
first_filter = first_filter['date_added'].groupby(first_filter['date_added']).size()


#     plt.xticks(range(1, 11, 1))
#     plt.axis((0, 11, (min(closing_prices_list) - 2), max(closing_prices_list) + 2))
first_filter.plot()
plt.title("Indian Movies Added to Netflix Per Year")
plt.xlabel('Years')
plt.ylabel('Number of Movies')
plt.grid(True)
plt.savefig(f'charts/Indian Movies.png')
plt.show()


########_____Second Graph_____######
