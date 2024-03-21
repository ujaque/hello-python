## Funciones de orden superior ##


from functools import reduce


def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5


def sum_two_values_and_one(first_value, second_value):
    return sum_one(first_value + second_value)

print(sum_two_values_and_one(5, 2))
    

def sum_two_values_and_add_value(first_value, second_value, f_sum_one):
    return f_sum_one(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_five))


### Clousures ###

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))


print(sum_ten(5)(1))

## built-in high order functions ##

numbers = [2, 5, 10, 21, 3, 30]

### map ###

def mutiply_two(number):
    return number * 2

result = list(map(mutiply_two, numbers))

print(result)

result2 = list(map(lambda number: number * 2, numbers))

print(result2)

## Filter ##

def filter_greater_than_ten(number):
    if number > 10:
        return True
    else:
        return False


result_filter = list(filter(filter_greater_than_ten,numbers))

print(result_filter)


result_filter_lambda = list(filter(lambda number: number > 10,numbers))

print(result_filter_lambda)

## Reduce ##

2, 5, 10, 21, 3, 30]

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values,numbers))