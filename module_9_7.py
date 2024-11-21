
def is_prime(func):
    def wrapper(*args, **kwargs):
        sum = func(*args, **kwargs)
        prime_num_b = True
        if sum <= 1:
            prime_num_b = False
        for i in range(2, int(sum ** 0.5) + 1):
            if sum % i == 0:
                prime_num_b = False
        if prime_num_b:
            print("Простое")
        else:
            print("Составное")
        return sum
    return wrapper




@is_prime
def sum_three(*args):
    sum = 0
    for i in args:
        if isinstance(i, int):
            sum += i
    return sum


result = sum_three(2, 3, 7)
print(result)
