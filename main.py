def optimalSolution(graph, decisions, N):
    profit = [0] * (N + 1)
    d = [0] * (N - 1)

    selectedValue = 0
    maximumPath = 0
    for i in range(N - 2, -1, -1):
        for j in range(N + 1):
            if graph[i][j] != 0 and profit[i] < graph[i][j] + profit[j]:
                profit[i] = max(profit[i], graph[i][j] + profit[j])
                d[i] = j
                if selectedValue < profit[i]:
                    selectedValue = profit[i]
                    maximumPath = i

    output = ""
    i = maximumPath
    while i < N - 1:
        for key, value in decisions.items():
            if i + 1 == value[0] and d[i] + 1 == value[1]:
                output += "\nDecyzja " + key + ": (" + str(i + 1) + ", " + str(d[i] + 1) + ") => " + str(graph[i][d[i]])
        i = d[i]
    output += "\nSuma korzyści wynosi: " + str(selectedValue)
    profit.sort(reverse=True)
    return output


def main():
    graph = [[0, 0, 150, 120, 130, 0, 0, 0, 0],
             [0, 0, 140, 160, 180, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 170, 150, 0, 0],
             [0, 0, 0, 0, 0, 170, 180, 0, 0],
             [0, 0, 0, 0, 0, 160, 170, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 150, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 140],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    decisions = {'A': [1, 3], 'B': [1, 4], 'C': [1, 5], 'D': [2, 3], 'E': [2, 4],
                 'F': [2, 5], 'G': [3, 6], 'H': [3, 7], 'I': [4, 6], 'J': [4, 7],
                 'K': [5, 6], 'L': [5, 7], 'M': [6, 8], 'N': [7, 9]}

    dimensions = 8

    print("Najbardziej korzystne rozwiązanie:", optimalSolution(graph, decisions, dimensions))


if __name__ == "__main__":
    main()
