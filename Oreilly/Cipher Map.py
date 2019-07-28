'''

SOLUTION NOT IDEAL AND DOES NOT WORK FOR LARGER GRIDS

Cipher Grille is 4 x 4 grid with 4 squares cut out.
Encoder writes down the first 4 symbols of his
password inside the cut out squares.
Encoder rotates grille 90 deg clockwise.
Previous symbols become hidden and they write the next
4 symbols of the password in the new squares

See link below for visual example
https://js-static.checkio.org/media/task/media/badfa46b25c948fdaaa5e5946b3ef1c4/cipher_map.png

Input: A cipher grille and a ciphered password as a
tuples of strings.
Output: The password as a string.
'''

def recall_password(cipher_grille, ciphered_password):
    # in order of 90 deg rotation
    corner_indices = [[0, 0], [0, 3], [3, 3], [3, 0]]
    centre_indices = [[1, 2], [2, 2], [2, 1], [1, 1]]
    edge_1_indices = [[2, 0], [0, 1], [1, 3], [3, 2]]
    edge_2_indices = [[2, 3], [3, 1], [1, 0], [0, 2]]
    initial_indices = []
    password = ''

    # find initial locations of X
    a = 0
    b = 0
    while a < len(cipher_grille):
        while b < len(cipher_grille):
            if cipher_grille[a][b] == 'X':
                # will append in order from top to bottom row and left to right column
                initial_indices.append([a, b])
            b += 1
        b = 0
        a += 1

    # find which indices list each initial X is fom
    # reorder the following lists for iteration later
    for initial_index in initial_indices:
        if initial_index in corner_indices:
            initial_corner = corner_indices.index(initial_index)
            corner_indices = corner_indices[initial_corner:] + corner_indices[0:initial_corner]
        elif initial_index in centre_indices:
            initial_centre = centre_indices.index(initial_index)
            centre_indices = centre_indices[initial_centre:] + centre_indices[0:initial_centre]
        elif initial_index in edge_1_indices:
            initial_edge_1 = edge_1_indices.index(initial_index)
            edge_1_indices = edge_1_indices[initial_edge_1:] + edge_1_indices[0:initial_edge_1]
        else:
            initial_edge_2 = edge_2_indices.index(initial_index)
            edge_2_indices = edge_2_indices[initial_edge_2:] + edge_2_indices[0:initial_edge_2]

    # double all_indices for overlap repeat cases
    all_indices = corner_indices*2 + centre_indices*2 + edge_1_indices*2 + edge_2_indices*2

    # Sort each list of indices upon rotation based on their row and column values
    i = 0
    j = 0
    while i < len(cipher_grille):
        next_indices = []
        while j < len(cipher_grille):
            index = all_indices.index(initial_indices[j]) + i
            coordinates = all_indices[index]
            next_indices.append(coordinates)
            j += 1
        k = 0
        sorted_next_indices = []
        while k < 4:
            temp = []
            for l in next_indices:
                if l[0] == k:
                    temp.append(l)
                if len(temp) > 1:
                    if temp[-1][1] < temp[0][1]:
                        temp.insert(0, temp[-1])
                        temp.reverse()
                        temp.remove(temp[0])
                        temp.reverse()
            sorted_next_indices += temp
            k += 1
        for coordinate in sorted_next_indices:
           password += ciphered_password[coordinate[0]][coordinate[1]]
        j = 0
        i += 1
    return password


print(recall_password(
    ('XXXX',
     '....',
     '....',
     '....'),
    ('call',
     'rsqi',
     'epzn',
     'yeee')))
