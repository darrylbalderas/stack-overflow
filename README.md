# Stack Overflow Developer Survey Analysis

## Table of Contents
  * [Motivation](#motivation)
  * [Installation](#installation)
  * [Start Project](#Start)
  * [File Structure](#file-structure)
  * [Licensing, Authors, and Acknowledgement](#licensing--authors--and--acknowledgement)
  * [Medium Post](#Medium Post)

## Motivation 

   Data Science Nanodegree project to showcase my application of CRISP-DM standard

## Installation

- Create a python3 virtual environment

    `python3 -m venv ./venv `

- Start virtual environment

    `source venv/bin/activate`

- Stop virtual environment

    `deactivate`

- Install project dependencies 

    > (virtual env must be started to install dependencies)
     
    `pip install -r requirements.txt`

## Start

- Install project dependencies 
     
    `jupyter notebook survey-analysis.ipynb`

## File Structure 

1. `survey-analysis.ipynb` - juypter notebook that contains my analysis of the 2019 Stack Overflow Developer 
Survey dataset
2. `survey_results_public2017.csv` - CSV file with main 2017 survey results, one respondent per row and 
one column per answer 
3. `survey_results_public2018.csv` - CSV file with main 2018 survey results, one respondent per row and 
one column per answer 
4. `survey_results_schema.csv` - CSV file with survey schema, i.e., the questions that correspond to 
each column name

## Licensing, Authors, and Acknowledgement

Data is directly taken from [StackOverflow](https://insights.stackoverflow.com/survey/) and licensed 
under the [ODbl license](https://opendatacommons.org/licenses/odbl/1.0/)

## Medium Post

Here is the link to the [post](https://medium.com/@drrylbalderas/black-and-brown-in-the-flow-e17aa32876ea)

