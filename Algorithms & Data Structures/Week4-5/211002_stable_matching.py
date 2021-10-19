"""
Assignment: Gale-Shapely Algorithm Implementation
"""

__author__ = "Irene Ann Iype"
__email__ = "irene.iype@fs-students.de"

import random as rd
import pandas as pd
from time import perf_counter_ns
import matplotlib.pyplot as plt


def return_index(list_, person):
    for i in range(len(list_)):
        if list_[i] == person:
            return i
    Exception('index out of range!!!!!!')


class Person:
    def __init__(self, name):
        self.name = name
        self.preference = None
        self.partner = None

    def __str__(self):
        return str(self.name)

    def set_preference(self, list_of_persons):
        self.preference = list_of_persons

    def show_preferences(self):
        """
        just prints out a persons preferences 
        """
        for pref in self.preference:
            print(pref)

        return 0

    def make_proposal(self):
        preferences = self.preference
        for pref in preferences:
            if pref is not None:
                next_choice = pref

                self.choose(next_choice)
                break

        return 0

    def choose(self, girl):

        if girl.partner is None:
            girl.partner = self
            self.partner = girl
        else:
            current_guy = girl.partner
            # loop through girls preference list to see which guy is better
            preferences = girl.preference
            current_guy_index = return_index(preferences, current_guy)
            potential_guy_index = return_index(preferences, self)

            if potential_guy_index > current_guy_index:
                # print(f'sorry, {self} has been rejected by {girl}')

                #     remove girl from guys list
                girl_index = return_index(self.preference, girl)
                self.preference[girl_index] = None
            else:
                # print(f'congratulations! {self} has been accepted by {girl}')

                # remove girl from prev guys list 
                girl_index = return_index(current_guy.preference, girl)
                current_guy.preference[girl_index] = None
                current_guy.partner = None

                # set girl up with new guy 
                self.partner = girl
                girl.partner = self

        return 0


def gale_shapely(proposers):
    while True:  # for each choice
        exit = 0
        for i in range(len(proposers)):  # go through each proposer
            if (proposers[i].partner is None):
                proposers[i].make_proposal()
                exit += 1

                # exit early if all engaged
        if exit == 0:
            break


def print_matches(proposers):
    # print matches after matching
    for proposer in proposers:
        print(f'({proposer}, {proposer.partner})')


def create_people(n):
    """
    function generates n number of proposers and acceptors of class Person randomly creates and sets preferences of each person

    n : number of proposers and acceptors to create
    return: 2 lists of randomly generated proposers and acceptors
    """
    proposers = []
    acceptors = []

    # creating proposers and acceptors according to num
    for i in range(n):
        accep = Person(f'Girl{i}')
        prop = Person(f'Guy{i}')

        proposers.append(prop)
        acceptors.append(accep)

    # creating preferences for each proposer -> by shuffling acceptors list
    for proposer in proposers:
        f_list = acceptors
        rd.shuffle(f_list)

        # set preferences 
        proposer.set_preference(f_list)

    # creating preferences for each acceptor -> by shuffling proposers list
    for acceptor in acceptors:
        m_list = proposers
        rd.shuffle(m_list)

        # set preferences 
        acceptor.set_preference(m_list)

    return (proposers, acceptors)


def plot_creator(df: pd.DataFrame):
    """
    Creates plot out of the DataFrame with array length on x-axis and duration in seconds on y axis
    :param df: DataFrame containing array length and duration of respective insertion sort
    :return: none
    """
    # Define the plot
    plt.style.use("bmh")
    fig, ax = plt.subplots()
    ax.plot(df["number"], df["time_taken"], label="gale shapely", marker="o", linestyle="-")

    # Prepare the labels and title
    ax.legend(loc="upper left")
    ax.set_xlabel("Number of pairs to match")
    ax.set_ylabel("Duration in nanoseconds")
    ax.set_title("Time complexity of gale-shapely algorithm")

    # Create plot and save it
    plt.show()
    # fig.savefig("assignment1_insertion_sort_time_complexity/figure_assigment_1")


def main():
    df = pd.DataFrame(columns=['number', 'time_taken'])

    sizes = [100, 200, 500, 1000, 2000, 5000, 10000, 20000]

    for i in range(len(sizes)):
        proposers, acceptors = create_people(sizes[i])

        start = perf_counter_ns()
        gale_shapely(proposers)
        end = perf_counter_ns()

        time = (end - start) / 1e6
        df.loc[i] = [sizes[i]] + [time]

    print(df)
    plot_creator(df)

    print(
        'Time complexity: From the graph plotted, we can see that it follows O(n^2). This is because the gale-shapely '
        'algorithm has a loop runing inside another loop - iterating through a loop in this case takes O(n) time so a nested loop (with each block in each loop taking O(1) time) would thus have a time complexity of O(n^2). ')


if __name__ == "__main__":
    main()
