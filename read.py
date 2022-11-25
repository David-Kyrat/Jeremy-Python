LINE_ENDING = "\n"

lines = []

with open("res.txt", "r") as f:
    lines = f.readlines()
f.close()


SEPARATOR = " "


matrix = []
for line in lines:
    #clean_line = line.split(LINE_ENDING)[0] # without LINE ENDING
    #res2 = clean_line.split(SEPARATOR) #* en 2 temps

    #* plus rapide:
    split_line = line.split(LINE_ENDING)[0].split(SEPARATOR)
    matrix.append(split_line)
    

def printf(s):
    print(s)


def get_column(matrix, idx):
    col = []
    for i in range(len(matrix)):
        col.append(matrix[i][idx])

    return col


""" print(get_column(matrix, 2))
print(get_column(matrix, 1)) """

def printcolij(matrix, col1_idx, col2_idx):
    col0 = get_column(matrix, col1_idx)
    col1 = get_column(matrix, col2_idx)

    for el1, el2 in zip(col0, col1):
        tmp = [el1, el2]
        joined_str = "-".join(tmp)

        print(joined_str)

printcolij(matrix, 0, 2)