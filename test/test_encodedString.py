from unittest import TestCase

from lib.encodings import EncodedString

class TestEncodedString(TestCase):

    def test_decode(self):
        testcase = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        encodedObj = EncodedString(testcase, format='hex')
        encodedObj.decode('base64')
        assert encodedObj.payload == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

