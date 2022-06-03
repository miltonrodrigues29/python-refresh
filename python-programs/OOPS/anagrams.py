class Anagram:
    def check_anagram(self,string1,string2):
        if len(string1)!=len(string2):
            print("String length does not match!, they are not anagrams")
        else :  
            for i in string1:
                if i not in string2:
                    print("Not Anagrams")
                    break
            else:
                print("Anagrams")


o1 = Anagram()
o1.check_anagram("eat","ate")
