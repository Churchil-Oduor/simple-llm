import json

class CharTokenizer:
    def __init__(self, text: str):
        self.chars = sorted(set(text))
        self.vocab_size = len(set(self.chars))
        self.stoi = {ch: i for i, ch in enumerate(self.chars)}
        self.itos = {i: ch for ch, i in self.stoi.items()}

    def encode(self, s: str) -> list[int]:
        return [self.stoi[c] for c in s]

    def decode(self, ids: list[int]) -> str:
        return "".join(self.itos[i] for i in ids)


    def save(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.chars, f, ensure_ascii=False)

    @classmethod
    def load(cls, path: str):
        with open(path, encoding="utf-8") as f:
            chars = json.load(f)

        tok = cls.__new__(cls)
        tok.chars = chars
        tok.vocab_size = len(chars)
        tok.stoi = {ch : i for i, ch in enumerate(chars)}
        tok.itos = {i: ch for ch, i in tok.stoi.items()}
        return tok



