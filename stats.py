



def word_count(content):
    count = 0
    contents = content.split()
    
    for words in contents:
        count += 1

    return count



def char_count(content):
    content = content.lower()

    dchar = {}

    for words in content:
        if words in dchar:
            dchar[words] += 1
        else:
            dchar[words] = 1

    # print(dchar)
            
    return dchar


def sort_on(dict_of_chars):
    for foo in dict_of_chars:
        num = dict_of_chars[foo]
    return num



def sort_dict(dict_of_chars):

    list_of_dicts = []



    for foo in dict_of_chars:
        if foo.isalpha():

            # print(foo, dict_of_chars[foo])

            bar = {foo:dict_of_chars[foo]}

            list_of_dicts.append(bar)

    
    list_of_dicts.sort(reverse=True, key=sort_on)

    for bar in list_of_dicts:
        # print(bar)

        for k, v in bar.items():
            print(f"{k}: {v}")
