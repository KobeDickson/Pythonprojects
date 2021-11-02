"""
Test script for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: Kobe Dickson krd63
Date:   10/2/20 (Reason: Covid)
"""

import introcs
import a1

def testA():
    """
    Test procedure for Part A

    This function tests the functions before_space(s) and after_space(s)
    from module a1.py
    Precondition: s is a string with at least one space
    """
    # testing before_space(s)
    introcs.assert_equals(a1.before_space("my string"), "my")
    introcs.assert_equals(a1.before_space("mystring "), "mystring")
    introcs.assert_equals(a1.before_space(" my string"), "")
    introcs.assert_equals(a1.before_space("m y  string"), "m")
    introcs.assert_equals(a1.before_space(" my string "), "")
    introcs.assert_equals(a1.before_space("my string"), "my")

    #testing after_space(s)
    introcs.assert_equals(a1.after_space("my string"), "string")
    introcs.assert_equals(a1.after_space(" my string"), "my string")
    introcs.assert_equals(a1.after_space("mystring "), "")
    introcs.assert_equals(a1.after_space(" mystring"), "mystring")
    introcs.assert_equals(a1.after_space("my strin g "), "strin g ")
    introcs.assert_equals(a1.after_space("m y string "), "y string ")


def testB():
    """
    Test procedure for Part B

    This function tests the functions first_inside_quotes(s), get_src(json),
    get_dst(json) and has_error(json)
    from module a1.py

    """
    #a test with one set of quotes
    actual = a1.first_inside_quotes('A "B C" D')
    expected = 'B C'
    introcs.assert_equals(expected, actual)
    #a test with two sets of quotes
    actual = a1.first_inside_quotes('A "B C" D "E F" G')
    expected = 'B C'
    introcs.assert_equals(expected, actual)
    #a test with 3 letters inside the quote
    actual = a1.first_inside_quotes('A "B C D" D"')
    expected = 'B C D'
    introcs.assert_equals(expected, actual)

    #a test for bitcoin and euros
    actual = a1.get_src('{ "src":"1 Bitcoin", "dst":"9916.0137 Euros", \
    "valid":true, "err":"" }')
    expected = '1 Bitcoin'
    introcs.assert_equals(expected, actual)
    #a test for currency input
    actual = a1.get_src('{ "src":"", "dst":"", "valid":false, "err":\
    "Currency amount is invalid." }')
    expected = ''
    introcs.assert_equals(expected, actual)
    #a test for Namibian dollars and Lesotho Maloti
    actual = a1.get_src('{ "src":"2 Namibian Dollars", "dst": \
    "2 Lesotho Maloti", "valid":true, "err":"" }')
    expected = '2 Namibian Dollars'
    introcs.assert_equals(expected, actual)

    #a test for Euros and Bitcoin
    actual = a1.get_dst('{ "src":"1 Bitcoin", "dst":"9916.0137 Euros", \
    "valid":true, "err":"" }')
    expected = '9916.0137 Euros'
    introcs.assert_equals(expected, actual)
    #a test for currency input
    actual = a1.get_dst('{ "src":"2 Namibian Dollars", "dst":\
    "2 Lesotho Maloti", "valid":true, "err":"" }')
    expected = '2 Lesotho Maloti'
    introcs.assert_equals(expected, actual)
    #a test for Namibian dollars and Lesotho Maloti
    actual = a1.get_dst('{ "src":"", "dst":"", "valid":false, "err":\
    "Currency amount is invalid." }')
    expected = ''
    introcs.assert_equals(expected, actual)

    #a test to see if there is an error in exchange
    actual = a1.has_error('{ "src":"1 Bitcoin", "dst":"9916.0137 Euros", \
    "valid":true, "err":"" }')
    expected = False
    introcs.assert_equals(expected, actual)
    #a test to look for error in exchange rates
    actual = a1.has_error('{ "src":"2 Namibian Dollars", "dst":\
    "2 Lesotho Maloti", "valid":true, "err":"" }')
    expected = False
    introcs.assert_equals(expected, actual)
    #a test to make sure errors are reported right
    actual = a1.has_error('{ "src":"", "dst":"", "valid":false, "err":\
    "Currency amount is invalid." }')
    expected = True
    introcs.assert_equals(expected, actual)

def testC():
    """
    Test procedure for Part C
    This function tests the functions currency_response(old, new, amt)
    from a1.py module

    """
    #a test for the old amount USD and new amt CUP
    actual = a1.currency_response('USD', 'CUP', 2.5)
    expected = '{ "src":"2.5 United States Dollars", "dst":\
    "64.375 Cuban Pesos", "valid":true, "err":"" }'
    introcs.assert_equals(expected, actual)
#a test for the old amount AED and new amt USD
    actual = a1.currency_response('AED', 'USD', 23.3)
    expected = '{ "src":"23.3 United Arab Emirates Dirhams", \
    "dst":"6.3436729757625 United States Dollars", "valid":true, "err":"" }'
    introcs.assert_equals(expected, actual)
#a test for the old amount INR and new amt USD
    actual = a1.currency_response('INR', 'USD', 4100)
    expected = '{ "src":"4100 Indian Rupees", "dst":\
    "55.761569621271 United States Dollars", "valid":true, "err":"" }'
    introcs.assert_equals(expected, actual)
#a test for old amount BTC and New ammount INR
    actual = a1.currency_response('BTC', 'INR', 100)
    expected = '{ "src":"100 Bitcoins", "dst":\
    "80211165.134545 Indian Rupees", "valid":true, "err":"" }'
    introcs.assert_equals(expected, actual)


def testD():
    """
    Test procedure for Part D
    This function tests the functions is_currency(code) and
    exchange(old, new, amt) from the a1.py module

    """
    #A test to see if USD is a valid 3-letter currency
    actual = a1.is_currency('USD')
    expected = True
    introcs.assert_equals(expected, actual)
#A test to see if CUP is a valid 3-letter currency
    actual = a1.is_currency('CUP')
    expected = True
    introcs.assert_equals(expected, actual)
#A test to see if AAA is a valid 3-letter currency
    actual = a1.is_currency('AAA')
    expected = False
    introcs.assert_equals(expected, actual)
#A test to see if INR is a valid 3-letter currency
    actual = a1.is_currency('INR')
    expected = True
    introcs.assert_equals(expected, actual)
#A test to see if BTC is a valid 3-letter currency
    actual = a1.is_currency('BTC')
    expected = True
    introcs.assert_equals(expected, actual)
#A test to see if BLF is a valid 3-letter currency
    actual = a1.is_currency('BLF')
    expected = False
    introcs.assert_equals(expected, actual)

#a test for the exchange between USD and CUP
    actual = a1.exchange('USD', 'CUP', 2.5)
    expected = 64.375
    introcs.assert_floats_equal(expected, actual)
#a test for the exchange between INR and USD
    actual = a1.exchange('INR', 'USD', 4100)
    expected = 55.761569621271
    introcs.assert_floats_equal(expected, actual)
#a test for the exchange between BTC and INR
    actual = a1.exchange('BTC', 'INR', 100)
    expected = 80211165.134545
    introcs.assert_floats_equal(expected, actual)
#a test for the exchange between AED and USD
    actual = a1.exchange('AED', 'USD', 23.3)
    expected = 6.3436729757625
    introcs.assert_floats_equal(expected, actual)





testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')
