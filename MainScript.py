import csv
import math

initial_prefix = 111111111 # A number that cannot be a prefix

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

# print(data_A[1][0])

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

prefix_A = initial_prefix
prefix_B = initial_prefix

cost_A = -1
cost_B = -1

oper_A_Flag = True
oper_B_Flag = True

count_A_previous = -1
count_A_cur = -1
count_B_previous = -1
count_B_cur = -1

counter = 0
extracted = num_given // (10 ** (len_num - counter - 1))

while (counter <= len_num) and oper_A_Flag:
    count_A_previous = count_A_cur
    count_A_cur = 0
    extracted = num_given // (10 ** (len_num - counter - 1))

    for i in range(0,len(data_A)):
        len_A = math.floor(math.log10(int(data_A[i][0])))+1        
        if(len_A > counter):
            oper_num_A = int(data_A[i][0]) // (10 ** (len_A - counter - 1))
            if(oper_num_A == extracted):
                count_A_cur += 1
                if(len_A == math.floor(math.log10(extracted))+1):
                    prefix_A = data_A[i][0]
                    cost_A = float(data_A[i][1])
                    break

    if((count_A_cur == 0) and (count_A_previous == 1) and (math.floor(math.log10(int(prefix_A)))+1 == math.floor(math.log10(extracted)))):
        oper_A_Flag = False
    elif((count_A_cur == 0) and (count_A_previous == 0)):        
        oper_A_Flag = False       

    counter += 1

if((prefix_A == initial_prefix) and (cost_A == -1) and (prefix_B == initial_prefix) and (cost_B == -1)):
    print("Unfortunatley, none of our operators can help you.")
else:
    print(prefix_A,cost_A)