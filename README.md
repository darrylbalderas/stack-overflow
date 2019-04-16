# Stack Overflow Developer Survey Analysis

## Table of Contents
1. [Motivation](#motivation)
2. [Installation](#installation)
3. [File Structure](#file-structure)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)
  

## Motivation <a name="motivation"></a>

For my analysis, I would like to take a further dive into the Stack Overflow Developers Survey dataset and understand the answers that my fellow Latinx/Black community gave in the survey

Questions that I would like to answer:

1. “How many survey entries were from a Latinx or Black race-ethnicity?”
2. “Which top 5 countries had the most amount of Latinx participants?”
3. “Which top 5 countries had the most amount of Black or of African descent participants?
4. “How much did the salary increase from 2017–2018 for Latinx and Black folks?”
5. “What was the increase percentage of Latinx/Black participants with Bachelors’, Masters and Postdoctoral degrees?”

## Installation <a name="installation"></a>

- Create a python3 virtual environment

    `python3 -m venv ./venv `

- Start virtual environment

    `source venv/bin/activate`

- Stop virtual environment

    `deactivate`

- Install project dependencies 

    > (virtual env must be started to install dependencies)
     
    `pip install -r requirements.txt`
    
- Start notebook 
     
    `jupyter notebook survey-analysis.ipynb`

## File Structure <a name="file-structure"></a>

1. `survey-analysis.ipynb` - juypter notebook that contains my analysis of the 2019 Stack Overflow Developer 
Survey dataset
2. `survey_results_public2017.csv` - CSV file with main 2017 survey results, one respondent per row and 
one column per answer 
3. `survey_results_public2018.csv` - CSV file with main 2018 survey results, one respondent per row and 
one column per answer 
4. `survey_results_schema.csv` - CSV file with survey schema, i.e., the questions that correspond to 
each column name

## Results <a name="results"></a>

The main findings of the code can be found at the post available [here](https://medium.com/@drrylbalderas/black-and-brown-in-the-flow-e17aa32876ea)


## Licensing, Authors, Acknowledgements <a name="licensing"></a>

Data is directly taken from [StackOverflow](https://insights.stackoverflow.com/survey/) and licensed 
under the [ODbl license](https://opendatacommons.org/licenses/odbl/1.0/)
