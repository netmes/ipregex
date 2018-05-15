from . import (
    IPv4Regex,
    IPv6Regex
)
import pytest
import itertools


@pytest.mark.slow
def test_ipv4_exhaust_correct_addresses():
    regex = IPv4Regex().regex

    for i in range(0, 255, 1):
        for j in range(0, 255, 1):
            for k in range(0, 255, 1):
                for m in range(0, 255, 1):
                    assert(regex.match('%s.%s.%s.%s' % (i, j, k, m)))

def test_ipv4_boundary_segments():
    regex = IPv4Regex().regex

    correct_segments = [
        '0', '9', '10', '99', '100', '199', '200', '249', '250', '255'
    ]

    correct_ip_addresses = itertools.product(correct_segments, repeat=4)

    for ip in correct_ip_addresses:
        ip = '.'.join(ip)
        assert(regex.match(ip) != None)


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

def test_ipv6_correct_addresses():
    regex = IPv6Regex().regex

    assert(regex.match('0000:0000:0000:0000:0000:0000:0000:0000'))
    assert(regex.match('1111:1111:1111:1111:1111:1111:1111:1111'))
    assert(regex.match('2222:2222:2222:2222:2222:2222:2222:2222'))
    assert(regex.match('3333:3333:3333:3333:3333:3333:3333:3333'))
    assert(regex.match('4444:4444:4444:4444:4444:4444:4444:4444'))
    assert(regex.match('5555:5555:5555:5555:5555:5555:5555:5555'))
    assert(regex.match('6666:6666:6666:6666:6666:6666:6666:6666'))
    assert(regex.match('7777:7777:7777:7777:7777:7777:7777:7777'))
    assert(regex.match('8888:8888:8888:8888:8888:8888:8888:8888'))
    assert(regex.match('9999:9999:9999:9999:9999:9999:9999:9999'))
    assert(regex.match('aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa'))
    assert(regex.match('bbbb:bbbb:bbbb:bbbb:bbbb:bbbb:bbbb:bbbb'))
    assert(regex.match('cccc:cccc:cccc:cccc:cccc:cccc:cccc:cccc'))
    assert(regex.match('dddd:dddd:dddd:dddd:dddd:dddd:dddd:dddd'))
    assert(regex.match('eeee:eeee:eeee:eeee:eeee:eeee:eeee:eeee'))
    assert(regex.match('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff'))

    # Collapsed versions
    assert(regex.match('::1111:1111:1111:1111:1111:1111:1111'))
    assert(regex.match('1111::1111:1111:1111:1111:1111:1111'))
    assert(regex.match('1111:1111::1111:1111:1111:1111:1111'))
    assert(regex.match('1111:1111:1111::1111:1111:1111:1111'))
    assert(regex.match('1111:1111:1111:1111::1111:1111:1111'))
    assert(regex.match('1111:1111:1111:1111:1111::1111:1111'))
    assert(regex.match('1111:1111:1111:1111:1111:1111::1111'))
    assert(regex.match('1111:1111:1111:1111:1111:1111:1111::'))
    assert(regex.match('::'))

    # With leading zeros

    # Without leading zeros
    assert(regex.match('0:0:0:0:0:0:0:0'))
