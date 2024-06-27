# require a delimeter as word length can be double digit.
class Solution:
    delimeter = '#'
    def encode(self, strs: List[str]) -> str:
        ret = ""
        for word in strs:
            ret += f"{len(word)}{self.delimeter}{word}"
        return ret

    def decode(self, s: str) -> List[str]:
        cur_str = ""
        cur_length = 0
        ret = []
        k = 0
        while k < len(s):
            while s[k] != self.delimeter:
                print(s[k])
                cur_length *= 10
                cur_length += int(s[k])
                k += 1
            k += 1
            while cur_length:
                cur_str += s[k]
                k += 1
                cur_length -= 1
            ret.append(cur_str)
            cur_str = ""
        
        return ret


