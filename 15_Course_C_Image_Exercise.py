from PIL import Image

words = Image.open('word_matrix.png')
print(words.size)
print(words)

mask = Image.open("mask.png")
print(mask.size)
print(mask)

mask = mask.resize((1015,559))
print(mask.size)

mask.putalpha(200)
print(mask)

words.paste(mask, (0,0), mask)
print(words.show())