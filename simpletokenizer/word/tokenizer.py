from collections import Counter
from typing import List, Union
import json

class Tokenizer(object):
    """Simple Tokenizer wrapper."""
    def __init__(self, reserved_tokens=None):
        if reserved_tokens is None:
            reserved_tokens = []
        self.itos = ['<unk>'] + reserved_tokens
        self.stoi = {token: idx for idx, token in enumerate(self.itos)}

    def add_token(self, token: str):
        if token not in self.stoi:
            self.itos.append(token)
            self.stoi[token] = len(self.itos) - 1    

    def __len__(self):
        return len(self.itos)
    
    def __call__(self, words: List[str]) -> List[int]:
        return self.encode(words)
            
    def decode(self, indices: List[int]) -> List[str]:
        return [self.itos[index] for index in indices]
    
    def encode(self, tokens: Union[List[str], str]) -> List[int]:
        return [
            self.stoi[token] if token in self.stoi else self.stoi['<unk>'] 
            for token in tokens
        ]
    
    def save(self, file_path: str):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.stoi, ensure_ascii=False, indent=4))

    @staticmethod
    def load(file_path: str):
        with open(file_path, 'r', encoding='utf-8') as f:
            stoi:dict = json.load(f)
        vocab = Tokenizer()
        vocab.stoi = stoi
        vocab.itos = list(stoi.keys())
        return vocab
    

def build_vocab(data_path, min_freq=0, reserved_tokens=['<pad>']):
    counter = Counter()
    vocab = Tokenizer(reserved_tokens)
    with open(data_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        for word in line.strip().split():
            counter.update(word)
    
    _token_freqs = sorted(
        counter.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for token, freq in _token_freqs:
        if freq < min_freq:
            print(f"Break at token: {token}, freq: {freq} < min_freq: {min_freq}")
            break
        vocab.add_token(token)
        print(f"Add token: {token}, freq: {freq}")
    
    return vocab