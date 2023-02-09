class Sum:
    @staticmethod
    def getSum(*args):

        Sum = 0
        for i in args:
            Sum += i
            return Sum

def main():
    print("Sum :", Sum.getSum(1,2))
    
main()
