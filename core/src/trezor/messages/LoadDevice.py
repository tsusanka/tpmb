# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .HDNodeType import HDNodeType

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class LoadDevice(p.MessageType):
    MESSAGE_WIRE_TYPE = 13

    def __init__(
        self,
        mnemonics: List[str] = None,
        node: HDNodeType = None,
        pin: str = None,
        passphrase_protection: bool = None,
        language: str = None,
        label: str = None,
        skip_checksum: bool = None,
        u2f_counter: int = None,
    ) -> None:
        self.mnemonics = mnemonics if mnemonics is not None else []
        self.node = node
        self.pin = pin
        self.passphrase_protection = passphrase_protection
        self.language = language
        self.label = label
        self.skip_checksum = skip_checksum
        self.u2f_counter = u2f_counter

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('mnemonics', p.UnicodeType, p.FLAG_REPEATED),
            2: ('node', HDNodeType, 0),
            3: ('pin', p.UnicodeType, 0),
            4: ('passphrase_protection', p.BoolType, 0),
            5: ('language', p.UnicodeType, 0),  # default=english
            6: ('label', p.UnicodeType, 0),
            7: ('skip_checksum', p.BoolType, 0),
            8: ('u2f_counter', p.UVarintType, 0),
        }