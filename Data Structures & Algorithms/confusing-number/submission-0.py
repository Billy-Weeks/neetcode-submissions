class Solution:
    def confusingNumber(self, n: int) -> bool:
        # simply declare two dicts: confuse, not_confuse
            # key: intial value
            # value: flipped value
        # don't forget the check if flipped number is the same as original
        valid = {0 : 0, 1: 1, 6: 9, 8: 8, 9: 6}
        invalid = {2, 3, 4, 5, 7}
        new_num = 0

        n_string = str(n)
        
        # check if valid/invalid, create new number
        for index, value in enumerate(n_string):
            n_value = int(value) # change to integer
            if n_value in invalid:
                return False
            flipped = valid[n_value]
            new_num += flipped * (10**index)          
        if new_num == n:
            return False
        return True
        