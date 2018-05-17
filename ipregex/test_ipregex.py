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

@pytest.mark.exhaustive
def test_ipv4_exhaust_addresses_with_boundary_segments():
    regex = IPv4Regex().regex

    correct_segments = [
        '0', '9', '10', '99', '100', '199', '200', '249', '250', '255'
    ]

    ip_list = itertools.product(correct_segments, repeat=4)

    for ip in ip_list:
        ip_str = '.'.join(ip)
        assert(regex.match(ip_str))

def test_ipv4_manual_correct_addresses():
    regex = IPv4Regex().regex

    assert(regex.match('0.0.0.0'))
    assert(regex.match('1.1.1.1'))
    assert(regex.match('11.11.11.11'))
    assert(regex.match('111.111.111.111'))
    assert(regex.match('222.222.222.222'))
    assert(regex.match('250.250.250.250'))
    assert(regex.match('255.255.255.255'))

    assert(regex.match('1.11.111.222'))
    assert(regex.match('222.111.11.1'))
    assert(regex.match('1.11.111.250'))
    assert(regex.match('250.111.11.1'))
    assert(regex.match('1.11.222.250'))
    assert(regex.match('250.222.11.1'))

def test_ipv4_manual_incorrect_addresses():
    regex = IPv4Regex().regex

    assert(not regex.match('1'))
    assert(not regex.match('1.1'))
    assert(not regex.match('1.1.1'))
    assert(not regex.match('1.1.1.1.'))
    assert(not regex.match('.1.1.1.1'))
    assert(not regex.match('.1.1.1.1.'))
    assert(not regex.match('1...'))
    assert(not regex.match('1.1..'))
    assert(not regex.match('1.1.1.'))
    assert(not regex.match('.1.1.1'))
    assert(not regex.match('..1.1'))
    assert(not regex.match('...1'))
    assert(not regex.match('1..'))

    assert(not regex.match('1,1,1,1'))
    assert(not regex.match('1-1-1-1'))

    assert(not regex.match('256.1.1.1'))
    assert(not regex.match('1.256.1.1'))
    assert(not regex.match('1.1.256.1'))
    assert(not regex.match('1.1.1.256'))

    assert(not regex.match('1.-1.1.1'))
    assert(not regex.match('a1.1.1.1'))
    assert(not regex.match('`1.1.1.1'))
    assert(not regex.match('1.1.a1.1'))
    assert(not regex.match('1.1.1.1a'))

@pytest.mark.exhaustive
def test_ipv6_exhaust_addresses_with_boundary_segments():
    regex = IPv6Regex().regex

    correct_segments = [
        '0', 'f', '10', 'ff', '100', 'fff', '1000', 'ffff'
    ]

    for num_octets in range(9):
        if num_octets == 0:
            assert(regex.match('::'))
        else:
            ip_list = itertools.product(correct_segments, repeat=num_octets)
            if num_octets == 8:
                for ip in ip_list:
                    ip_str = ':'.join(ip)
                    assert(regex.match(ip_str))
            else:
                for ip in ip_list:
                    for num_octets_before_compression in range(num_octets+1):
                        ip_str = ':'.join(ip[:num_octets_before_compression])
                        ip_str += '::'
                        ip_str += ':'.join(ip[num_octets_before_compression:])
                        assert(regex.match(ip_str))

def test_ipv6_manual_correct_addresses():
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

    # Boundaries without leading zeros
    assert(regex.match('0:0:0:0:0:0:0:0'))
    assert(regex.match('f:f:f:f:f:f:f:f'))
    assert(regex.match('10:10:10:10:10:10:10:10'))
    assert(regex.match('ff:ff:ff:ff:ff:ff:ff:ff'))
    assert(regex.match('100:100:100:100:100:100:100:100'))
    assert(regex.match('fff:fff:fff:fff:fff:fff:fff:fff'))
    assert(regex.match('1000:1000:1000:1000:1000:1000:1000:1000'))
    assert(regex.match('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff'))

    # Boundaries with leading zeros
    assert(regex.match('00:00:00:00:00:00:00:00'))
    assert(regex.match('000:000:000:000:000:000:000:000'))
    assert(regex.match('0f:0f:0f:0f:0f:0f:0f:0f'))
    assert(regex.match('00f:00f:00f:00f:00f:00f:00f:00f'))
    assert(regex.match('000f:000f:000f:000f:000f:000f:000f:000f'))
    assert(regex.match('010:010:010:010:010:010:010:010'))
    assert(regex.match('0010:0010:0010:0010:0010:0010:0010:0010'))
    assert(regex.match('0ff:0ff:0ff:0ff:0ff:0ff:0ff:0ff'))
    assert(regex.match('00ff:00ff:00ff:00ff:00ff:00ff:00ff:00ff'))
    assert(regex.match('0100:0100:0100:0100:0100:0100:0100:0100'))
    assert(regex.match('0fff:0fff:0fff:0fff:0fff:0fff:0fff:0fff'))

    # Collapsed versions
    assert(regex.match('::'))
    assert(regex.match('::1111:1111:1111:1111:1111:1111:1111'))
    assert(regex.match('1111::1111:1111:1111:1111:1111:1111'))
    assert(regex.match('1111:1111::1111:1111:1111:1111:1111'))
    assert(regex.match('1111:1111:1111::1111:1111:1111:1111'))
    assert(regex.match('1111:1111:1111:1111::1111:1111:1111'))
    assert(regex.match('1111:1111:1111:1111:1111::1111:1111'))
    assert(regex.match('1111:1111:1111:1111:1111:1111::1111'))
    assert(regex.match('1111:1111:1111:1111:1111:1111:1111::'))

    assert(regex.match('::0:0:0:0:0:0:0'))
    assert(regex.match('0::0:0:0:0:0:0'))
    assert(regex.match('0:0::0:0:0:0:0'))
    assert(regex.match('0:0:0::0:0:0:0'))
    assert(regex.match('0:0:0:0::0:0:0'))
    assert(regex.match('0:0:0:0:0::0:0'))
    assert(regex.match('0:0:0:0:0:0::0'))
    assert(regex.match('0:0:0:0:0:0:0::'))

    assert(regex.match('::1:1:1:1:1:1:1'))
    assert(regex.match('1::1:1:1:1:1:1'))
    assert(regex.match('1:1::1:1:1:1:1'))
    assert(regex.match('1:1:1::1:1:1:1'))
    assert(regex.match('1:1:1:1::1:1:1'))
    assert(regex.match('1:1:1:1:1::1:1'))
    assert(regex.match('1:1:1:1:1:1::1'))
    assert(regex.match('1:1:1:1:1:1:1::'))

    assert(regex.match('::f:f:f:f:f:f:f'))
    assert(regex.match('f::f:f:f:f:f:f'))
    assert(regex.match('f:f::f:f:f:f:f'))
    assert(regex.match('f:f:f::f:f:f:f'))
    assert(regex.match('f:f:f:f::f:f:f'))
    assert(regex.match('f:f:f:f:f::f:f'))
    assert(regex.match('f:f:f:f:f:f::f'))
    assert(regex.match('f:f:f:f:f:f:f::'))

    # Mixed
    assert(regex.match('0:01:022:0333:a:bb:ccc:ddd'))
    assert(regex.match('0:01:022:0333:a:bb:ccc::'))
    assert(regex.match('0:01:022:0333:a::ccc:ddd'))

def test_ipv6_column_errors():
    regex = IPv6Regex().regex

    assert(not regex.match(':'))
    assert(not regex.match(':::'))
    assert(not regex.match('::::'))
    assert(not regex.match(':::::'))
    assert(not regex.match('::::::'))
    assert(not regex.match(':::::::'))
    assert(not regex.match('::::::::'))
    assert(not regex.match(':::::::::'))
    assert(not regex.match('::::::::::'))

    # Compression with 8 hextets
    assert(not regex.match('1:1:1:1:1:1:1:1::'))
    assert(not regex.match('1:1:1:1:1:1:1::1'))
    assert(not regex.match('1:1:1:1:1:1::1:1'))
    assert(not regex.match('1:1:1:1:1::1:1:1'))
    assert(not regex.match('1:1:1:1::1:1:1:1'))
    assert(not regex.match('1:1:1::1:1:1:1:1'))
    assert(not regex.match('1:1::1:1:1:1:1:1'))
    assert(not regex.match('1::1:1:1:1:1:1:1'))
    assert(not regex.match('::1:1:1:1:1:1:1:1'))
    assert(not regex.match('11:11:11:11:11:11:11:11::'))
    assert(not regex.match('11:11:11:11:11:11:11::11'))
    assert(not regex.match('11:11:11:11:11:11::11:11'))
    assert(not regex.match('11:11:11:11:11::11:11:11'))
    assert(not regex.match('11:11:11:11::11:11:11:11'))
    assert(not regex.match('11:11:11::11:11:11:11:11'))
    assert(not regex.match('11:11::11:11:11:11:11:11'))
    assert(not regex.match('11::11:11:11:11:11:11:11'))
    assert(not regex.match('::11:11:11:11:11:11:11:11'))
    assert(not regex.match('111:111:111:111:111:111:111:111::'))
    assert(not regex.match('111:111:111:111:111:111:111::111'))
    assert(not regex.match('111:111:111:111:111:111::111:111'))
    assert(not regex.match('111:111:111:111:111::111:111:111'))
    assert(not regex.match('111:111:111:111::111:111:111:111'))
    assert(not regex.match('111:111:111::111:111:111:111:111'))
    assert(not regex.match('111:111::111:111:111:111:111:111'))
    assert(not regex.match('111::111:111:111:111:111:111:111'))
    assert(not regex.match('::111:111:111:111:111:111:111:111'))
    assert(not regex.match('1111:1111:1111:1111:1111:1111:1111:1111::'))
    assert(not regex.match('1111:1111:1111:1111:1111:1111:1111::1111'))
    assert(not regex.match('1111:1111:1111:1111:1111:1111::1111:1111'))
    assert(not regex.match('1111:1111:1111:1111:1111::1111:1111:1111'))
    assert(not regex.match('1111:1111:1111:1111::1111:1111:1111:1111'))
    assert(not regex.match('1111:1111:1111::1111:1111:1111:1111:1111'))
    assert(not regex.match('1111:1111::1111:1111:1111:1111:1111:1111'))
    assert(not regex.match('1111::1111:1111:1111:1111:1111:1111:1111'))
    assert(not regex.match('::1111:1111:1111:1111:1111:1111:1111:1111'))

    # Multiple compressions
    assert(not regex.match('1::1::1'))
    assert(not regex.match('1::1::1:1'))
    assert(not regex.match('1:1:1::1::1'))
    assert(not regex.match('1::1::'))
    assert(not regex.match('::1::1'))
