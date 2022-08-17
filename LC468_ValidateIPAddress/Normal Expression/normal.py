# Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.
# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.
import re

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
        patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')
        
        chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
        patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')    
        
        if '.' in queryIP:
            return "IPv4" if self.patten_IPv4.match(queryIP) else "Neither" 
        if ':' in queryIP:
            return "IPv6" if self.patten_IPv6.match(queryIP) else "Neither" 
        return "Neither"