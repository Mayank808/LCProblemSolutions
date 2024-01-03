class Solution:
    # count number of beams in one row.
    # using previous rows count we can compute beams: prev * curr
    # if curr is 0 keep prev the same
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0
        for string in bank:
            # curr = string.count('1')
            curr = 0
            for c in string:
                if c == '1':
                    curr += 1
            
            if not curr:
                continue
            
            res += curr * prev
            prev = curr

        return res
      
