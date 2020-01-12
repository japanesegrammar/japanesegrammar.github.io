from python_utils.generator import printTitle, generateCard, writeNewLine, generate, getInfoBlock
from python_utils.html_generator import getHtmlString
from python_utils.mermaid_flow_chart_utils import getCssFlowChartWithTwoBlock, getCssFlowChartWithThreeBlock
from python_utils.model import TextPair, HighlightText, Color, ForceReplace
from python_utils.table_generator import generateTable
from python_utils.vocab_list import generateVocabLines

with open('conditional_form.md', 'w', encoding="utf-8") as f:
    f.write(printTitle('Conditional Form Conjugation Rules'))
    f.write(
        'In this lesson, we will learn how to change from dictionary form to conditional form to express condition in Japanese.')
    cardText = '<b>Rule 1:</b> For u-verbs: Replace the u-vowel sound with the え equivalent and attach ば' + '\n' + '\n' + \
               '<b>Rule 2:</b> For ru-verbs: Replace る with れば' + '\n' + '\n' + \
               '<b>Rule 3:</b> For verb exceptions: する becomes すれば and くる becomes くらば' + '\n' + '\n' + \
               '<b>Rule 4:</b> For い-Adj:  Change the last い of the い-adjective into ければ' + '\n' + '\n' + \
               '<b>Rule 5:</b> For な-Adj: Change the last な of the な-adjective and attach なら' + '\n' + '\n' + \
               '<b>Rule 6:</b> For Noun: Attach なら to the noun'

    f.write(generateCard(cardText, [], useLeft=True))

    f.write((printTitle('Rule 1')))
    writeNewLine(f)
    f.write('For u-verbs: Replace the u-vowel sound with the え equivalent and attach ば')

    table = generateTable(['Dictionary Form', 'Replacing Method', 'Conditional Form'],
                          [[getHtmlString("使う"), 'Replace う with the え equivalent and attach ば', getHtmlString("使えば")],
                           [getHtmlString("引く"), 'Replace く with the え equivalent and attach ば', getHtmlString("引けば")],
                           [getHtmlString("泳ぐ"), 'Replace ぐ with the え equivalent and attach ば', getHtmlString("泳げば")],
                           [getHtmlString("起こす"), 'Replace す with the え equivalent and attach ば', getHtmlString("起せば")],
                           [getHtmlString("待つ"), 'Replace つ with the え equivalent and attach ば', getHtmlString("待てば")],
                           [getHtmlString("往ぬ"), 'Replace ぬ with the え equivalent and attach ば', getHtmlString("往ねば")],
                           [getHtmlString("呼ぶ"), 'Replace ぶ with the え equivalent and attach ば', getHtmlString("呼べば")],
                           [getHtmlString("読む"), 'Replace む with the え equivalent and attach ば', getHtmlString("読めば")],
                           [getHtmlString("走る"), 'Replace る with the え equivalent and attach ば', getHtmlString("走れば")],
                           ])
    f.write(table)

    f.write((printTitle('Rule 2')))
    f.write('For ru-verbs: Replace る with れば')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'Conditional Form'],
                          [[getHtmlString("食べる"), 'replace る with れば', getHtmlString("食べれば ")],
                           ])
    f.write(table)

    f.write((printTitle('Rule 3')))
    f.write('For exceptions: する becomes すれば and くる becomes くらば')
    table = generateTable(['Dictionary Form', 'Conditional Form'],
                          [[getHtmlString("する"), 'すれば'],
                           [getHtmlString("くる"), 'くらば'],
                           ])
    f.write(table)

    f.write((printTitle('Rule 4')))
    f.write('For い-Adj:  Change the last い of the い-adjective into ければ')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'Conditional Form'],
                          [[getHtmlString("寒い"), 'replace the last い of the い-adjective into ければ', getHtmlString("寒ければ ")],
                           ])
    f.write(table)

    f.write((printTitle('Rule 5')))
    f.write('For な-Adj: Change the last な of the な-adjective and attach なら')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'Conditional Form'],
                          [[getHtmlString("元気[な]"), 'replace the last な of the な-adjective and attach なら', getHtmlString("元気なら ")],
                           ])
    f.write(table)

    f.write(getInfoBlock('Some grammar website shows attaching `であれば` to な-Adj. But `なら` is usually used.'))

    f.write((printTitle('Rule 6')))
    f.write('For Noun: Attach なら to the noun')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'Conditional Form'],
                          [[getHtmlString("雨"), 'attach なら', getHtmlString("雨なら ")],
                           ])
    f.write(table)

    f.write(getInfoBlock('Some grammar website shows attaching `であれば` to Noun. But `なら` is usually used.'))
