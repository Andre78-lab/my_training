calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    len_ = len(string)
    len_up = string.upper()
    len_low = string.lower()
    return (len_, len_up, len_low)

def is_contains(string , is_contains):
    count_calls()
    is_cont = True
    for str_is_cont in is_contains:
        if str_is_cont.lower() == string.lower():
            is_cont = True
        else:
            is_cont = False
    return is_cont


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

