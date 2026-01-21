def groupAnagram(str):
    dict1 = {}

    def sortedString(s):
        s1=list(s)
        s1.sort()
        return "".join(s1)

    for s in str:
        key = sortedString(s)
        if key in dict1:
            dict1[key].append(s)
        else:
            dict1[key] = [s]
    
    return list(dict1.values())


print(groupAnagram(["eat","tea","tan","ate","nat","bat"]))