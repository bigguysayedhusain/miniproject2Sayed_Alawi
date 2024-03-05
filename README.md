### INF601 - Advanced Programming in Python
### Sayed Husain Alawi
### Mini Project 1


# Mini Project 1

## Description

This project utilizes Python, pandas, and Matplotlib to analyze the distribution of TV Shows and movies available on 
Netflix. The data is sourced from netflix_titles.csv, which contains detailed information on Netflix titles, including 
directors, cast, duration, genre, and more.The results of the analysis are shown to the users as graphs. Then, it 
automatically creates  a directory to save these graphs as PNG files using the Path function from the pathlib module and
matplotlib.

## Key Features
This project answers three questions:
* **How many Indian movies are added to Netflix per year?** By filtering titles based on their country of origin (India)
, this segment calculates and visualizes the number of Indian movies added to Netflix each year. This insight helps 
understand the growth of Indian content on the platform over time.
* **What is the total number of movies and shows currently available on Netflix?** This part of the analysis identifies 
the total number of movies and TV shows 
currently available on Netflix, offering a clear view of the platform's content balance. A bar chart visualizes the 
comparison, making it easy to see the proportion of each type.
* **What are the top five movie categories on Netflix?** This section explores the most popular movie genres on Netflix, 
determining the top five categories. The analysis is visualized through a pie chart, highlighting the relative share of 
each top category, providing a glimpse into Netflix's genre diversity.

## Getting Started

### Install requirements with pip

```
pip install -r requirement.txt
```

### Download the required dataset

```
https://www.kaggle.com/datasets/shivamb/netflix-shows?resource=download
```
1. Download the archive.zip file from the above link into your computer.
2. Unzip the file.
3. Copy the netflix_titles.csv file and paste at the top of the project (miniproject2Sayed_Alawi).
4. On the copy window, don't change the name, and just click Ok.

### Executing program

```
python main.py
```

## Authors

Contributors names and contact info

ex. Sayed Husain Alawi

## Version History

* 0.1
    * Initial Release

## License

This project is dedicated to the public domain under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. You can copy, modify, distribute, and perform the work, even for commercial purposes, all without asking permission. See the [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/) for more information.

## Acknowledgments

Inspiration, code snippets, etc.
* [Matplotlib](https://matplotlib.org/stable/tutorials/pyplot.html)
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/overview.html)