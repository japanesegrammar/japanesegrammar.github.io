from python_utils.generator import printTitle, generateCard, writeNewLine, generate, getInfoBlock
from python_utils.html_generator import getHtmlString
from python_utils.model import TextPair, HighlightText, Color, ForceReplace
from python_utils.vocab_list import generateVocabLines

# For subsequent actions and subsequent events,
# Do something in advance

with open('v_te-form_okimasu.md', 'w') as f:
    f.write(printTitle('Usage Form'))
    f.write('\n')
    f.write(generateCard('V て-form + おきます', [('light_green', 'V て-form'), ('light_pink', 'おきます')]))
    f.write('\n')

    f.write((printTitle('To do something in advance; Preparation')))
    writeNewLine(f)

    l1 = TextPair('旅行の 前に切符を 買って おきます。', 'I will buy a ticket before the trip.', [HighlightText('買って', Color.LIGHT_GREEN), HighlightText('おきます', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    l1 = TextPair('来週までにレポートを書いておきます。', 'I will write a report by next week.', [HighlightText('書いて', Color.LIGHT_GREEN), HighlightText('おきます', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    f.write((printTitle('To keep something in a certain state')))
    l1 = TextPair('使たら、元の場所に戻しておきます。', 'When you finished using it, put it back where it is.', [HighlightText('戻して', Color.LIGHT_GREEN), HighlightText('おきます', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    # 彼は部屋を きれい にしておく
    l1 = TextPair('彼は 部屋を きれいにしておく。', 'He keeps the room clean.', [HighlightText('して', Color.LIGHT_GREEN), HighlightText('おく', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    # to generate vocab
    vocabListInThisPage = ['旅行', '切符', '買う', '来週', 'レポート', '書く', '使う', '元', '場所', '戻す', '彼', '部屋']
    vocabLines = generateVocabLines(vocabListInThisPage)
    f.write(vocabLines)
