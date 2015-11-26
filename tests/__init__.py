import unittest
from requests_oembed import (endpoints, get_endpoint, get_oembed, gist, oembed)

class TestOEmbed(unittest.TestCase):

    def test_embed(self):

        valid_tags = ["iframe","blockquote","script"]
        
        for service in endpoints:
            embed_string = oembed(endpoints[service]['example'])
            self.assertTrue(any(tag in embed_string for tag in valid_tags))