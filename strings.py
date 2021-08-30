#code breaker
def decode(string,n):
    result = ""
    start = n
    end = 2*n
    for i in range(0,(len(string))):
        result += string[start:end]
        start += 2*n
        end += 2*n
    return result
print(decode("#P#Y#T#H#O#N",1))
print(decode("AxYLet1x3’s T74codaa7e!",3))

##Pattern Finder
def pattern_count(string,pat):
    a = len(string)
    result = 0
    end = len(pat)
    for i in range (0,a):
        if pat == string[i :end]:
             result += 1
        pass
        end += 1
    return result
print(pattern_count("abcabcabcab","abc"))
print(pattern_count("aaaa", "aa"))
print(pattern_count("A long time ago in a galaxy far, far away...", "a"))
print(pattern_count("If you must blink, do it now.", "code"))


##Palindromes
def palindrome(string):
    punctuationMarks = "%" "#""\"""=""?"">""{""|"",""!""\"""$""]""@"":"";" "_""'" ".""}" "+""~""*"")""[""/""&""(""-""^""<""`"
    string = "".join(x for x in string if x not in punctuationMarks)
    y = string.lower()
    z = y.replace(" ","")
    if z[::-1] == z:
        return True
    return False
print(palindrome("RacecaR"))
print(palindrome("66racecar77"))
print(palindrome("Madam, I'm Adam"))
print(palindrome("4Satire: Veritas4"))



