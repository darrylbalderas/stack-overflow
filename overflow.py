import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

def is_latinx_or_black(ethnicities):
    """
    Checks if Latinx or Black was provided by the developer
    in their list of race-ethnicities
    """
    return 'Hispanic or Latino/Latina' in ethnicities or 'Black or of African descent' in ethnicities


def is_black(ethnicities):
    """
    Checks if Black or of African descent was provided by the developer
    in their list of race-ethnicities
    """
    return not 'Hispanic or Latino/Latina' in ethnicities and 'Black or of African descent' in ethnicities


def is_latinx(ethnicities):
    """
    Checks if Latinx and not Black was provided by the developer
    in their list of race-ethnicities
    """
    return 'Hispanic or Latino/Latina' in ethnicities and not 'Black or of African descent' in ethnicities


def is_latinx_and_black(ethnicities):
    """
    Checks if only Latinx and Black was provided by the developer
    in their list of race-ethnicities
    """
    return 'Hispanic or Latino/Latina' in ethnicities and 'Black or of African descent' in ethnicities


def get_indexes(df, column, conditional):
    """
    Gets a list of index based on the conditional for a
    specific column
    """
    indexes = []
    for idx in range(df.shape[0]):
        try:
            multi_answers = [answer.strip() for answer in df[column][idx].split(";")]
            if conditional(multi_answers):
                indexes.append(idx)
        except Exception as e:
            continue
    return indexes


def remove_outliers(df, column):
    """
    Removes outliers for numerical columns in a dataframe
    """
    first_qt, third_qt = np.percentile(df[column], [25, 75])
    iqr = third_qt - first_qt
    criteria = df[column] >  (first_qt - (1.5 * iqr))
    criteria2 = df[column] < (third_qt + (1.5 * iqr))
    return df[criteria & criteria2]


def get_education_degrees(education_counts, educations):
    """
    Gets a map count of the formal educations that was provided in the survey
    """
    education_degrees = defaultdict(int)
    for e in educations:
        for idx in education_counts.index:
            if idx in educations[e]:
                education_degrees[e] =  education_counts[idx]
    return education_degrees


def clean_multi_answers(df, index_name, column_name):
    """
    Returns a dataframe that contains the value
    count for a given column
    """
    def total_count(df, index_name, column_name):
        new_df = df[column_name].value_counts().reset_index()
        new_df.rename(columns={'index': index_name, column_name: 'count'}, inplace=True)
        counts = defaultdict(int)
        for answer in parse_multi_answer(df, column_name):
            for idx in range(new_df.shape[0]):
                developer_answers = [entry.strip() for entry in new_df[index_name][idx].split(";")]
                if answer in developer_answers:
                    counts[answer] += int(new_df['count'][idx])
        counts = pd.DataFrame(pd.Series(counts)).reset_index()
        counts.columns = [index_name, 'count']
        counts.sort_values('count', ascending=False, inplace=True)
        return counts

    answer_df = total_count(df, index_name, column_name)
    answer_df.set_index(index_name, inplace=True)
    return answer_df



def parse_multi_answer(df, column):
    """
    Returns a set of the answers that were separated by a semi-colon
    """
    answers = set()
    for idx in df[df[column].notnull()].index:
        for entry in df[column].iloc[idx].split(';'):
            answers.add(entry.strip())
    return answers


def plot_race_distribution(df, title, color='red'):
    """
    Plots and saves figure that shows race-ethnicities entry counts that
    were given in the Stack Overflow Developer Survey
    """
    f, ax = plt.subplots(figsize=(10, 10))
    races = list(df.index)[::-1]
    counts = df['count'].values[::-1] / df.sum().values
    ax.barh(races, counts, 0.35, color=color)
    ax.set_title(title)
    ax.set_ylabel('Race')
    ax.set_xlabel('Survey Entrees Percentage')
    plt.savefig('race-ethnicities', bbox_inches='tight')
    plt.show()


def get_total_latinx_black_count(df):
    """
    Returns a count of entries that were from a latinx or black race ethnicity
    """
    latinx_black = df.index.isin(['Hispanic or Latino/Latina', 'Black or of African descent'])
    return np.sum(df[latinx_black].values)


def display_statistics(df, count, year):
    """
    Displays count of entries that were from a latinx or black race ethnicity
    And latinx or black entry percentage
    """
    percentage = (count / np.sum(df.values)) * 100
    print("\n{} individuals reported as Latinx/Black participated in the {} Stack Overflow Developer survey".format(count, year))
    print("Latinx/Black account for {:0.3f}% of the {} Stack Overflow survey participants".format(percentage, year))


def plot_countries_ethnicities(df, df1, conditional, title, title2, color, num_countries):
    """
    Plots bar graphs for two dataframes to show how many latinx or black folks are
    in various countries
    """
    data_2017 = df.loc[get_indexes(df, "Race", conditional), :].reset_index()
    data_2017['Country'].value_counts()[:num_countries][::-1].plot(kind="barh",
                                                title=title,
                                                color=color)
    plt.show()
    data_2018 = df1.loc[get_indexes(df1, "RaceEthnicity", conditional), :].reset_index()
    data_2018['Country'].value_counts()[:num_countries][::-1].plot(kind="barh",
                                                title=title2,
                                                color=color)


def get_salary_dataframe(df, race_col, salary_col):
    """
    Returns a dataframe that contains descriptive statistics in regards to salary
    """
    salary_df = df.loc[get_indexes(df, race_col, is_latinx_or_black), :].reset_index()
    salary_df = salary_df[salary_df[salary_col].notnull()]
    return remove_outliers(salary_df, salary_col)[salary_col].describe()