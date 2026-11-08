class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        
        # create hash for month: days
        months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
                    6: 30, 7: 31, 8: 31, 9: 30,
                    10: 31, 11: 30, 12: 31}
        
        if month == 2:
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                return months[month] + 1
        return months[month]

