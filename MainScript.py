import csv
import math

# Read csv files for each operator
file = open("OperatorA.csv")
csvreader = csv.reader(file)
header = next(csvreader)
data_A = []
for row in csvreader:
    data_A.append(row)
file.close()

file = open("OperatorB.csv")
csvreader = csv.reader(file)
header = next(csvreader)
data_B = []
for row in csvreader:
    data_B.append(row)
file.close()

# print(data_A[0][0])

# Ask for an integer from the user through the terminal and repeat until the input is an actual integer
got_int = False
while (not(got_int)):
    try:
        num_given = int(input('Enter phone number in an integer form: '))
        got_int = True 
    except ValueError:
        print('Please only input digits')

# Find the length of the given integer
len_num = math.floor(math.log10(num_given))+1

counter = 0
extracted = num_given // (10 ** (len_num - counter - 1))

while counter < len_num:
    extracted = num_given // (10 ** (len_num - counter - 1))
    counter += 1