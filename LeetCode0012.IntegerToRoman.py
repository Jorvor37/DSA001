"""
MMMMCMXCIX = 4999
4999 = MMMM
Q: convert Integer to Roman number
I tackle this question using simple yet complicate if else statement
1. Create array to later on store the string
2. Use if else for every possible output like 1000, 900, 500, 400, 100, 90, 50, 10, 9, 5, 4, 1
3. Tell how many of each character need to be print by using floor operator
4. join each character one by one into answer array, then return
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ""
        while num != 0:
            if num >= 1000:
                Mval = num // 1000
                num -= Mval * 1000
                while Mval > 0:
                    answer = "".join([answer, "M"])
                    Mval -= 1
            elif num >= 900:
                CMval = num // 900
                num -= CMval * 900
                while CMval > 0:
                    answer = "".join([answer, "CM"])
                    CMval -= 1
            elif num >= 500:
                Dval = num // 500
                num -= Dval * 500
                while Dval > 0:
                    answer = "".join([answer, "D"])
                    Dval -= 1
            elif num >= 400:
                CDval = num // 400
                num -= CDval * 400
                while CDval > 0:
                    answer = "".join([answer, "CD"])
                    CDval -= 1
            elif num >= 100:
                Cval = num // 100
                num -= Cval * 100
                while Cval > 0:
                    answer = "".join([answer, "C"])
                    Cval -= 1
            elif num >= 90:
                XCval = num // 90
                num -= XCval * 90
                while XCval > 0:
                    answer = "".join([answer, "XC"])
                    XCval -= 1
            elif num >= 50:
                Lval = num // 50
                num -= Lval * 50
                while Lval > 0:
                    answer = "".join([answer, "L"])
                    Lval -= 1
            elif num >= 40:
                XLval = num // 40
                num -= XLval * 40
                while XLval > 0:
                    answer = "".join([answer, "XL"])
                    XLval -= 1
            elif num >= 10:
                Xval = num // 10
                num -= Xval * 10
                while Xval > 0:
                    answer = "".join([answer, "X"])
                    Xval -= 1
            elif num >= 9:
                IXval = num // 9
                num -= IXval * 9
                while IXval > 0:
                    answer = "".join([answer, "IX"])
                    IXval -= 1
            elif num >= 5:
                Vval = num // 5
                num -= Vval * 5
                while Vval > 0:
                    answer = "".join([answer, "V"])
                    Vval -= 1
            elif num >= 4:
                IVval = num // 4
                num -= IVval * 4
                while IVval > 0:
                    answer = "".join([answer, "IV"])
                    IVval -= 1
            else:
                Ival = num
                num -= Ival
                while Ival > 0:
                    answer = "".join([answer, "I"])
                    Ival -= 1
        #end while
        return answer
