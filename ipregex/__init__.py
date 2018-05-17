import re

class IPRegexBase(object):
    """Compiled regex. Lazily initialized by :meth:`regex`."""
    _regex = None

    """Initiate class. Currently empty."""
    def __init__(self):
        pass

    def compile(self):
        raise NotImplementedError('This method should have been overriden.')

    """Return compiled regular expression. Compile regular expression if this
    is the first call. :meth:`self._initialized_regex` replace this function
    after first call to implement lazy initialization.
    """
    @property
    def regex(self):
        self.compile()
        self.re = self._initialized_regex
        return self._regex

    """Return compiled regular expression. Replace :meth:`regex` after regex
    compilation.
    """
    @property
    def _initialized_regex(self):
        return self._regex

class IPv4Regex(IPRegexBase):
    """Regular expression string for each byte of IPv4 address represented by
    an unsigned 8-bit integer.
    """
    octet_str  = (
        r'(?:'          # begin non-capturing group
        r'[0-9]'        # matches 0..9
        r'|[1-9][0-9]'  # or matches 10..99
        r'|1[0-9][0-9]' # or matches 100..199
        r'|2[0-4][0-9]' # or matches 200..249
        r'|25[0-5]'     # or matches 250..255
        r')'            # end non-capturing group
    )

    """IPv4 regular expression string.

    `{o}` occurences in this string will be replaced with :attr:`octet_str`
    before regular expression is compiled.

    .. note:: Double curly braces should be used instead of single if curly
              brace is meant for regular expression. This is because curly
              braces are used by `str.format`, which is used to replace octets
              in this string before creating regular expression.
    """
    re_str = r'^(?:{o}\.{o}\.{o}\.{o})$'


    """Initate class. Call constructor of base class."""
    def __init__(self):
        super(IPv4Regex, self).__init__()
        pass

    """Replace octets in regular expression string and compile regular
    expression.
    """
    def compile(self):
        self._regex = re.compile(self.re_str.format(o=self.octet_str))


class IPv6Regex(IPRegexBase):
    """Regular expression string for each 2 bytes of IPv6 address represented
    by 1-4 hexadecimal characters.

    .. note:: Default hextet defition is a loose one, meaning that it accepts
              IPv6 addresses which are valid, but not well-defined. See RFC
              5952 for definition of well-defined IPv6 addresses.
    """
    hextet_str = (
        r'(?:'           # begin non-capturing group
        r'[0-9a-f]{1,4}' # 1-4 digits hex
        r')'             # end non-capturing group
    )

    """IPv6 regular expression string.

    `{x}` occurences in this string will be replaced with :attr:`hextet_str`
    before regular expression is compiled.

    .. note:: Double curly braces should be used instead of single if curly
              brace is meant for regular expression. This is because curly
              braces are used by `str.format`, which is used to replace hextets
              in this string before creating regular expression.
    """
    re_str = (
        r'^'
        r'(?:'                           # begin non-capturing group
        r'(?:{x}:){{7}}{x}'              # 8 hextets
        r'|(?:{x}:){{1,7}}:'             # or 1-7 hextets ::
        r'|(?:{x}:){{6}}(?::{x}){{1}}'   # or 6 hextets :: 1 hextet
        r'|(?:{x}:){{5}}(?::{x}){{1,2}}' # or 5 hextets :: 1-2 hextets
        r'|(?:{x}:){{4}}(?::{x}){{1,3}}' # or 4 hextets :: 1-3 hextets
        r'|(?:{x}:){{3}}(?::{x}){{1,4}}' # or 3 hextets :: 1-4 hextets
        r'|(?:{x}:){{2}}(?::{x}){{1,5}}' # or 2 hextets :: 1-5 hextets
        r'|(?:{x}:){{1}}(?::{x}){{1,6}}' # or 1 hextet  :: 1-6 hextets
        r'|:(?::{x}){{1,7}}'             # or :: 1-7 hextets
        r'|::'                           # or no hextets at all
        r')'                             # end non-capturing group
        r'$'
    )

    """Initate class. Call constructor of base class."""
    def __init__(self):
        super(IPv6Regex, self).__init__()
        pass

    """Replace hextets in regular expression string and compile regular
    expression.
    """
    def compile(self):
        self._regex = re.compile(self.re_str.format(x=self.hextet_str))

