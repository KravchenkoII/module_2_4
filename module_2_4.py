numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if int(numbers[i]) == 1:
        continue
    else:
        flag = True
        for k in range(2,numbers[i]):
            if numbers[i] % k == 0:
                flag = False
                break
        if flag:
                primes.append(numbers[i])
        else:
                not_primes.append(numbers[i])
print('Primes: ', primes)
print('Not Primes: ', not_primes)

