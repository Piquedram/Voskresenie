from django import template


class FiltersException(Exception):
    pass


register = template.Library()

bad_words = {'человек', 'клуб'}


@register.filter()
def censor(text):
    if type(text) != str:
        raise FiltersException(f'Custom filter censor() received non str data type.')
    else:
        for word in text.split():
            for i in range(len(word)):
                if word.lower()[:i + 1] in bad_words:
                    if word.isalpha():
                        text = text.replace(word[1:], '*' * (len(word) - 1))
                    else:
                        count = 0
                        for symbol in word:
                            if symbol.isalpha():
                                count += 1
                        text = text.replace(word[1:count], '*' * (len(word) - 1))
    return text
