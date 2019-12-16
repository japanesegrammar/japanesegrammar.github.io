from python_utils.generator import printTitle, generateCard, writeNewLine, generate
from python_utils.html_generator import getHtmlString
from python_utils.model import TextPair, HighlightText, Color

with open('volitional_form.md', 'w', encoding="utf-8") as f:
    f.write(printTitle('Volitional Form Conjugation Rules'))

    cardText = '<b>Rule 1:</b> For u-verbs: Replace the u-vowel sound with the お equivalent and attach う' + '\n' + '\n' + \
               '<b>Rule 2:</b> For ru-verbs: Replace る with よう' + '\n' + '\n' + \
               '<b>Rule 3:</b> For exceptions: する becomes しよう and くる becomes こよう'

    f.write(generateCard(cardText, [], useLeft=True))

    f.write((printTitle('Rule 1')))
    writeNewLine(f)
    f.write('For u-verbs: Replace the u-vowel sound with the お equivalent and attach う')

    # we need to add this dummy. otherwise, there is brake line between explanation and example sentence
    l1 = TextPair('', '', [],)
    f.write(generate([l1]))

    f.write('<b>Example A</b>')
    f.write('<br>')
    oyogu = getHtmlString('泳ぐ')
    oyogo = getHtmlString('泳ご')
    oyogou = getHtmlString('泳ごう')
    f.write(f'{oyogu} ---`[replace u-vowel with the お equivalent]`--> {oyogo} ---`[attach う]`---> {oyogou}')

    l1 = TextPair('この夏は たくさん 泳ごうと 思います。', 'I am going to swim a lot this summer.', [HighlightText('泳ごう', Color.LIGHT_GREEN)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example B</b>')
    f.write('<br>')
    matsu = getHtmlString('待つ')
    mato = getHtmlString('待と')
    matou = getHtmlString('待とう')
    f.write(f'{matsu} ---`[replace u-vowel with the お equivalent]`--> {mato} ---`[attach う]`---> {matou}')
    f.write('<br>')
    l1 = TextPair('雨が やむまで 待とう。', "Let's wait until the rain stops.", [HighlightText('待とう', Color.LIGHT_GREEN)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)
