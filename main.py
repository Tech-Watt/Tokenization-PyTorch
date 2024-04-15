from torchtext.data.utils import get_tokenizer


text = 'With PyTorch Tokenization becomes easy and everyone can do it'
tokenizer = get_tokenizer('basic_english')
tokens = tokenizer(text)
print(tokens)