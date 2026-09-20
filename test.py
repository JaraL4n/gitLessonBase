def my_two_to_the_power_of_n(n: int):
    result = 1
    i = 0
    while True:
        if i == n:
            break
        else:
            result += result
        i = i + 1
    return result


print(my_two_to_the_power_of_n(0) == 1)
print(my_two_to_the_power_of_n(1) == 2)
print(my_two_to_the_power_of_n(2) == 4)
print(my_two_to_the_power_of_n(8) == 256)
print(my_two_to_the_power_of_n(10) == 1024)
print(my_two_to_the_power_of_n(20) == 1048576)
print(my_two_to_the_power_of_n(30) == 1073741824)