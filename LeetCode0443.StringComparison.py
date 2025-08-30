"""
Q: Given an array of characters chars, compress it using the following algorithm:
So I just follow what the instruction said and comes up with this, at first I did come up with loop and compare bwtween i and i+1 which result in didn't read the last value due to index out of bound. So I twist it a bit ans start from one to the last instead then have the handle case for the last element
1. For loop from second to last compare with the element in front of it to check how many that character have
2. If value at position i-1 != i we then append value of i-1 and if it's have more than one we append our count

Runtime
3
ms
Beats
36.55%

Memory
17.78
MB
Beats
94.43%

"""

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        count = 1

        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                s.append(chars[i-1])
                if count > 1:
                    s.extend(list(str(count)))
                count = 1

        s.append(chars[-1])
        if count > 1:
            s.extend(list(str(count)))

        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)
