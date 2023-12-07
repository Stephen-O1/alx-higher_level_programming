#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new = []
        for rows in matrix:
            new.append(list(map(lambda x: x**2, rows)))
        return (new)
    return None

# return[[elem**2 in row] for row in matrix]
# return(list(map(lambda x: x**2, list)) forl ist in matrix)
