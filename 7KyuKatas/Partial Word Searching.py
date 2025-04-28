def word_search(query, seq):
    words = [x for x in seq if query.lower() in x.lower()]
    if words == []: return ['None']
    else: return words
