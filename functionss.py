def fib(n):
    a, b = 0,1
    while a<n:
        print(a, end=' ')
        a,b = b, a+b
    print('')
# fib(5)

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a,b = b, a+b
    return result
# f100 = fib2(100)
# print(f100)

def ask_ok(prompt, retries=4, reminder="Please try againa!"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries -1
        if retries < 0:
            raise ValueError('invalid user repsonse')
        # print(reminder)
        
# print(ask_ok('ask for ok?'))
