from . import (
    IPv4Regex,
    IPv6Regex
)
import pytest

@pytest.mark.slow
@pytest.mark.skip
def test_ipv4_correct_addresses():
    regex = IPv4Regex().regex

    for i in range(0, 255, 2):
        for j in range(0, 255, 3):
            for k in range(0, 255, 5):
                for m in range(0, 255, 7):
                    assert(regex.match('%s.%s.%s.%s' % (i, j, k, m)))

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

    assert(regex.match('256.1.1.1') == None)
    assert(regex.match('1.256.1.1') == None)
    assert(regex.match('1.1.256.1') == None)
    assert(regex.match('1.1.1.256') == None)

    assert(regex.match('1.-1.1.1') == None)
    assert(regex.match('a1.1.1.1') == None)
    assert(regex.match('`1.1.1.1') == None)
    assert(regex.match('1.1.a1.1') == None)
    assert(regex.match('1.1.1.1a') == None)

