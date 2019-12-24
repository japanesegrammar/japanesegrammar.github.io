from python_utils.generator import printTitle, generateCard, writeNewLine, generate, generateGridContainer
from python_utils.html_generator import getHtmlString
from python_utils.model import TextPair, HighlightText, Color, ForceReplace, FuriganaGridItem
from python_utils.vocab_list import generateVocabLines

with open('volitional_form_+_question_particle_ka.md', 'w', encoding="utf-8") as f:
    f.write(f'Please see [these rules](volitional_form.md) if you want to know how to do verb conjugation for volitional form.')
    f.write('You can use the volitional form with the question particle `か` to ask for an opinion in your offer or suggestion.')

    f.write((printTitle('Rule 1')))
    writeNewLine(f)
    f.write('For u-verbs: Replace the u-vowel sound with the お equivalent and attach う')

    # we need to add this dummy. otherwise, there is brake line between explanation and example sentence
    l1 = TextPair('', '', [], )
    f.write(generate([l1]))

    f.write('<b>Example A</b>')
    f.write('<br>')
    oyogu = getHtmlString('手伝う')
    oyogo = getHtmlString('手伝お')
    oyogou = getHtmlString('手伝おう')
    f.write(f'{oyogu} ---`[replace u-vowel with the お equivalent]`--> {oyogo} ---`[attach う]`---> {oyogou}')
    # 夏は川で泳ごう
    # この夏は たくさん 泳ごうと 思います
    # japaneseText = '手伝おうか。'
    # englishText = 'My friend said it was interesting so let ’s see this movie.'
    # pairs = ['手伝']
    # f.write(generateGridContainer([FuriganaGridItem(japaneseText, pairs, englishText, [HighlightText('手伝おう', Color.LIGHT_GREEN), HighlightText('か', Color.LIGHT_PINK)], addBullet=True)]))
    # writeNewLine(f)

    l1 = TextPair('手伝おうか。', "Shall I help you?", [HighlightText('手伝おう', Color.LIGHT_GREEN), HighlightText('か', Color.LIGHT_PINK)], addBullet=True)
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
    oyogu = getHtmlString('見る')
    oyogo = getHtmlString('見よう')

    f.write(f'{oyogu} ---`[replace る with よう]`--> {oyogo}')

    t = '友だちが おもしろい と言っていたから、この映画を見ようか。'
    englishText = 'My friend said it was interesting so let ’s see this movie.'
    pairs = ['友', '言', '映画', '見']
    f.write(generateGridContainer([FuriganaGridItem(t, pairs, englishText, [HighlightText('見よう', Color.LIGHT_GREEN), HighlightText('か', Color.LIGHT_PINK, 2)], addBullet=True)]))
    writeNewLine(f)

    f.write((printTitle('Rule 3')))
    writeNewLine(f)
    f.write('For exceptions: する becomes しよう and くる becomes こよう')

    # we need to add this dummy. otherwise, there is brake line between explanation and example sentence
    l1 = TextPair('', '', [], )
    f.write(generate([l1]))

    f.write('<b>Example A</b>')
    f.write('<br>')
    matsu = getHtmlString('散歩する')
    mato = getHtmlString('散歩しよう')
    f.write(f'{matsu} ---`[replace する with しよう]`--> {mato}')
    f.write('<br>')
    l1 = TextPair('園庭をちょっとだけ散歩しようか。', "Let's take a short walk in the garden.", [HighlightText('散歩しよう', Color.LIGHT_GREEN), HighlightText('か', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example B</b>')
    f.write('<br>')
    oyogu = getHtmlString('来る')
    oyogo = getHtmlString('来よう')

    f.write(f'{oyogu} ---`[くる becomes こよう]`--> {oyogo}')

    l1 = TextPair('試食に また来ようか。', "Shall we come again for food tasting?", [HighlightText('来よう', Color.LIGHT_GREEN), HighlightText('か', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    vocabListInThisPage = ['手伝う', '友だち', '言う', '映画', '見る', '園庭', '散歩', '試食', '来る']
    vocabLines = generateVocabLines(vocabListInThisPage)
    f.write(vocabLines)
