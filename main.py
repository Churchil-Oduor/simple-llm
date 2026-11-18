import numpy as np
from tokenizer import CharTokenizer

text = open("input.txt", encoding="utf-8").read()
tok = CharTokenizer(text)
data = np.array(tok.encode(text), dtype=np.int64)

np.save("train_ids.npy", data)
print(f"Saved {len(data):,} tokens, vocab size {tok.vocab_size}")
print(f"{tok.decode(data[:100])}")
