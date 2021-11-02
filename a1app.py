"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: Kobe Dickson krd63
Date:   10/2/20 (Reason: Covid)
"""
import a1

def main():
    """
    This main function takes the input from the user the src currency and
    the dst currency and amt to be exchanged.

    It prints the exchanged amount.
    """
    src = input('Enter source currency: ')
    dst = input('Enter target currency: ')
    amt = float(input('Enter original amount: '))

    new_amt = a1.exchange(src, dst, amt)

    print('You can exchange ' + str(amt) + ' ' + src
         + ' for ' + str(new_amt) + ' ' + dst + '.')


main()
