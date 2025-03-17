# this function will return array for broadcasting according
# to the rows and columns 
def broadcasting_list(rows, cols, value):
    # creating empty list
    arr = []
    for i in range(rows):
        columns = []
        for j in range(cols):
            if(isinstance(value, int)):
                columns.append(value)
            else:
                columns.append(value[j])
        arr.append(columns)
    return arr