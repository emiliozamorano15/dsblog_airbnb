Boston's Red Sox vs Seattle's Mariners as told by Airbnb
==============================

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

The libraries used to run the code are:
- jupyterlab 3.0.12
- matplotlib 3.4.1
- numpy 1.19.2
- pandas 1.2.3
- scikit-learn 0.21.3
- seaborn 0.11.1

## Project Motivation<a name="motivation"></a>

This project was developed as part of the requirements for Udacity's Data Science Nanodegree Program.
It takes a look at Airbnb Data of listings from Boston and Seattle between 2016 and 2017. The main questions
addressed here are:

1.	What is the effect of time on listing price both in Seattle and in Boston? Is this effect different on each city?
2.	Is there any difference in the amenities offered in Boston vs. Seattle?
3.	Do amenities have an impact on the bookability of a listing and if so, how different is it on each city?


## File Descriptions <a name="files"></a>

    ├── LICENSE
    ├── README.md           <- The top-level README for developers using this project.
    ├── data			    <- Data used in the notebooks.
    │   ├── boston_calendar.csv
    │   ├── boston_listings.csv
    │   ├── seattle_calendar.csv
    │   ├── seattle_listings.csv
    ├── notebooks           <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── requirements.txt    <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── src                 <- Source code for use in this project.
    │   ├── config          <- Scripts for general project setup
    │   │   └── config.py
    │   ├── data            <- functions for data exploration
    │   │   └── __init__.py

## Results<a name="results"></a>

The main findings of the code can be found at the post available [here](https://emiliozamoranodeacha.medium.com/bostons-red-sox-vs-seattle-s-mariners-as-told-by-airbnb-3a7816ca363f).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to Airbnb and Kaggle for the data.  
The Licensing for the data and other descriptive information can be found at the 
following Kaggle links available [here](https://www.kaggle.com/airbnb/seattle/data)
and [here](https://www.kaggle.com/airbnb/boston)