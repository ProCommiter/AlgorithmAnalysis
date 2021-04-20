import numpy as np
import random

'''
For each item i, let 0 <= f(i) <= 1 be a fraction of item i. Find a subset S in I and a fraction f(i) for i in S s.t.
    sum of (i in S) f(i)wi <= W and sum of (i in S) f(i)vi is maximized
'''
class ItemValue:

    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost

def fractional_knapsack(val, weight, capacity):
    ratio = []
    for i in range(len(val)):
        ratio.append(ItemValue(weight[i], val[i], i))

    ratio.sort(reverse=True)

    total = 0
    for i in ratio:
       curWt = int(i.wt)
       curVal = int(i.val)
       if capacity - curWt >= 0:
          capacity -= curWt
          total += curVal
       else:
          fraction = capacity / curWt
          total += curVal * fraction
          capacity = int(capacity - (curWt * fraction))
          break
    return total

def main():
    val = [1,6,18,22,28]
    wt = [1,2,5,6,7]
    W = 11
    print("Greedy algorithm approach to Knapsack problem")
    print("Values and Weights")
    print(val)
    print(wt)

    print("Knapsack has capacity of", W, "amount", end = " ")
    print(fractional_knapsack(val, wt, W), "is the maximum profit")

if __name__ == '__main__':
    main()
