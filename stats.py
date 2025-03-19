



def word_count(content):
    count = 0
    contents = content.split()
    
    for words in contents:
        count += 1

    return f"{count} words found in the document"



def char_count(content):
    content = content.lower()

    dchar = {}

    for words in content:
        if words in dchar:
            dchar[words] += 1
        else:
            dchar[words] = 1
            
    return dchar
