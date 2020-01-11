from python_utils.generator import printTitle, generateCard, writeNewLine, generate
from python_utils.html_generator import getHtmlString
from python_utils.mermaid_flow_chart_utils import getCssFlowChartWithTwoBlock, getCssFlowChartWithThreeBlock
from python_utils.model import TextPair, HighlightText, Color, ForceReplace
from python_utils.table_generator import generateTable
from python_utils.vocab_list import generateVocabLines

with open('volitional_form.md', 'w', encoding="utf-8") as f:
    f.write(printTitle('Volitional Form'))
    f.write(
        'The volitional form of a verb is a less formal, more casual equivalent of `ましょう`. You can use it to suggest a plan to a close friend but may not be appropriate to use when you speak with your boss or senior.')
    cardText = '<b>Rule 1:</b> For u-verbs: Replace the u-vowel sound with the お equivalent and attach う' + '\n' + '\n' + \
               '<b>Rule 2:</b> For ru-verbs: Replace る with よう' + '\n' + '\n' + \
               '<b>Rule 3:</b> For exceptions: する becomes しよう and くる becomes こよう'

    f.write(generateCard(cardText, [], useLeft=True))

    f.write((printTitle('Rule 1')))
    writeNewLine(f)
    f.write('For u-verbs: Replace the u-vowel sound with the お equivalent and attach う')

    table = generateTable(['Dictionary Form', 'Replacing Method', 'Volitional Form'],
                          [[getHtmlString("使う"), 'Replace う with お sound equivalent and attach う', getHtmlString("使おう")],
                           [getHtmlString("引く"), 'Replace く with お sound equivalent and attach う', getHtmlString("引こう")],
                           [getHtmlString("泳ぐ"), 'Replace ぐ with お sound equivalent and attach う', getHtmlString("泳ごう")],
                           [getHtmlString("起こす"), 'Replace す with お sound equivalent and attach う', getHtmlString("起こそう")],
                           [getHtmlString("待つ"), 'Replace つ with お sound equivalent and attach う', getHtmlString("待とう")],
                           [getHtmlString("往ぬ"), 'Replace ぬ with お sound equivalent and attach う', getHtmlString("往のう")],
                           [getHtmlString("呼ぶ"), 'Replace ぶ with お sound equivalent and attach う', getHtmlString("呼ぼう")],
                           [getHtmlString("読む"), 'Replace む with お sound equivalent and attach う', getHtmlString("読もう")],
                           [getHtmlString("走る"), 'Replace る with お sound equivalent and attach う', getHtmlString("走ろう")],
                           ])
    f.write(table)

    # we need to add this dummy. otherwise, there is brake line between explanation and example sentence
    l1 = TextPair('', '', [], )
    f.write(generate([l1]))

    f.write('<b>Example A</b>')
    l1 = TextPair('夏は川で泳ごう。', "Let's swim in the river in summer.", [HighlightText('泳ごう', Color.LIGHT_GREEN)], addBullet=True)
    f.write(generate([l1]))
    f.write(getCssFlowChartWithThreeBlock(getHtmlString('泳ぐ'), 'replace u-vowel with the お equivalent', getHtmlString('泳ご'), 'attach う', getHtmlString('泳ごう')))
    writeNewLine(f)

    f.write('<b>Example B</b>')

    f.write('<br>')
    l1 = TextPair('雨が やむまで 待とう。', "Let's wait until the rain stops.", [HighlightText('待とう', Color.LIGHT_GREEN)], addBullet=True)
    f.write(generate([l1]))
    f.write(getCssFlowChartWithThreeBlock(getHtmlString('待つ'), 'replace u-vowel with the お equivalent', getHtmlString('待と'), 'attach う', getHtmlString('待とう')))

    f.write((printTitle('Rule 2')))
    f.write('For ru-verbs: Replace る with よう')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'Volitional Form'],
                          [[getHtmlString("食べる"), 'replace る with よう', getHtmlString("食べよう")],
                           ])
    f.write(table)

    # we need to add this dummy. otherwise, there is brake line between explanation and example sentence
    l1 = TextPair('', '', [], )
    f.write(generate([l1]))

    f.write('<b>Example A</b>')
    f.write('<br>')

    l1 = TextPair('ご飯を 食べよう。', "Let's eat rice.", [HighlightText('食べよう', Color.LIGHT_GREEN)], addBullet=True, forceReplaceList=[ForceReplace('飯', "はん")])
    f.write(generate([l1]))
    f.write(getCssFlowChartWithTwoBlock(getHtmlString('食べる'), 'replace る with よう', getHtmlString('食べよう')))
    f.write('<br>')

    f.write('<b>Example B</b>')
    f.write('<br>')
    l1 = TextPair('今夜は早く寝よう。', "Let's sleep early tonight.", [HighlightText('寝よう', Color.LIGHT_GREEN)], addBullet=True)
    f.write(generate([l1]))
    f.write(getCssFlowChartWithTwoBlock(getHtmlString('寝る'), 'replace る with よう', getHtmlString('寝よう')))

    f.write((printTitle('Rule 3')))
    f.write('For exceptions: する becomes しよう and くる becomes こよう')
    table = generateTable(['Dictionary Form', 'Volitional Form'],
                          [[getHtmlString("する"), 'replace る with よう', getHtmlString("しよう")],
                           [getHtmlString("くる"), 'replace る with よう', getHtmlString("こよう")],
                           ])
    f.write(table)
    # we need to add this dummy. otherwise, there is brake line between explanation and example sentence
    l1 = TextPair('', '', [], )
    f.write(generate([l1]))

    f.write('<b>Example A</b>')
    l1 = TextPair('一緒に卒業しようね。', "Let's graduate together.", [HighlightText('卒業しよう', Color.LIGHT_GREEN)], addBullet=True)
    f.write(generate([l1]))
    f.write(getCssFlowChartWithTwoBlock(getHtmlString(' 卒業する'), 'replace する with しよう', getHtmlString('卒業しよう')))
    f.write('<br>')

    f.write('<b>Example B</b>')
    f.write('<br>')
    l1 = TextPair('二年後、また来よう。', "Let's come again two years later.", [HighlightText('来よう', Color.LIGHT_GREEN)], addBullet=True)
    f.write(generate([l1]))
    f.write(getCssFlowChartWithTwoBlock(getHtmlString('来る'), 'くる becomes こよう', getHtmlString('来よう')))

    vocabListInThisPage = ['夏', '川', '泳ぐ', '雨', '待つ', 'ご飯', '食べる', '今夜', '早く', '寝る', '一緒に', '卒業', '年後', '来る']
    vocabLines = generateVocabLines(vocabListInThisPage)
    f.write(vocabLines)
