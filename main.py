import csv
from matplotlib import pyplot as plt


# Create an empty dict
population_per_continent = {}

filename = r'data.csv'

with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)