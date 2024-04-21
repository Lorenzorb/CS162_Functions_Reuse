import numpy as np

def step1():
    # Generate a 5x5 matrix of random integers between 0 and 10.
    return np.random.randint(0, 10, size=(5, 5))

def step2(matrix):
    # Print the given matrix.
    print(matrix)

def step3(matrix):
    # Print the item in the 2nd row, 3rd column of the given matrix.
    print(f"The item in 2nd row 3rd column is {matrix[1, 2]}")

def step4(matrix):
    # Print the total sum of all elements in the given matrix.
    print(f"The total of all elements is {matrix.sum()}")

def step5(matrix):
    # Calculate and print the mean of each row in the given matrix.
    for row in matrix:
        print(f"The mean of {row} = {row.mean()}")

def step6(matrix):
    # Calculate and print the maximum value of each column in the given matrix.
    for i in range(len(matrix[0])):
        print(f"Max of column {i+1} = {matrix[:, i].max()}")

matrix = step1()
step2(matrix)
step3(matrix)
step4(matrix)
step5(matrix)
step6(matrix)
