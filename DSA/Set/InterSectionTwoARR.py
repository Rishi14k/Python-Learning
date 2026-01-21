def interSection(lst1,lst2):
    s1 = set(lst1)
    s2 = set(lst2)
    interSEC = s1&s2

    return list(interSEC)

print(interSection([1,2,2,1],[2,2]))