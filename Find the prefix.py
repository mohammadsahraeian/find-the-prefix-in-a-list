
my_list = ['flower', 'flowing', 'flowered', 'flown', 'flown', 'flowery', 'floral']
# suppose first index as a prefix
prefix = string[0]
# Create a loop to iterate my_list
for word in my_list[1:]:
    if word != prefix:
        prefix = word[:len(prefix)-1]
print(prefix)
