def raise_to_power(base_num,pow_num):
    result = 1
    for index in range(pow_num):#0-pow_num ，not including pow_num
        result = result * base_num

    return result

print(raise_to_power(3,2))