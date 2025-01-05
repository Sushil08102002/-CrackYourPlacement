# Question Number 287

from typing import List
from collections import defaultdict


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in range(len(nums)):
            if d[nums[i]]==1:
                return nums[i]
            else:
                d[nums[i]]+=1

def main():
    num=list(map(int,input().split()))
    new_obj=Solution()
    solution=new_obj.findDuplicate(num)
    print(solution)

if __name__=="__main__":
    main()

                
        