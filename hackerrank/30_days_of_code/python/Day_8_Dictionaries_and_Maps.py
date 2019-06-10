# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {key: value for key, value in name_numbers}

while True:
    try:
        name = input()
        if name in phone_book:
            print('{0}={1}'.format(name, phone_book[name]))
        else:
            print('Not found')
    except:
        break
