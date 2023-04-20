import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# Список нежелательных слов
BAD_WORDS = ['редиска', 'редиски', 'фуфло', 'кардан', 'кардана', 'бельмондо', 'заёб', 'распиздяй', 'веблюдей',
             'гунявый', 'гунявой', 'кака', 'кончитта', 'вомитнул', 'вомиторий', 'кусороклиша', 'мохуяр',
             'обсерватория', 'пулька', 'сиська', 'трухлявый', 'туба', 'щайсе', 'невротъебательского', 'ахтунг',
             'пиздатый', 'пиздатом', 'пиздатого', 'опездол ', 'опездолов', 'пиздопротивный', 'яйца',  'шлёпалово',
             'шлепаловом', 'черепа ', 'фуфломицина', 'хлесиво']


@register.filter(name='censor')
def censor(text):
    # Проход по списку нежелательных слов и замена букв на * со второй буквы
    for word in BAD_WORDS:
        pattern = re.compile(r'\b{}\b'.format(word), re.IGNORECASE)
        censored_word = word[0] + '*'*(len(word)-1)
        text = re.sub(pattern, censored_word, text)
    return mark_safe(text)
