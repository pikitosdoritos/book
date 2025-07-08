import logging

logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Початок програми')

def factorial(n):
    logging.debug('Початок factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i = ' + str(i) + ', total = ' + str(total))
    logging.debug('Кінець factorial(%s%%)' % (n))
    return total    

print(factorial(5))
logging.debug('Кінець програми')