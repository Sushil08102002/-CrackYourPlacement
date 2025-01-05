class Solution:

    def __init__(self, string, sub):
        self.string = string
        self.sub = sub

    def find_count(self):
        count = 0
        left, right = 0, len(self.sub)
        
        # Sliding window approach
        while right <= len(self.string):
            if self.string[left:right] == self.sub:
                count += 1
            left += 1
            right += 1
        
        return count

# Example usage
new = Solution("Sushil", "Su")
result = new.find_count()
print(f"'{new.sub}' appears {result} times in '{new.string}'")
