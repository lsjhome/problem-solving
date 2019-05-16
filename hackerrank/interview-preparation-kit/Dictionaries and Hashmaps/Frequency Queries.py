#!/bin/python3
#https://www.hackerrank.com/challenges/frequency-queries

from collections import defaultdict

def freqQuery(queries):

    ans = []

    count_dict = defaultdict(int)
    preq_dict = defaultdict(int)

    for query, data in queries:

        if query == 1:
            count_dict[data] += 1
            preq_dict[count_dict[data]] += 1
            preq_dict[count_dict[data] - 1] -= 1

        if query == 2:
            if count_dict[data] > 0:
                count_dict[data] -= 1
                preq_dict[count_dict[data]] += 1
                preq_dict[count_dict[data] + 1] -= 1

        if query == 3:
            ans.append(1 if preq_dict[data] > 0 else 0)

    return (ans)

queries = [[1, 1,], [2, 2], [3, 2], [1, 1], [1, 1], [2, 1], [3, 2]]

print (freqQuery(queries))

print (69 /4)
