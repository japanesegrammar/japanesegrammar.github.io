from python_utils.generator import printTitle, generateCard, writeNewLine, generate
from python_utils.html_generator import getHtmlString
from python_utils.model import TextPair, HighlightText, Color
from python_utils.vocab_list import generateVocabLines

with open('volitional_form_+_toomotteimasu.md', 'w', encoding="utf-8") as f:
    toomotteimasu = getHtmlString("と 思っています")

    f.write(printTitle('Usage Form'))
    f.write(generateCard('V volitional form +' + toomotteimasu, [('light_green', 'V volitional form'), ('light_pink', toomotteimasu)]))
    writeNewLine(f)

    f.write(printTitle('Prerequisite'))
    f.write(f'Please see [these rules](volitional_form.md) if you want to know how to do verb conjugation for volitional form.')
    writeNewLine(f)
    f.write(printTitle('Explanation'))
    f.write(f"You can use the volitional form with {toomotteimasu} to express what the speaker is thinking of doing. Note that when you use this expression, the decision of doing something was made some time ago. You can also use to express a third person's will or intention.")

    f.write(printTitle('Examples'))

    f.write('<b>Example A</b>')
    f.write('<br>')
    l1 = TextPair('週末は 海に 行こうと思っています。', "I am thinking of going to the beach at the weekend.", [HighlightText('行こう', Color.LIGHT_GREEN), HighlightText('と 思っています', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example B</b>')
    f.write('<br>')
    l1 = TextPair('今から 銀行へ 行こうと思っています。', "I'm going to the bank now.", [HighlightText('行こう', Color.LIGHT_GREEN), HighlightText('と 思っています', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example C</b>')
    f.write('<br>')
    l1 = TextPair('彼は 外国で働こうと思っています。', "He is thinking of working in a foreign country.", [HighlightText('働こう', Color.LIGHT_GREEN), HighlightText('と 思っています', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))

    vocabListInThisPage = ['週末', '海', '行く', '思う', '今から', '銀行', '彼', '外国', '働く']
    vocabLines = generateVocabLines(vocabListInThisPage)
    f.write(vocabLines)
