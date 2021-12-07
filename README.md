# Programming-Callenge

This is a repository for the solution of the Programming Challenge found [here](https://docs.google.com/document/d/14j6tWiFN5DlfitQrU2AD2VNun71UTNjKDbueK55RDgM/edit?usp=sharing).

For solving this challenge I used Python3 and the libraries csv and math.

There are two possible options for running the solution of this challenge:
- Using Python3:
    - Open a terminal in this folder
    - Install the dependencies:
  ```
    pip install csv
    pip install math
  ```
  - Execute the Python Script:
  ```
    python3 MainScript.py
  ```

- Execute the .exe file
    - Open a terminal in this folder
    - Execute the following line
     ```
    ./dist/MainScript
    ```

## Explanation of my Solution
For this challenge I created 2 csv files, one for each operator, and added the prefixes alongside their prices. Similarly, one could add more prefixes and prices in these csv files without affecting the end result.

There is an extra csv file called "TestValues.csv", which includes some test values and their results for the final price. One could add more test cases in this csv file, making sure that the end result is correct.

In the script, I read the two csv files and I ask for the user to input an integer number that represents the phone number that wishes to call. There is a while loop to make sure that the user actually inserted an integer number and not string or float.

I extract this integer number by number, for example if the integer number is 123456789, I extract the number as 1, 12, 123 and so on. For each extracted number, I compare it with the corresponding extracted numbers from the two csv files, until there is at least one match for each file. If a match is found, then the investigation continues by extracting the next number (e.g. 1234) and repeat the process, until there is no match found in both files. If no match is found in one of the files, in the next loop there won't be an investigation in that file and it will only look for a match in the other file.

In the end, when no matches are found in any of the files, there is a simple comparison to find which operator is the cheapest option and prints the operator with the corresponding price in the terminal. If the final result matches the result of the "TestValues.csv" file, the message "Correct" is printed, otherwise, the message "False" is printed.

Complexity of the solution:

    
    2KN
    

Where K is the length of the integer given (e.g. the length of the integer 1234 is 4), and N is the size of the csv files. Multiplied by 2 as there are two possible operators that can handle the phonecall.