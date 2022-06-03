class Arguments:
    def example(self,a,b,*args):

        print(a,b)
        print(len(args))
        print(type(args))
        print("-----elements in argument buffer-----")
        for i in args:
            print(i)

    
    def example2(self,a,b,**kargs):
        print(a,b)
        print("These are the keys--------------------->")
        for i in kargs.keys():
            print(i)
        print("These are the keys--------------------->")
        for i in kargs.values():
            print(i)
        print("These are the both--------------------->")
        for i,j in zip(kargs.keys(),kargs.values()):
            print(i,":",j)


# o1 = Arguments()
# o1.example("Milton","Rodrigues","Extra","Extra1","one more")

o2 = Arguments()
o2.example2("Christon","Rodrigues",firstKey = "First Key", secondKey ="Second key")