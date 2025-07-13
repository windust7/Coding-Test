word1 = list(input())
word2 = list(input())

# Please write your code here.
word1.sort()
word2.sort()
if word1 == word2:
    print("Yes")
else:
    print("No")