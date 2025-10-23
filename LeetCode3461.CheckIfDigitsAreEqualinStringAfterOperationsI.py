
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            temp_list = []
            for i in range(len(s)-1):
                temp = (int(s[i]) + int(s[i+1])) % 10
                temp_list.append(str(temp))
            s = "".join(temp_list)

        if s[0] == s[1]:
            return True
        else:
            return False
