# Stack Overflow Developer Survey Analysis

## Table of Contents
  * [Installation](#installation)
  * [Motivation](#motivation)
  * [File Structure](#file-structure)
  * [Licensing, Authors, and Acknowledgement](#licensing--authors--and--acknowledgement)

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

## Motivation 

Data Science Nanodegree project 



## File Structure 

1. `survey-analysis.ipynb` - juypter notebook that contains my analysis of the 2019 Stack Overflow Developer 
Survey dataset
2. `survey_results_public.csv` - CSV file with main survey results, one respondent per row and 
one column per answer 
3. `survey_results_schema.csv` - CSV file with survey schema, i.e., the questions that correspond to 
each column name

## Licensing, Authors, and Acknowledgement

Data is directly taken from [StackOverflow](https://insights.stackoverflow.com/survey/) and licensed 
under the [ODbl license](https://opendatacommons.org/licenses/odbl/1.0/)

