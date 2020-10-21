import numpy as np

def horizontals(ndarr):
    longest = 0
    for i in ndarr:
        row = longestLine(i)
        if row > longest: longest = row
    return longest

def longestLine(arr):
    row = 0 
    row_longest = 0
    for j, val in enumerate(arr):
        if val == 0: 
            row = row_longest
            row_longest = 0
        elif val == 1:
            row_longest = row_longest + 1
        if j+1 == len(arr) and row_longest > row: row = row_longest
    return row

def longestDiagonal(arr):
    diag_arr = arr.copy()
    dimension_y = arr.shape[0]
    dimension_x = arr.shape[1]
    print(diag_arr)
    result = []
    before = dimension_x-1
    after = 0
    for i in diag_arr:
        current = i.tolist()
        for k in range(0, before):
            current.insert(0, 0)
        for k in range(0, after):
            current.append(0)
        result.append(current)

        before = before - 1
        after = after + 1

        # [X, X, X, 1, 1, 0, 0],
        # [X, X, 0, 0, 1, 1, X],
        # [X, 0, 0, 1, 1, X, X],
        # [1, 0, 0, 0, X, X, X]

    return longestLine(np.array(result).transpose())

def main():
    M = np.array([[1, 0, 1, 1],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]])

    longest = [horizontals(M)] # Longest horizontal
    longest.append(horizontals(M.transpose())) # Longest vertical
    longest.append(longestLine(M.diagonal())) # Longest diagonal
    longest.append(longestLine(np.fliplr(M).diagonal())) # Longest diagonal flipped

    print(longest)
    print("Longest consecutive line: ", max(longest))



if __name__ == "__main__":
    main()
