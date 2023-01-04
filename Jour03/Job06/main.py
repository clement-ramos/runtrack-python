alphabet = "abcdefghijklmnopqrstuvwxyz" * 10

i = 1

while i <= len(alphabet):
    print(alphabet[:i])
    alphabet = alphabet[i:]
    i += 1
