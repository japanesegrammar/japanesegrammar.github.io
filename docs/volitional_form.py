from python_utils.generator import printTitle, generateCard, writeNewLine, generate, getInfoBlock
from python_utils.html_generator import getHtmlString
from python_utils.model import TextPair, HighlightText, Color, ForceReplace
from python_utils.vocab_list import generateVocabLines

with open('volitional_form.md', 'w') as f:
    f.write(printTitle('Volitional Form Conjugation Rules'))

    cardText = '<b>Rule 1:</b> For u-verbs: Replace the u-vowel sound with the お equivalent and attach う' + '\n' + '\n' + \
               '<b>Rule 2:</b> For ru-verbs: Replace る with よう' + '\n' + '\n' + \
               '<b>Rule 3:</b> For exceptions: する becomes しよう and くる becomes こよう'

    f.write(generateCard(cardText, [], useLeft=True))

    f.write((printTitle('Rule 1')))
    writeNewLine(f)

    f.write('For u-verbs: Replace the u-vowel sound with the お equivalent and attach う')
    f.write('\n')
    f.write('\n')
    oyogu = getHtmlString('泳ぐ')
    oyogo = getHtmlString('泳ご')
    oyogou = getHtmlString('泳ごう')
    f.write(f'{oyogu} ---`[replace u-vowel with the お equivalent]`--> {oyogo} ---`[attach う]`---> {oyogou}')

    l1 = TextPair('この夏は たくさん 泳ごうと 思います。', 'I am going to swim a lot this summer.', [HighlightText('泳ごう', Color.LIGHT_GREEN)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    matsu = getHtmlString('待つ')
    mato = getHtmlString('待と')
    matou = getHtmlString('待とう')
    f.write(f'{matsu} ---`[replace u-vowel with the お equivalent]`--> {mato} ---`[attach う]`---> {matou}')

    l1 = TextPair('雨が やむまで 待とう。', "Let's wait until the rain stops.", [HighlightText('待とう', Color.LIGHT_GREEN)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)
