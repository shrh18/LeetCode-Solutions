class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return True if len(counter.values()) == len(set(counter.values())) else False
            