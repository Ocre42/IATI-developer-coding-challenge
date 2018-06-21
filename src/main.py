import csv
import math
import date

filename = "tests/sample_data_fully_valid_10_rows.csv"

def run():
	while(True):
		year = str(input('Please input a year (YYYY):'))
		try:
			if(valid_year(int(year))):
				break
		except ValueError:
			#Make sure the input is an integer
			print('Input must be a number in YYYY format')
			continue
	get_total_budget_value(filename, year)

def valid_year(n):
	#Make sure the input is a positive number and follows the YYYY format (4 digits, not negative)
	if n>0 and int(math.log10(n))+1 == 4:
		return True
	else:
		print("Input must be in YYYY format")
		return False

def get_total_budget_value(csv_filepath, year):
    """Compute the total USD value of projects for the input year.

    Args:
        csv_filepath (str): A path to a CSV file containing three columns: project-id; start-date; total-budget-value-usd.
        year (int): A value corresponding to a year.

    Returns:
        (float) The USD value of projects that start in the given year
    """

if __name__ == '__main__':
	run()