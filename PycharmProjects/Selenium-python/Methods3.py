#methods demo POSITIONAL parameters

def sum_nums(n1=35,n2=10):
    return n1+n2

def check_sum_even_odd(sum):
    if sum % 2 == 0:
        return "even"
    else:
        return "odd"

sum = sum_nums(90)
print(sum)
print(check_sum_even_odd(sum))
