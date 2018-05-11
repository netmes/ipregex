import re

class IPv4Regex:
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
    before regular expression is compiled. Since :meth:`str.format` will be
    used for formatting, curly braces should be escaped ({{ }}) if they are
    meant to be used for regular expression. This is not needed for default
    value as it does not include any curly braces in final regular expression.
    """
    re_str = r'(?:{o}\.{o}\.{o}\.{o})'

    """Compiled regex. Lazily initialized by :meth:`re`."""
    _re = None

    """Receives no parameters and does nothing."""
    def __init__(self):
        pass

    def compile(self):
        self._re = re.compile(self.re_str.format(o=self.octet_str))

    @property
    def re(self):
        self.compile()
        self.re  = self._initialized_re
        return self._re

    @property
    def _initialized_re(self):
        return self._re

class IPv6Regex:
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

    .. note:: Double curly braces used here are to denote they are not format
              identifiers, as they are part of regular expression. i.e. They
              are escaped.
    """
    re_str = (
        r'(?:'                           # begin non-capturing group
        r'(?:{x}:){{7}}{x}'              # 8 hextets
        r'|(?:{x}:){{6}}(?::{x}){{0,1}}' # or 6 hextets, 0-1 hextets after ::
        r'|(?:{x}:){{5}}(?::{x}){{0,2}}' # or 5 hextets, 0-2 hextets after ::
        r'|(?:{x}:){{4}}(?::{x}){{0,3}}' # or 4 hextets, 0-3 hextets after ::
        r'|(?:{x}:){{3}}(?::{x}){{0,4}}' # or 3 hextets, 0-4 hextets after ::
        r'|(?:{x}:){{2}}(?::{x}){{0,5}}' # or 2 hextets, 0-5 hextets after ::
        r'|(?:{x}:){{1}}(?::{x}){{0,6}}' # or 1 hextet,  0-6 hextets after ::
        r'|:(?::{x}){{1,7}}'             # or 1-7 hextets after ::
        r'|::'                           # or no hextets at all
        r')'                             # end non-capturing group
    ).format(x=hextet_str)

    """Compiled regex. Lazily initialized by :meth:`re`."""
    _re = None

    """Constructor receives no parameters and does nothing."""
    def __init__(self):
        pass

    def compile(self):
        self._re = re.compile(self.re_str.format(x=self.hextet_str))

    @property
    def re(self):
        self.compile()
        self.re  = self._initialized_re
        return self._re

    @property
    def _initialized_re(self):
        return self._re

