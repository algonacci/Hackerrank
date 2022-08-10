def minion_game(s):
    # your code goes here
    vowel = 'aiueo'.upper()
    strl = len(s)
    kevin = sum(strl-i for i in range(strl) if s[i] in vowel)
    stuart = strl*(strl+1)/2 - kevin
    
    if kevin == stuart:
        print('Draw')
    elif kevin > stuart:
        print("Kevin %d" % kevin)
    else:
        print("Stuart %d" % stuart)
    
if __name__ == '__main__':
    s = input()
    minion_game(s)