import csv
import math

initial_prefix = 111111111 # A number that cannot be a prefix

# Read csv files for each operator
# For Operator A
file = open("OperatorA.csv")
csvreader = csv.reader(file)
header = next(csvreader)
data_A = []
for row in csvreader:
    data_A.append(row)
file.close()

# For Operator B
file = open("OperatorB.csv")
csvreader = csv.reader(file)
header = next(csvreader)
data_B = []
for row in csvreader:
    data_B.append(row)
file.close()

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

# Initialise some variables
prefix_A = initial_prefix   # For saving the prefix for each operator
prefix_B = initial_prefix

cost_A = -1 # For saving the price for each operator for the corresponding prefix
cost_B = -1

oper_A_Flag = True  # For checking if there is a match in the csv files with the integer given by the user
oper_B_Flag = True

count_A_previous = -1   # For checking if there is still a match between two iterations in the row
count_A_cur = -1
count_B_previous = -1
count_B_cur = -1

counter = 0
extracted = num_given // (10 ** (len_num - counter - 1))    # Get the first number of the integer given

while (counter <= len_num) and (oper_A_Flag or oper_B_Flag):
    # For checking if there is still a match between two iterations in the row
    count_A_previous = count_A_cur
    count_A_cur = 0
    count_B_previous = count_B_cur
    count_B_cur = 0

    # add the next digit of the integer given in the variable extracted
    extracted = num_given // (10 ** (len_num - counter - 1))

    # For Operator A
    for i in range(0,len(data_A)):
        len_A = math.floor(math.log10(int(data_A[i][0])))+1  
        if(len_A > counter):    # Proceed only for entries whose length is bigger than the length of the extracted part of the nubmer given
            oper_num_A = int(data_A[i][0]) // (10 ** (len_A - counter - 1))
            if(oper_num_A == extracted):
                count_A_cur += 1
                if(len_A == math.floor(math.log10(extracted))+1):   # If there is a match, save the prefix, the price and skip the rest of the csv entries
                    prefix_A = data_A[i][0]
                    cost_A = float(data_A[i][1])
                    break

    if((count_A_cur == 0) and (count_A_previous == 1) and (math.floor(math.log10(int(prefix_A)))+1 == math.floor(math.log10(extracted)))):
        # Found an exact match in the csv and it's the only match and length(csv_Entry) = length(extracted part of the number given)
        oper_A_Flag = False
    elif((count_A_cur == 0) and (count_A_previous == 0)):
        # No match between any entry in the csv and the extracted part of the number given in the two previous loops         
        oper_A_Flag = False   

    # For Operator B
    for i in range(0,len(data_B)):
        len_B = math.floor(math.log10(int(data_B[i][0])))+1        
        if(len_B > counter):    # Proceed only for entries whose length is bigger than the length of the extracted part of the nubmer given
            oper_num_B = int(data_B[i][0]) // (10 ** (len_B - counter - 1))
            if(oper_num_B == extracted):
                count_B_cur += 1
                if(len_B == math.floor(math.log10(extracted))+1):   # If there is a match, save the prefix, the price and skip the rest of the csv entries
                    prefix_B = data_B[i][0]
                    cost_B = float(data_B[i][1])
                    break

    if((count_B_cur == 0) and (count_B_previous == 1) and (math.floor(math.log10(int(prefix_B)))+1 == math.floor(math.log10(extracted)))):
        # Found an exact match in the csv and it's the only match and length(csv_Entry) = length(extracted part of the number given)
        oper_B_Flag = False
    elif((count_B_cur == 0) and (count_B_previous == 0)):
        # No match between any entry in the csv and the extracted part of the number given in the two previous loops     
        oper_B_Flag = False   

    # Increase counter that will help on extracting the next digit
    counter += 1

if((prefix_A == initial_prefix) and (cost_A == -1) and (prefix_B == initial_prefix) and (cost_B == -1)):
    # No match for Operator A and Operator B
    print("Unfortunatley, none of our operators can help you.")
elif(prefix_A != initial_prefix and prefix_B == initial_prefix):
    # Match for Operator A, but not Operator B
    print("Operator A will help you at the price of:",cost_A, "per minute")
elif(prefix_A == initial_prefix and prefix_B != initial_prefix):
    # Match for Operator B, but not Operator A
    print("Operator B will help you at the price of:",cost_B, "per minute")
else:
    # Match for both Operators
    if(cost_A <= cost_B):
        # Operator A is cheaper
        print("Operator A will help you at the price of:",cost_A, "per minute")
    else:
        # Operator B is cheaper
        print("Operator B will help you at the price of:",cost_B, "per minute")