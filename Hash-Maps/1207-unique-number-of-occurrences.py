class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        # Check if the occurrences are unique
        occurrences_set = set(hashmap.values())
        return len(occurrences_set) == len(hashmap)