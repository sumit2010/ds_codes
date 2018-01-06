from collections import defaultdict


def remove_duplicates(s):
    j=-1
    seen=set()
    for ch in s:
        if ch not in seen:
            s[j+1]=ch
            j +=1
            seen.add(ch)
        print s
    print s

# remove_duplicates(['a','b','a'])

def isAnagram(s1,s2):
    charCount=defaultdict(int)
    for ch in s1:
        charCount[ch]+=1

    for ch in s2:
        charCount[ch]-=1
        if charCount[ch]<0:
            return False

    for ch in charCount:
        if charCount[ch]!=0:
            return False


    return True

print isAnagram("abc","bcaa")

