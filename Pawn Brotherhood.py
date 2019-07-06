'''
A pawn is safe if another pawn can capture a unit on that square.
We have several white pawns on the chess board and only white pawns.
You should design your code to find how many pawns are safe.

You are given a set of square coordinates where we have placed white pawns.
You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.

Precondition:
0 < pawns ≤ 8
'''

def safe_pawns(pawns: set) -> int:
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ranks = [1, 2, 3, 4, 5, 6, 7, 8]
    safe = set()
    for pawn in pawns:
        file, rank = pawn[0], int(pawn[1])  # get file and rank of pawn
        file_index = files.index(file)  # get index of file of pawn
        rank_index = ranks.index(rank)  # get index of rank of pawn
        for other_pawn in pawns:
            other_file, other_rank = other_pawn[0], int(other_pawn[1])
            if file != files[0] and file != files[-1] and rank_index != 0:  # pawn is not in file a or h (index error)
                if other_file == files[file_index-1] or other_file == files[file_index+1]:  # other pawn in file L or R
                    if other_rank == ranks[rank_index-1]:  # other pawn is 1 rank below
                        safe.add(pawn)  # add pawn to safe set
                        break
            elif rank == ranks[0]:
                continue
            elif file == files[-1]:  # pawn file is g
                if other_file == files[file_index-1]:  # other pawn in file L
                    if other_rank == ranks[rank_index-1]:  # other pawn is 1 rank below
                        safe.add(pawn)
                        break
            elif file == files[0]: # pawn file is a
                if other_file == files[file_index+1]:  # other pawn in file R
                    if other_rank == ranks[rank_index-1]:  # other pawn is 1 rank below
                        safe.add(pawn)
                        break
    return len(safe)

print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})) #6
print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})) #1


'''
Interesting alternate solutions on Checkio
___________________________________________________________________________________________________________________
def safe_pawns(pawns: set) -> int:
    
    counter = 0
    for pawn in pawns:
        letter, back_row = pawn[0], str(int(pawn[1]) - 1)
        # ord('a') == 93, chr(94) == 'b',  chr(ord('b') - 1) == 'a'
        left_back = chr(ord(letter) - 1) + back_row
        right_back = chr(ord(letter) + 1) + back_row
        if left_back in pawns or right_back in pawns:
            counter += 1        

    return counter
'''