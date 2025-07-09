text = input()
pattern = input()

# Please write your code here.
result = False
for idx in range(len(text) - len(pattern) + 1):
    test_text = text[idx:(idx+len(pattern))]
    if pattern == test_text:
        result = True
        print(idx)
        break
if not result:
    print(-1)