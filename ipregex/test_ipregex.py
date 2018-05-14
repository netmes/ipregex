from . import (
    IPv4Regex,
    IPv6Regex
)
import pytest


@pytest.mark.slow
def test_ipv4_exhaust_correct_addresses():
    regex = IPv4Regex().regex

    for i in range(0, 255, 1):
        for j in range(0, 255, 1):
            for k in range(0, 255, 1):
                for m in range(0, 255, 1):
                    assert(regex.match('%s.%s.%s.%s' % (i, j, k, m)))


def test_ipv4_correct_addresses():
    regex = IPv4Regex().regex

    assert(regex.match('0.0.0.0') != None)
    assert(regex.match('1.1.1.1') != None)
    assert(regex.match('11.11.11.11') != None)
    assert(regex.match('111.111.111.111') != None)
    assert(regex.match('222.222.222.222') != None)
    assert(regex.match('250.250.250.250') != None)
    assert(regex.match('255.255.255.255') != None)

    assert(regex.match('1.11.111.222') != None)
    assert(regex.match('222.111.11.1') != None)
    assert(regex.match('1.11.111.250') != None)
    assert(regex.match('250.111.11.1') != None)
    assert(regex.match('1.11.222.250') != None)
    assert(regex.match('250.222.11.1') != None)


def test_ipv4_incorrect_addresses():
    regex = IPv4Regex().regex

    assert(regex.match('1')         == None)
    assert(regex.match('1.1')       == None)
    assert(regex.match('1.1.1')     == None)
    assert(regex.match('1.1.1.1.')  == None)
    assert(regex.match('.1.1.1.1')  == None)
    assert(regex.match('.1.1.1.1.') == None)
    assert(regex.match('1...')      == None)
    assert(regex.match('1.1..')     == None)
    assert(regex.match('1.1.1.')    == None)
    assert(regex.match('.1.1.1')    == None)
    assert(regex.match('..1.1')     == None)
    assert(regex.match('...1')      == None)
    assert(regex.match('1..')       == None)

    assert(regex.match('1,1,1,1')   == None)
    assert(regex.match('1-1-1-1')   == None)

    assert(regex.match('256.1.1.1') == None)
    assert(regex.match('1.256.1.1') == None)
    assert(regex.match('1.1.256.1') == None)
    assert(regex.match('1.1.1.256') == None)

    assert(regex.match('1.-1.1.1') == None)
    assert(regex.match('a1.1.1.1') == None)
    assert(regex.match('`1.1.1.1') == None)
    assert(regex.match('1.1.a1.1') == None)
    assert(regex.match('1.1.1.1a') == None)

def test_ipv6_incorrect_addresses():
    pass
