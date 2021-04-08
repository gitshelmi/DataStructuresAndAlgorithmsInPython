from problem_base import ProblemBase
from constants import Constants as ctx
from typing import List

class TwoSum(ProblemBase):
    def __init__(self):
        name = "TwoSum"
        description = '''
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
            You may assume that each input would have exactly one solution, and you may not use the same element twice.
            You can return the answer in any order.
            Example 1:              
         Input: nums = [2, 7, 11, 15], target = 9
         Output:[0,1]
         Output: Because nums[0] +nums[1] == 9, we return [0, 1].

         Example 2:              
         Input: nums = [3, 2, 4], target = 6
         Output:[1,2]
        '''
        source = 'https://leetcode.com/problems/two-sum/'
        level = ctx().level_easy
        keywords = [ctx().tags_arrays]
        super().__init__(name, description, source, level, keywords)

    def two_sum_solver(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            return None
        
        complement_index_map = {}
        indices = [0, 0]
        
        for index in range(len(numbers)):            
            number = numbers[index]
            # check if the complement has already found
            if number in complement_index_map.keys():
                indices[0] = complement_index_map[number]
                indices[1] = index
                break
        
        # add the complement and its index to the dictionary
            complement = target - number
            complement_index_map[complement] = index

        return indices
    