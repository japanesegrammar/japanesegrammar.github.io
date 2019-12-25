from python_utils.generator import printTitle, generateCard, writeNewLine, generate
from python_utils.model import TextPair, HighlightText, Color
from python_utils.vocab_list import generateVocabLines

with open('~kamoshiremasen.md', 'w', encoding="utf-8") as f:

    f.write(printTitle('Usage Form'))
    cardText = '<b>V plain form</b> + かも しれません' + '\n' + '\n' + \
               '<b>い-adj plain form</b> + かも しれません' + '\n' + '\n' + \
               '<b>な-adj plain form</b> + かも しれません' + '\n' + '\n' + \
               '<b>N</b> + かも しれません'

    f.write(generateCard(cardText, [], useLeft=True))

    f.write(printTitle('Explanation'))
    f.write("You can use this to express the speaker's inference, and means that there is a possibility that some event or state occurred/occurs/will occur.")
    f.write(printTitle('Examples'))

    f.write('<b>Example A :</b> V plain form + かも しれません')
    f.write('<br>')
    l1 = TextPair('約束の 時間に 間に 合わないかもしれません。', "We might not be in time for the appointment.", [HighlightText('合わない', Color.LIGHT_GREEN), HighlightText('かもしれません', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example B : </b> い-adj plain form + かも しれません')
    f.write('<br>')
    l1 = TextPair('時期によっては少し安いかもしれません。', "May be a little cheaper depending on the season.", [HighlightText('安い', Color.LIGHT_GREEN), HighlightText('かもしれません', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example C : </b> な-adj plain form</b> + かも しれません')
    f.write('<br>')
    l1 = TextPair('この 画家は 一番 有名かもしれません。', "This painter may be the most famous.", [HighlightText('有名', Color.LIGHT_GREEN), HighlightText('かもしれません', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example D : </b> N + かも しれません')
    f.write('<br>')
    l1 = TextPair('一番楽しい時間かもしれません。', "It may be the most fun time.", [HighlightText('時間', Color.LIGHT_GREEN), HighlightText('かもしれません', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    vocabListInThisPage = ['約束', '時間', '間に', '合う', '時期', '少し', '安い','画家', '一番' ,'有名', '楽しい']
    vocabLines = generateVocabLines(vocabListInThisPage)
    f.write(vocabLines)
