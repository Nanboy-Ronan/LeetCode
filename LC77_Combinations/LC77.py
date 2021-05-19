from typing import List

class CombinationSolution:
    # LeetCode 77. Combinations
    # Given two integers n and k, return all possible combinations of k numbers out of the range [1, n]. You may return the answer in any order.
    # Method: Backtracking
    # Time Complexity: O(c(n,k))
    # Space Complxity: O(k)
    def __init__(self, end, numPerGroup) -> None:
        self.n = end
        self.k = numPerGroup

    def main(self) -> None:
        result = []
        result = self.combine(self.n, self.k)
        #self.printArray(result)
        print(result)


    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtracking(n, k, result, 1, [])
        return result


    # result is the result to return (this function add new list into result)
    # begin is the next number to start (this is to avoid repetition in the result)
    def backtracking(self, n: int, k: int, result: List[List[int]], begin: int, list: List[int]) -> None:
        if(len(list) == k):
            # copy list to avoid change the original list
            result.append(list[:])
            return
        for i in range(begin, n+1):
            list.append(i)
            self.backtracking(n,k,result,i+1,list)
            list.pop()
    
    def printArray(self, arr: List[List[int]]):
        print("[")
        for i in range(len(arr)):
            print("[")
            for j in range(len(arr[i])):
                print(arr[i][j])
                print(", ")
            print("]")
        print("]")


test = CombinationSolution(4, 2)
test.main()
