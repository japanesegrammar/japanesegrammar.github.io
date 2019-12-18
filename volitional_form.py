from python_utils.generator import printTitle, generateCard, writeNewLine, generate
from python_utils.html_generator import getHtmlString
from python_utils.model import TextPair, HighlightText, Color, ForceReplace
from python_utils.vocab_list import generateVocabLines

with open('volitional_form.md', 'w', encoding="utf-8") as f:
    f.write(printTitle('Volitional Form Conjugation Rules'))
    f.write('The volitional form of a verb is a less formal, more casual equivalent of `ましょう`. You can use it to suggest a plan to a close friend but may not be appropriate to use when you speak with your boss or senior.')
    cardText = '<b>Rule 1:</b> For u-verbs: Replace the u-vowel sound with the お equivalent and attach う' + '\n' + '\n' + \
               '<b>Rule 2:</b> For ru-verbs: Replace る with よう' + '\n' + '\n' + \
               '<b>Rule 3:</b> For exceptions: する becomes しよう and くる becomes こよう'

    f.write(generateCard(cardText, [], useLeft=True))

    f.write((printTitle('Rule 1')))
    writeNewLine(f)
    f.write('For u-verbs: Replace the u-vowel sound with the お equivalent and attach う')

    # we need to add this dummy. otherwise, there is brake line between explanation and example sentence
    l1 = TextPair('', '', [], )
    f.write(generate([l1]))

    f.write('<b>Example A</b>')
    f.write('<br>')
    oyogu = getHtmlString('泳ぐ')
    oyogo = getHtmlString('泳ご')
    oyogou = getHtmlString('泳ごう')
    f.write(f'{oyogu} ---`[replace u-vowel with the お equivalent]`--> {oyogo} ---`[attach う]`---> {oyogou}')
    # 夏は川で泳ごう
    # この夏は たくさん 泳ごうと 思います
    l1 = TextPair('夏は川で泳ごう。', "Let's swim in the river in summer.", [HighlightText('泳ごう', Color.LIGHT_GREEN)], addBullet=True)
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

    f.write((printTitle('Rule 2')))
    writeNewLine(f)
    f.write('For ru-verbs: Replace る with よう')

    # we need to add this dummy. otherwise, there is brake line between explanation and example sentence
    l1 = TextPair('', '', [], )
    f.write(generate([l1]))

    f.write('<b>Example A</b>')
    f.write('<br>')
    oyogu = getHtmlString('食べる')
    oyogo = getHtmlString('食べよう')

    f.write(f'{oyogu} ---`[replace る with よう]`--> {oyogo}')

    l1 = TextPair('ご飯を 食べよう。', "Let's eat rice.", [HighlightText('食べよう', Color.LIGHT_GREEN)], addBullet=True, forceReplaceList=[ForceReplace('飯', "はん")])
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example B</b>')
    f.write('<br>')
    matsu = getHtmlString('寝る')
    mato = getHtmlString('寝よう')
    f.write(f'{matsu} ---`[replace る with よう]`--> {mato}')
    f.write('<br>')
    l1 = TextPair('今夜は早く寝よう。', "Let's sleep early tonight.", [HighlightText('寝よう', Color.LIGHT_GREEN)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    f.write((printTitle('Rule 3')))
    writeNewLine(f)
    f.write('For exceptions: する becomes しよう and くる becomes こよう')

    # we need to add this dummy. otherwise, there is brake line between explanation and example sentence
    l1 = TextPair('', '', [], )
    f.write(generate([l1]))

    f.write('<b>Example A</b>')
    f.write('<br>')
    matsu = getHtmlString(' 卒業する')
    mato = getHtmlString('卒業しよう')
    f.write(f'{matsu} ---`[replace する with しよう]`--> {mato}')
    f.write('<br>')
    l1 = TextPair('一緒に卒業しようね。', "Let's graduate together.", [HighlightText('卒業しよう', Color.LIGHT_GREEN)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example B</b>')
    f.write('<br>')
    oyogu = getHtmlString('来る')
    oyogo = getHtmlString('来よう')

    f.write(f'{oyogu} ---`[くる becomes こよう]`--> {oyogo}')

    l1 = TextPair('二年後、また来よう。', "Let's come again two years later.", [HighlightText('来よう', Color.LIGHT_GREEN)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    vocabListInThisPage = ['夏', '川', '泳ぐ', '雨', '待つ', 'ご飯', '食べる', '今夜', '早く', '寝る', '一緒に', '卒業', '年後', '来る']
    vocabLines = generateVocabLines(vocabListInThisPage)
    f.write(vocabLines)
