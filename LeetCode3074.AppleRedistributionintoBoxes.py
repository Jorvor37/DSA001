class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sum_apple = sum(apple)
        sum_capacity = 0
        count = 0

        while sum_capacity < sum_apple and capacity:
            max_capacity = max(capacity)
            sum_capacity += max_capacity
            capacity.remove(max_capacity)
            count += 1
        
        return count
