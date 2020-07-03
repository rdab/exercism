
def factors(number):
    return (v for v in range(1, number) if number % v == 0)

def classify(number):
    if number < 1:
        raise ValueError('Not a valid natural number')
    aliquot = sum(factors(number))
    if aliquot == number:
        return 'perfect'
    elif aliquot > number:
        return 'abundant'
    return 'deficient'
