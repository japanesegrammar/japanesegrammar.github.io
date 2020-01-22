from python_utils.generator import printTitle, generateCard, writeNewLine, generate, getInfoBlock
from python_utils.html_generator import getHtmlString
from python_utils.mermaid_flow_chart_utils import getCssFlowChartWithTwoBlock
from python_utils.model import TextPair, HighlightText, Color
from python_utils.vocab_list import generateVocabLines

with open('conditional_to_form.md', 'w', encoding="utf-8") as f:
    f.write(printTitle('Conditional - と「to」form'))

    f.write('The `と`「to」form can be used to express the result/event which is predictable and unavoidable due to an action.')

    f.write('\n')
    f.write(getInfoBlock("You <b>cannot</b> use `と` 「to」to express the speaker's wishes, judgement, permission, hopes, requests"))
    f.write('\n')

    f.write(printTitle('Conjugation Rule for と「to」'))
    cardText = 'Sentence: <em>[Condition]</em> `と` <em>[Result]</em> \n \n use <em>present tense short form</em> + `と`'

    f.write(generateCard(cardText, [], useLeft=True))

    f.write('<br>')
    f.write('<b>Example A</b>')
    f.write('<br>')
    l1 = TextPair('ここを押すと、ドアが 開きます。', "Press here to open the door.", [HighlightText('押す', Color.LIGHT_GREEN), HighlightText('と', Color.LIGHT_PINK)], addBullet=True, )
    f.write(generate([l1]))
    writeNewLine(f)

    f.write(getCssFlowChartWithTwoBlock(getHtmlString('押す'), 'attach と', getHtmlString('押すと'), ))
    writeNewLine(f)
    f.write('<b>Example B</b>')
    f.write('<br>')
    l1 = TextPair('メアリーさんが 国に帰ると 寂しくなります。', "When Mary returns home, we will be lonely.", [HighlightText('帰る', Color.LIGHT_GREEN), HighlightText('と', Color.LIGHT_PINK)], addBullet=True, )
    f.write(generate([l1]))

    f.write(getCssFlowChartWithTwoBlock(getHtmlString('帰る'), 'attach と', getHtmlString('帰ると'), ))
    f.write('\n')
    f.write(getInfoBlock("In this example, we are expressing the cause-effect relationship within the event"))
    f.write('\n')

    f.write('<br>')
    f.write('<b>Example C</b>')
    f.write('<br>')
    l1 = TextPair('私は子供の時、冬になると風邪をひきました。', "When I was a child, I caught a cold whenever winter arrived.", [HighlightText('だった', Color.LIGHT_GREEN), HighlightText('ら', Color.LIGHT_PINK, replaceAt=1)],
                  addBullet=True, )
    f.write(generate([l1]))
    writeNewLine(f)
    f.write(getCssFlowChartWithTwoBlock(getHtmlString('なる'), 'attach と', getHtmlString('なると'), ))

    f.write('\n')
    f.write(getInfoBlock("Even though we have to use present tense to attach with `と`「to」, we still can express the past event."))
    f.write('\n')

    f.write('<br>')
    f.write('<b>Example D: I-Adjective at the second clause</b>')
    f.write('<br>')
    l1 = TextPair('秋になると木が赤くなります。', "The trees turn red in the fall.", [HighlightText('なる', Color.LIGHT_GREEN), HighlightText('と', Color.LIGHT_PINK)],
                  addBullet=True, )
    f.write(generate([l1]))
    writeNewLine(f)
    f.write(getCssFlowChartWithTwoBlock(getHtmlString('なる'), 'attach と', getHtmlString('なると'), ))

    f.write('<br>')
    f.write('<b>Example E: Na-Adjective at the second clause</b>')
    f.write('<br>')
    l1 = TextPair('夜になると町が静かになります。', "The town becomes quite at night.", [HighlightText('なる', Color.LIGHT_GREEN), HighlightText('と', Color.LIGHT_PINK)],
                  addBullet=True, )
    f.write(generate([l1]))
    writeNewLine(f)
    f.write(getCssFlowChartWithTwoBlock(getHtmlString('なる'), 'attach と', getHtmlString('なると'), ))

    f.write('\n')
    f.write(getInfoBlock("For both example D and E, take note that we use an adjective (い「i」 and な「na」Adjective respectively) at the second clause. This kinds of sentence express a change in the content; something has turned/became due to a first clause."))
    f.write('\n')

    vocabListInThisPage = ['押す', 'ドア', '開く', '国', '帰る', '寂しい', '私', '子供', '時', '冬', '風邪', 'ひく', '秋', '木', '赤い', '夜', '町', '静か']
    vocabLines = generateVocabLines(vocabListInThisPage)
    f.write(vocabLines)
