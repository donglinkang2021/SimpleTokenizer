import pytest
from .utils import unpack

# a few strings to test the tokenizers on
test_strings = [
    "", # empty string
    "?", # single character
    "hello world!!!? (안녕하세요!) lol123 😉", # fun small string
    "FILE:taylorswift.txt", # FILE: is handled as a special string in unpack()
    "FILE:llama.txt", 
    "FILE:special.txt", 
]

    
import simpletokenizer.unicode.tokenizer as unicode_tokenizer
@pytest.mark.parametrize("text", test_strings)
def test_encode_decode_identity(text):
    text = unpack(text)
    ids = unicode_tokenizer.encode(text)
    decoded = unicode_tokenizer.decode(ids)
    assert text == decoded