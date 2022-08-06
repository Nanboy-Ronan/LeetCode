# Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.
# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

from ipaddress import ip_address, IPv6Address
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        try:
            return 'IPv6' if type(ip_address(queryIP)) is IPv6Address else 'IPv4'
        except ValueError:
            return 'Neither'