#Homework 6 functions

def get_p_distance(list1, list2):

    #get distance function of 2 lists

    y = 0

    for x in range(0,len(list1)):
        if list1[x] != list2[x]:
            y += 1
    
    p_distance = y/(len(list1))

    return p_distance


def get_p_distance_matrix(list1):

    pre_distance_matrix = []

    l1 = [i for i in range(0, len(list1))]

    j = 0
    for i in range(0, len(list1)):
        for j in range(0, len(list1)):
            x = get_p_distance(list1[i],list1[j])
            pre_distance_matrix.append(x)

    matrix = []
    k = 0

    for i in range(0,len(l1)):
        pre_matrix = []
        for j in range(0,len(l1)):
            pre_matrix.append(pre_distance_matrix[k])
            k += 1
        
        matrix.append(pre_matrix)

    return matrix


