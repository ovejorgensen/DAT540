import numpy as np

def longestLine(arr):
    longest = 0
    for i in arr:
        row = 0
        rowLongest = 0
        for j, val in enumerate(i):
            if val == 0: 
                row = rowLongest
                rowLongest = 0
            elif val == 1:
                rowLongest = rowLongest + 1
            if j+1 == len(i) and rowLongest > row: row = rowLongest
        if row > longest: longest = row
    return longest


def main():
    arr = np.array([[1, 1, 1, 0],
                    [0, 1, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

    longest = [longestLine(arr)] # Longest horizontal
    vertical = arr.transpose()
    longest.append(longestLine(vertical)) # Longest vertical

    diags = [arr[::-1,:].diagonal(i) for i in range(-arr.shape[0]+1,arr.shape[1])]
    diags.extend(arr.diagonal(i) for i in range(arr.shape[1]-1,-arr.shape[0],-1))
    longest.append(longestLine(n.tolist() for n in diags))


    print("Longest consecutive line: ", max(longest))



if __name__ == "__main__":
    main()
