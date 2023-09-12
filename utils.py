class utils:
    def reversed(self, num):
        num_str = str(num)
        reversed_str = num_str[::-1]
        return int(reversed_str)

    
    def formatter(self, num):
        base2 = bin(num)
        base8 = oct(num)
        return base2, base8

'''
Checking to see if it works
utils_instance = utils()
num = 10 
reversed_num = utils_instance.formatter(num)
print(reversed_num)
'''