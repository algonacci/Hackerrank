def swap_case(s):
    num = ""
    for let in s:
        if let.isupper() == True:
            num+=(let.lower())
        else:
            num+=(let.upper())
    return num

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result