import string

std_base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def hex_lookup(index):
    return std_base64chars[index]


def _hexToBase64(payload):
    # This is a bad way to do this because python doesn't expose. Replace with native code after proving you get it
    hex_buffer = []
    bytestring = '0' + bin(int(payload, 16))[2:]
    start_span =  0
    for ii in range(start_span + 6, len(bytestring), 6):
        hex_index = int(bytestring[start_span:ii], 2)
        hex_buffer.append(hex_lookup(hex_index))
        start_span = ii
    return ''.join(hex_buffer)

class EncodedString():
    hexDecodes = {'base64':_hexToBase64}


    def __init__(self, payload, format=str):
        self.format = format
        self.payload = payload

    def decode(self, toFormat=str):
        if self.format == 'hex':
            try:
                fx = self.hexDecodes[toFormat]
            except KeyError:
                raise(UnhandledFormatError('Cannot convert {} to {}'.format(self.format, toFormat)))

        self.format = toFormat
        self.payload = fx(self.payload)
        return self.payload


class UnhandledFormatError(Exception):
    pass

