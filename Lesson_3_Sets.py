# 1. Python Sets Adventure
# Objective: The aim of this assignment is to deepen your understanding and application of Python sets in various scenarios, ranging from basic operations to advanced manipulations and best practices. You will correct given codes, use sets in everyday contexts, and tackle challenges that require creative thinking and problem-solving.

# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# Destinations that both airlines fly to.
# Destinations unique to your airline.
# Whether there are any destinations that neither airline shares.
# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
all_possible_routes = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK", "ABC", "DEF", "GHI"}

import os

def clear ():
    os.system('cls' if os.name == 'nt' else 'clear')

def flight_intersection():
    intersect = our_routes.intersection(competitor_routes)
    print("Destinations both airlines fly to:", intersect)
    input("Press Enter to return to the main menu...")

def unique_destinations():
    unique_set = our_routes.difference(competitor_routes)
    print("Destinations unique to our airline:", unique_set)
    input("Press Enter to return to the main menu...")


def destinations_neither_airline():
    neither_set = all_possible_routes.difference(our_routes.union(competitor_routes))
    print("Destinations neither airline shares:", neither_set)
    input("Press Enter to return to the main menu...")


def main():
    while True:
        clear()
        ans = input('''
Welcome to the airline destinations app!

Please select one of the following:
1. Desitinations both airlines fly to
2. Destinations unique to our airline
3. Destinations neither airline shares
4. Quit

Please enter your selection (1-4): ''')
        if ans == '1':
            clear()
            flight_intersection()
        elif ans == '2':
            clear()
            unique_destinations()
        elif ans == '3':
            clear()
            destinations_neither_airline()
        elif ans == '4':
            print("Thanks for using our airlines app!")
            break
        else:
            print("Please enter a valid number.")

main()



# 2. Set Operations in Data Analysis

# Objective: The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.

# Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python function to remove duplicates and display the unique customer IDs.

# Example Code:

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# Expected Outcome: A set of unique customer IDs, ensuring no duplicates. For instance, {'C001', 'C002', 'C003', 'C004'}.

def unique_ids(ids):
    set_customer_ids = set(ids)
    list_customer_ids = list(set_customer_ids)
    list_customer_ids.sort()
    print(list_customer_ids)

unique_ids(customer_ids)
