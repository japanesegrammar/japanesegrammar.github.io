from python_utils.generator import printTitle, generateCard, writeNewLine, generate
from python_utils.html_generator import getHtmlString
from python_utils.model import TextPair, HighlightText, Color
from python_utils.vocab_list import generateVocabLines

with open('~taradoudesuka.md', 'w', encoding="utf-8") as f:

    f.write(printTitle('Usage Form'))
    cardText = 'V past form + らどうですか'

    f.write(generateCard(cardText, []))

    f.write(printTitle('Explanation'))
    f.write("This form conveys advice or recommendation but it may also have a criticizing tone for not performing the activity that should have done already.")
    f.write(printTitle('Examples'))

    f.write('<b>Example A</b>')
    f.write('<br>')
    furigana = getHtmlString("勉強する")
    furigana1 = getHtmlString("勉強した")
    furigana3 = getHtmlString("勉強したらどうですか")
    f.write(f'{furigana} --> [convert to past tense] --> {furigana1} --> [combine with らどうですか] --> {furigana3} ')
    l1 = TextPair('もっと勉強したらどうですか。', "Why don't you study harder?", [HighlightText('勉強した', Color.LIGHT_GREEN), HighlightText('らどうですか', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example B</b>')
    f.write('<br>')
    furigana = getHtmlString("飲む")
    furigana1 = getHtmlString("飲んだ")
    furigana3 = getHtmlString("飲んだらどうですか")
    f.write(f'{furigana} --> [convert to past tense] --> {furigana1} --> [combine with らどうですか] --> {furigana3} ')
    l1 = TextPair('薬を飲んだらどうですか。', "How about taking some medicine?", [HighlightText('飲んだ', Color.LIGHT_GREEN), HighlightText('らどうですか', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    vocabListInThisPage = ['勉強', '薬', '飲む']
    vocabLines = generateVocabLines(vocabListInThisPage)
    f.write(vocabLines)
