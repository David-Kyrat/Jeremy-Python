
"""
mat:list[list[str]] = [line.split("\n")[0].split(" ") for line in lines]


clearline = lines[0].rstrip().split(' ')
print(clearline)
print(clearline[2])""" 

def getcolumn(matrix, j):
    return [matrix[i][j] for i in range(len(matrix))]



def get_month(matrix, month_column_idx, month_number, to_extract_idx):
    # to_extract_idx : indice de ce que tu veux récupérer dans chaque ligne

    month = []
    crt_month_number = matrix[0][month_column_idx] # first month 
    i = 0
    while crt_month_number == month_number: # while our crt month is still the one we want

        month.append(matrix[i][to_extract_idx]) # add value of month
        crt_month_number= matrix[i][month_column_idx]
        
        i = i + 1
        
    # we changed month => so we get everything we wanted
    return month


    

def moyenne_col(matrix, j, month_column_idx, month_number):
    col = getcolumn(matrix, j)
    col_asfloat = [float(col[i]) for i in range(len(col)) if matrix[i][month_column_idx] == month_number]

    #
    # equivalent to
    # col_asfloat = []
    # for el in col:
    #
    #   if matrix[i][month_column_idx] == month_number:
    #      col_asfloat.append(float(el))
    #
    
    summ = sum(col_asfloat)
    return summ / len(col)


def write_to_csv(data, fileName):
    # data doit être une liste !
    
    with open(fileName, "w") as file:
        for i in range(len(data)):
            msg = f"{i}, {data[i]}\n" # pas oublier le "\n"
            file.write(msg)

write_to_csv([5, 8, 9, 12, 24, 36, 64, 52], "lul.csv")
            





    






