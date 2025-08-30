def num_words(contents):
    words = len(contents.split())
    return words

def character_count(words):
    results = {}
    for word in words:
        if word not in results:
            results[word] = 0
        if word in results:
            results[word] += 1
    return results

def sort_on(items):
    return items["num"]

def sort_reverse(count):
    output = []
    for k, v in count.items():
        if k.isalpha():
            output.append({"char": k, "num": v})
    output.sort(key=sort_on, reverse=True)
    return output
