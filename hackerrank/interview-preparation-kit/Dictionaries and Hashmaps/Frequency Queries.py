#!/bin/python3
#https://www.hackerrank.com/challenges/frequency-queries

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.


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

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

