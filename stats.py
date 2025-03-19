



def word_count(content):
    count = 0
    contents = content.split()
    
    for words in contents:
        count += 1

    return f"{count} words found in the document"



def char_count(content):

    count = {}

    content.lower()
    
    for char in content:
        num = content[char]
        count[num] = count[num.count()]
    
    return count
