from python_utils.generator import printTitle, generateCard, writeNewLine, generate, generateGridContainer
from python_utils.model import TextPair, HighlightText, Color, FuriganaGridItem
from python_utils.vocab_list import generateVocabLines

with open('volitional_form_+_question_particle_ka.md', 'w', encoding="utf-8") as f:

    f.write(printTitle('Usage Form'))
    f.write(generateCard('V volitional form +' + ' ' + 'か', [('light_green', 'V volitional form'), ('light_pink', 'か')]))
    writeNewLine(f)

    f.write(printTitle('Prerequisite'))
    f.write(f'Please see [these rules](volitional_form.md) if you want to know how to do verb conjugation for volitional form.')
    writeNewLine(f)

    f.write(printTitle('Explanation'))
    f.write('You can use the volitional form with the question particle `か` to ask for an opinion in your offer or suggestion.')

    f.write((printTitle('Examples')))

    # we need to add this dummy. otherwise, there is brake line between explanation and example sentence
    l1 = TextPair('', '', [], )
    f.write(generate([l1]))

    f.write('<b>Example A: Using Rule 1</b>')
    l1 = TextPair('手伝おうか。', "Shall I help you?", [HighlightText('手伝おう', Color.LIGHT_GREEN), HighlightText('か', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example B: Using Rule 2</b>')
    t = '友だちが おもしろい と言っていたから、この映画を見ようか。'
    englishText = 'My friend said it was interesting so let ’s see this movie.'
    pairs = ['友', '言', '映画', '見']
    f.write(generateGridContainer([FuriganaGridItem(t, pairs, englishText, [HighlightText('見よう', Color.LIGHT_GREEN), HighlightText('か', Color.LIGHT_PINK, 2)], addBullet=True)]))
    writeNewLine(f)

    f.write('<b>Example C: Using Rule 3</b>')
    f.write('<br>')
    l1 = TextPair('園庭をちょっとだけ散歩しようか。', "Let's take a short walk in the garden.", [HighlightText('散歩しよう', Color.LIGHT_GREEN), HighlightText('か', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example D: Using Rule 3</b>')
    l1 = TextPair('試食に また来ようか。', "Shall we come again for food tasting?", [HighlightText('来よう', Color.LIGHT_GREEN), HighlightText('か', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    vocabListInThisPage = ['手伝う', '友だち', '言う', '映画', '見る', '園庭', '散歩', '試食', '来る']
    vocabLines = generateVocabLines(vocabListInThisPage)
    f.write(vocabLines)
