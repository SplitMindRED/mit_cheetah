"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class gamepad_lcmt(object):
    __slots__ = ["leftBumper", "rightBumper", "leftTriggerButton", "rightTriggerButton", "back", "start", "a", "b", "x", "y", "leftStickButton", "rightStickButton", "leftTriggerAnalog", "rightTriggerAnalog", "leftStickAnalog", "rightStickAnalog"]

    __typenames__ = ["int32_t", "int32_t", "int32_t", "int32_t", "int32_t", "int32_t", "int32_t", "int32_t", "int32_t", "int32_t", "int32_t", "int32_t", "float", "float", "float", "float"]

    __dimensions__ = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, [2], [2]]

    def __init__(self):
        self.leftBumper = 0
        self.rightBumper = 0
        self.leftTriggerButton = 0
        self.rightTriggerButton = 0
        self.back = 0
        self.start = 0
        self.a = 0
        self.b = 0
        self.x = 0
        self.y = 0
        self.leftStickButton = 0
        self.rightStickButton = 0
        self.leftTriggerAnalog = 0.0
        self.rightTriggerAnalog = 0.0
        self.leftStickAnalog = [ 0.0 for dim0 in range(2) ]
        self.rightStickAnalog = [ 0.0 for dim0 in range(2) ]

    def encode(self):
        buf = BytesIO()
        buf.write(gamepad_lcmt._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">iiiiiiiiiiiiff", self.leftBumper, self.rightBumper, self.leftTriggerButton, self.rightTriggerButton, self.back, self.start, self.a, self.b, self.x, self.y, self.leftStickButton, self.rightStickButton, self.leftTriggerAnalog, self.rightTriggerAnalog))
        buf.write(struct.pack('>2f', *self.leftStickAnalog[:2]))
        buf.write(struct.pack('>2f', *self.rightStickAnalog[:2]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != gamepad_lcmt._get_packed_fingerprint():
            raise ValueError("Decode error")
        return gamepad_lcmt._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = gamepad_lcmt()
        self.leftBumper, self.rightBumper, self.leftTriggerButton, self.rightTriggerButton, self.back, self.start, self.a, self.b, self.x, self.y, self.leftStickButton, self.rightStickButton, self.leftTriggerAnalog, self.rightTriggerAnalog = struct.unpack(">iiiiiiiiiiiiff", buf.read(56))
        self.leftStickAnalog = struct.unpack('>2f', buf.read(8))
        self.rightStickAnalog = struct.unpack('>2f', buf.read(8))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if gamepad_lcmt in parents: return 0
        tmphash = (0x37c71cc8957b05cf) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if gamepad_lcmt._packed_fingerprint is None:
            gamepad_lcmt._packed_fingerprint = struct.pack(">Q", gamepad_lcmt._get_hash_recursive([]))
        return gamepad_lcmt._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
