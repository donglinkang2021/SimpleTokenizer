from typing import List

# encodings
UTF8 = 'utf-8'
UTF16 = 'utf-16'
UTF32 = 'utf-32'

def encode(text: str) -> List[int]:
    return list(text.encode(UTF8))

def decode(tokens: List[int]) -> str:
    return bytes(tokens).decode(UTF8)

if __name__ == '__main__':
    text = "hello123!!!? (안녕하세요!) 😉"
    print(f"Text(UTF-8) [{len(text)}chr, {len(text.encode('utf-8'))}byte]:")
    print(text)
    tokens = encode(text)
    print("Text --encoded--> Tokens:")
    print(f"Tokens(List[int]) [{len(tokens)}int]:")
    print(tokens)
    decoded_text = decode(tokens)
    print("Tokens --decoded--> Text:")
    print(decoded_text)
    assert text == decoded_text

# python -m simpletokenizer.unicode.tokenizer