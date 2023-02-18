#pylint:disable=C0209
#pylint:disable=C0114
db = {}
print('\t\tKey-Value Database \n')
while True:
    print('  What do you want to do?\n')
    print('  (1) Enter P to [P]ut' + '\n  (2) Enter G to [G]et' + '\n  (3) Enter L to [L]ist')
    print('\n  Or enter Q to [Q]uit')
    action = input("\n  Choice : ")
    if action == 'P':
        k = input('\n  Enter key: ')
        d = input('\n  Enter data: ')
        db[k] = d
    elif action == 'G':
        k = input('\n  Enter key: ')
        if not k in db:
            print('No such key')
        else:
            print('\n  Your data: %s' % db[k])
    elif action == 'L':
        print('\n  DB contents:')
        print(db)
    elif action == 'Q':
        print('Bye')
        break
