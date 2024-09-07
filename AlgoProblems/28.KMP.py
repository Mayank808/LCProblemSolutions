class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP Approach: O(n + m)

        # PREPROCESSING
        if len(needle) > len(haystack):
            return -1

        pi = [0] * len(needle)
        # Length of Longest Border for prefix before it.
        prev = 0
        # Iterating from index-1. longest_border[0] will always be 0
        i = 1

        while i < len(needle):
            if needle[i] == needle[prev]:
                # Length of Longest Border Increased
                prev += 1
                pi[i] = prev
                i += 1
            else:
                # Only empty border exist
                if prev == 0:
                    pi[i] = 0
                    i += 1
                # Try finding longest border for this i with reduced prev
                else:
                    prev = pi[prev - 1]

        index = 0
        letter = 0

        while letter < len(haystack):
            print(index, needle[index], letter, haystack[letter])
            if haystack[letter] == needle[index]:
                letter += 1
                index += 1

                if len(needle) == index:
                    return letter - len(needle)
            
            else:
                if index == 0:
                    letter += 1
                else:
                    index = pi[index - 1]



        return -1


        # # Navie approach: O(n * m)
        # if not needle:
        #     return True

        # for left in range(len(haystack)):
        #     index = 0
        #     while left + index < len(haystack) and haystack[left + index] == needle[index]:
        #         index += 1
        #         if index >= len(needle):
        #             return left
        
        # return -1
            
