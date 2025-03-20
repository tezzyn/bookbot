



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


def sort_dict(dict_of_chars):

    list_of_dicts = []
    solo_dict = {}
    
    # print(list(dict_of_chars), list(dict_of_chars.values()))

    for words in dict_of_chars:

        # print(dict_of_chars[words])

        solo_dict = {words:dict_of_chars[words]}
        if words.isalpha():
            list_of_dicts.append(solo_dict)
        solo_dict = {}
        
    
    

    return list_of_dicts

