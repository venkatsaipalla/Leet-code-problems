class Solution:
    def numberOfWeakCharacters(self, p: List[List[int]]) -> int:
        # the final answer to be returned
        weakCharacters = 0
        # record maximum defense. since 1 <= defense_i <= 10 ^ 5
        # we can set the init value to x where x < 1
        maxDefense = 0
        # sort properties with custom sort comparator
        # if the attack is same, then sort defense in descending order  
        # otherwise, sort attack in in ascending order 
        p.sort(key = lambda x: (x[0], -x[1]), reverse = True)
		# or we can do it like 
		# p.sort(key = lambda x: (-x[0], x[1]))
        for _, defense in p:
            # if it is less than current maxDefense, then it means it is a weak character
            if defense < maxDefense: weakCharacters += 1
            # update maxDefense
            else: maxDefense = defense
        return weakCharacters  
