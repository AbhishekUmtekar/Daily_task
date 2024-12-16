

-----------------------Q1
*******
******
*****
****
***
**
*

Code: 

rows = 7

# Loop
for i in range(rows, 0, -1):
    print('*' * i)

------------------Q2
----*
---**
--***
-****
*****

Code: 
# Number of rows 
rows = 5

# Loop 
for i in range(1, rows + 1):
    # Print leading spaces and stars
    print(' ' * (rows - i) + '*' * i)

--------------------Q3
1
10
101
1010
10101

Code: 

# Number of rows 
rows = 5

# Loop to print each row
for i in range(1, rows + 1):
    # Generate the pattern for the current row
    row_pattern = ''
    for j in range(i):
        # Append '1' or '0' depending on the index
        if j % 2 == 0:
            row_pattern += '1'
        else:
            row_pattern += '0'
    
    # Print the current row
    print(row_pattern)

---------------Q4
____1
___01
__101
_0101
10101

Code: 

# Number of rows 
rows = 5

# Loop to print each row
for i in range(1, rows + 1):
    row_pattern = ''
    for j in range(i):
        if (i + j) % 2 == 0:
            row_pattern += '1'
        else:
            row_pattern += '0'

    print(' ' * (rows - i) + row_pattern)
x

-----------------Q5
*********
-*******
--*****
---***
----*

Code: 

# Number of rows
rows = 5

# Loop to print each row
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))














