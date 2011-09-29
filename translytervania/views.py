from pleiades.transliteration import transliterate_name

langs = ['grc']

default_lang = 'grc'
default_text = u"\u1f08\u03c6\u03c1\u03bf\u03b4\u03b9\u03c3\u03b9\u03ac\u03c2"

def form(request):
    result = None
    if 't' in request.params and 'l' in request.params:
        result = transliterate_name(request.params['l'], request.params['t'])
    return {
        'project': "Classical Atlas Transliteration",
        'langs': langs,
        'lang': request.params.get('l', default_lang),
        'text': request.params.get('t', default_text),
        'result': result
        }
