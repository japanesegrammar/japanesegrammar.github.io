from python_utils.generator import printTitle, generateCard, writeNewLine, generate, getInfoBlock
from python_utils.html_generator import getHtmlString
from python_utils.mermaid_flow_chart_utils import getCssFlowChartWithTwoBlock
from python_utils.model import TextPair, HighlightText, Color
from python_utils.vocab_list import generateVocabLines

with open('conditional_nara_form.md', 'w', encoding="utf-8") as f:
    f.write(printTitle('Conditional - なら 「nara」form'))

    f.write('You can use なら 「nara」based on the situation but it is better to explain with examples. Please look at each example with an explanation.')

    f.write('<br>')
    f.write('<br>')
    f.write('<b>Example A</b>')
    f.write('<br>')
    l1 = TextPair('ブラジルに、行ったことがありますか。', 'Have you even been to Brazil?', addBullet=True, )
    l2 = TextPair('チリなら行ったことが, ブラジルは行ったことがありません。', "I've been to Chile, but never been to Brazil.", [HighlightText('なら', Color.LIGHT_GREEN)])
    f.write(generate([l1, l2]))

    f.write('\n')
    f.write(getInfoBlock("The second speaker responded with a contact sentence to show that even though he/she been to Chile, he/she never been to Brazil. "))
    f.write('\n')

    f.write('<br>')
    f.write('<b>Example B</b>')
    f.write('<br>')
    l1 = TextPair('日本語が、わかりますか。', 'Do you understand Japanese?', addBullet=True, )
    l2 = TextPair('ひらがななら わかります。', "if it is (written) in Hiragana, then yes.", [HighlightText('なら', Color.LIGHT_GREEN)])
    f.write(generate([l1, l2]))

    f.write('\n')
    f.write(getInfoBlock("Here, we want to express the limitation (written language limited to Hiragana in this situation)."))
    f.write('\n')

    f.write('<br>')
    f.write('<b>Example C</b>')
    f.write('<br>')
    l1 = TextPair('温泉に 行きたいんですが どこが いい 所 ありませんか。', "I want to visit a hot spring resort. Don't you know any good place?", addBullet=True, )
    l2 = TextPair('温泉なら、白馬が いいですよ。', "...If you are talking about hot springs, Hakuba would be good.", [HighlightText('なら', Color.LIGHT_GREEN)])
    f.write(generate([l1, l2]))

    f.write('\n')
    f.write(getInfoBlock("In this sentence, we want to pick up the topic introduced by the first speaker."))
    f.write('\n')

    vocabListInThisPage = ['ブラジル', '行く', 'チリ', '日本語', '温泉', '所', '白馬']
    vocabLines = generateVocabLines(vocabListInThisPage)
    f.write(vocabLines)
