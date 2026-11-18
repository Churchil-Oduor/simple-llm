from tokenizer import CharTokenizer

text = open("input.txt", encoding="utf-8").read()
tok = CharTokenizer(text)

print(f"Vocab size {tok.vocab_size}")
sample = text[:200]
ids = tok.encode(sample)
print("First 20 ids:", ids[:20])
print("Round Trip Ok:", tok.decode(ids))
tok.save("vocab.json")
