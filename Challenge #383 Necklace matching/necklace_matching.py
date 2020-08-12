def same_necklace(s1, s2):
    if(len(s1) != len(s2)):#the two strings need to at least be the same length
        return 'false'
    elif(s1 == s2):#check if they match
        return 'true'
    else:
        match = s1
        for _ in s1:#a string has as many combinations as it does characters
            last_char = match[-1]
            match = last_char + match[:-1]
            if(match == s2):
                return 'true'
        return 'false'#if no combonations match then return false

print('Enter the first string:')
s1 = input()
print('Enter the second string:')
s2 = input()
print('same_necklace("'+s1+'", "'+s2+'") => '+same_necklace(s1, s2))