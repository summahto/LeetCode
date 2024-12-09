

if __name__ == '__main__':

    leaders = ['elon', 'Jeff', 'Tim']

    # find a substring in a string
    s = 'abcde'
    print(s.find('def'))
    print('abc' in s)


    # for-else loop
    for leader in leaders:
        if leader == 'elon':
            print('elon is a leader')
            break
    else:
        print('not found elon')
