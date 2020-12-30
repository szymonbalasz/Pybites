import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        self.name = name
        if not re.match(r'.*\.[a-z]{2,3}$', self.name):
            raise DomainException
        
    # next add a __str__ method and write 2 class methods
    # called parse_from_url and parse_from_email to construct domains
    # from an URL and email respectively

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def parse_url(self, s):
        sub_s = re.findall(r'//(.*\.[a-z]+)/', s)
        if not sub_s:
            return Domain(re.findall(r'//(.*\.[a-z]+)', s)[0])
        while sub_s:
            s = sub_s[0]
            sub_s = re.findall(r'//(.*\.[a-z]+)/', s)

        return Domain(s)

    @classmethod
    def parse_email(self, s):
        return Domain(re.findall(r'@(.*\.[a-z]+)', s)[0])


domain = Domain.parse_url("https://pybit.es/get-python-source.html")
print(domain)
