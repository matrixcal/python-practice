
wordlist=["hello","hi","This","Is","shailesh"]
count=0
char_count=0
char_freq={}
for word in wordlist:
    for char1 in word:
        char_freq[char1]= char_freq.get(char1,0) + 1
        char_count=char_count+1
        print char1
    count=count+1
print "Total words"+ str(count)
print "Total characters"+ str(char_count)
print char_freq.items()
