from python_utils.generator import printTitle, generateCard, writeNewLine, generate, getInfoBlock
from python_utils.html_generator import getHtmlString
from python_utils.mermaid_flow_chart_utils import getCssFlowChartWithThreeBlock
from python_utils.model import TextPair, HighlightText, Color
from python_utils.vocab_list import generateVocabLines

with open('conditional_tara_form.md', 'w', encoding="utf-8") as f:
    f.write(printTitle('Conditional - たら (tara) form'))

    f.write(
        'The `たら` (tara) form can also be used for expressing a conditional. In order to use `たら` (tara) form, we need to use know how to convert dictionary form to past tense form. Please see how to change to past tense [here](past_tense_form.md).')

    f.write('\n')
    f.write(getInfoBlock("When you use `たら` (tara), it is usually express the speaker's will; even pure hypothetical condition."))
    f.write('\n')

    f.write(printTitle('Conjugation Rule for たら (tara)'))
    cardText = 'Change the noun, adjective, or verb to its past tense and attach `ら` (ra) to it.'

    f.write(generateCard(cardText, [], useLeft=True))

    f.write('<br>')
    f.write('<b>Example A : Verb</b>')
    f.write('<br>')
    l1 = TextPair('東京へ 来たら、 ぜひ連絡して ください。', "Please contact me when you come to Tokyo.", [HighlightText('来た', Color.LIGHT_GREEN), HighlightText('ら', Color.LIGHT_PINK, replaceAt=1)], addBullet=True, )
    f.write(generate([l1]))
    writeNewLine(f)

    f.write(getCssFlowChartWithThreeBlock(getHtmlString('来る'), 'change to past tense form', getHtmlString('来た'), 'attach ら', getHtmlString('来たら')))
    writeNewLine(f)
    f.write('<b>Example B : Verb</b>')
    f.write('<br>')
    l1 = TextPair('練習したら うまくなるよ。', "If you practice, you'll get better.", [HighlightText('練習した', Color.LIGHT_GREEN), HighlightText('ら', Color.LIGHT_PINK, replaceAt=1)], addBullet=True, )
    f.write(generate([l1]))
    writeNewLine(f)

    f.write(getCssFlowChartWithThreeBlock(getHtmlString('練習する'), 'change to past tense form', getHtmlString('練習した'), 'attach ら', getHtmlString('練習したら')))

    f.write('<br>')
    f.write('<b>Example C : Noun</b>')
    f.write('<br>')
    l1 = TextPair('日本人だったら この言葉を知っているでしょう。', "If the person is a Japanese, he/she would know this word.", [HighlightText('だった', Color.LIGHT_GREEN), HighlightText('ら', Color.LIGHT_PINK, replaceAt=1)],
                  addBullet=True, )
    f.write(generate([l1]))
    writeNewLine(f)

    f.write(getCssFlowChartWithThreeBlock(getHtmlString('日本人'), 'change to past tense form', getHtmlString('日本人だった'), 'attach ら', getHtmlString('日本人だったら')))

    f.write('<br>')
    f.write('<b>Example D : I-Adjective </b>')
    f.write('<br>')
    l1 = TextPair('安かったら、たくさん買います。', "If cheap, I will buy a lot.", [HighlightText('安かった', Color.LIGHT_GREEN), HighlightText('ら', Color.LIGHT_PINK, replaceAt=1)], addBullet=True, )
    f.write(generate([l1]))
    writeNewLine(f)

    f.write(getCssFlowChartWithThreeBlock(getHtmlString('安い'), 'change to past tense form', getHtmlString('安かった'), 'attach ら', getHtmlString('安かったら')))

    f.write('<br>')
    f.write('<b>Example E : Na-Adjective </b>')
    f.write('<br>')
    l1 = TextPair('元気だったら、 水泳をするのに。', "If you had been healthy, you would be able to swim.", [HighlightText('元気だった', Color.LIGHT_GREEN), HighlightText('ら', Color.LIGHT_PINK, replaceAt=1)],
                  addBullet=True, )
    f.write(generate([l1]))
    writeNewLine(f)

    f.write(getCssFlowChartWithThreeBlock(getHtmlString('元気'), 'change to past tense form', getHtmlString('元気だった'), 'attach ら', getHtmlString('元気だったら')))

    vocabListInThisPage = ['東京', '来る', '連絡', '練習', '日本人', '言葉', '知る', '安い', '買う', '元気', '水泳']
    vocabLines = generateVocabLines(vocabListInThisPage)
    f.write(vocabLines)
