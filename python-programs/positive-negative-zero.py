class CheckNumber:
    def check(n):
        if n>0:
            print("{0} is positive".format(n))
        elif n<0:
            print("{0} is negative".format(n))
        else:
            print("{0} is zero".format(n))


n = int(input('Enter an integer'))
c = CheckNumber
c.check(n)
