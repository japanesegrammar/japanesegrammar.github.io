from python_utils.generator import printTitle, generateCard, writeNewLine, generate
from python_utils.html_generator import getHtmlString
from python_utils.mermaid_flow_chart_utils import getMermaidScript, getFlowChart
from python_utils.model import TextPair, HighlightText, Color
from python_utils.vocab_list import generateVocabLines

with open('~nagara.md', 'w', encoding="utf-8") as f:
    f.write(getMermaidScript())

    f.write(printTitle('Usage Form'))
    cardText = ' Stem Verb  + ながら'

    f.write(generateCard(cardText, []))

    f.write(printTitle('Explanation'))
    f.write("You can use with ながら with two verbs to express the two actions are performed at the same time. However, it cannot describe an action performed by another person.")
    f.write(printTitle('Examples'))

    f.write('<b>Example A</b>')
    f.write('<br>')
    furigana = getHtmlString("聞く")
    furigana1 = getHtmlString("聞き")
    furigana3 = getHtmlString("聞きながら")
    flowChart = getFlowChart(["聞く", "聞き", "聞きながら"], ['convert dictionary to stem verb', 'combine with ながら'])
    f.write(flowChart)
    l1 = TextPair('私はいつも音楽を聞きながら日本語を勉強します。', "I always study Japanese while listening to music.", [HighlightText('聞き', Color.LIGHT_GREEN), HighlightText('ながら', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example B</b>')
    f.write('<br>')

    flowChart = getFlowChart(["歌う", "歌い", "歌いながら"], ['convert dictionary to stem verb', 'combine with ながら'])
    f.write(flowChart)
    l1 = TextPair('彼は歌を歌いながら洗濯をしています。', "He is doing laundry while singing a song.", [HighlightText('歌い', Color.LIGHT_GREEN), HighlightText('ながら', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example C</b>')
    f.write('<br>')
    flowChart = getFlowChart(["する", "し", "しながら"], ['convert dictionary to stem verb', 'combine with ながら'])
    f.write(flowChart)
    l1 = TextPair('アルバイトをしながら学校に行くのは大変です。', "It is hard to go to school while working part-time.", [HighlightText('し', Color.LIGHT_GREEN), HighlightText('ながら', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)

    vocabListInThisPage = ['私', '音楽', '聞く', '日本語', '勉強', '彼', '歌', '歌う', '洗濯', 'アルバイト', '学校', '行く', '大変']
    vocabLines = generateVocabLines(vocabListInThisPage)
    f.write(vocabLines)
