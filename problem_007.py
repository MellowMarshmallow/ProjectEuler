def find_nth_prime(n):
    
    # a prime number can only be divisible by one and itself
    # all non prime numbers can be divisible by a prime number (?)

    # keep an array of prime numbers

    # a temp variable that will be compared to the elements of the list

    # if the variable is divisible by an element, it is not prime, thus increment
    # if the variable is able to go through the list without being divisible,
    # then append said number to the list

    # continue this while the length of the list is less than 10,001
    # since we are looking for the 10,001th prime number

    primes = [2]
    number = 3
    is_prime = True

    while len(primes) < n:

        for prime in primes:
            
            if number % prime == 0:
               is_prime = False
               break

        if is_prime:
            primes.append(number)

        is_prime = True
        number += 1

    return primes[-1]

print(find_nth_prime(10001)) # Output: 104743
