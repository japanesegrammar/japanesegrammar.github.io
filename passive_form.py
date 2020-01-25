from python_utils.generator import printTitle, generateCard, writeNewLine, generate, getInfoBlock
from python_utils.html_generator import getHtmlString
from python_utils.mermaid_flow_chart_utils import getCssFlowChartWithTwoBlock, getCssFlowChartWithThreeBlock
from python_utils.model import TextPair, HighlightText, Color, ForceReplace
from python_utils.table_generator import generateTable
from python_utils.vocab_list import generateVocabLines

with open('passive_form.md', 'w', encoding="utf-8") as f:
    f.write(printTitle('Passive Form Conjugation Rules'))
    f.write(
        'In this lesson, we will learn how to change from dictionary form to passive form and how to conjugate from passive form to different forms; present; past and て-form.')
    cardText = '<b>Rule 1:</b> For u-verbs: Replace the u-vowel sound with the あ equivalent and attach れる' + '\n' + '\n' + \
               '<b>Rule 2:</b> For ru-verbs: Replace る with られる' + '\n' + '\n' + \
               '<b>Rule 3:</b> For verb exceptions: する becomes される and される becomes こられる' + '\n' + '\n'

    f.write(generateCard(cardText, [], useLeft=True))

    f.write((printTitle('Rule 1')))
    writeNewLine(f)
    f.write('For u-verbs: Replace the u-vowel sound with the あ equivalent and attach れる')

    table = generateTable(['Dictionary Form', 'Replacing Method', 'Passive Form'],
                          [[getHtmlString("使う"), 'Replace う with the あ equivalent and attach れる', getHtmlString("使われる")],
                           [getHtmlString("行く"), 'Replace く with the あ equivalent and attach れる', getHtmlString("行かれる")],
                           [getHtmlString("泳ぐ"), 'Replace ぐ with the あ equivalent and attach れる', getHtmlString("泳がれる")],
                           [getHtmlString("話す"), 'Replace す with the あ equivalent and attach れる', getHtmlString("話すれる")],
                           [getHtmlString("待つ"), 'Replace つ with the あ equivalent and attach れる', getHtmlString("待たれる")],
                           [getHtmlString("死ぬ"), 'Replace ぬ with the あ equivalent and attach れる', getHtmlString("死なれる")],
                           [getHtmlString("遊ぶ"), 'Replace ぶ with the あ equivalent and attach れる', getHtmlString("遊ばれる")],
                           [getHtmlString("読む"), 'Replace む with the あ equivalent and attach れる', getHtmlString("読まれる")],
                           [getHtmlString("走る"), 'Replace る with the あ equivalent and attach れる', getHtmlString("走られる")],
                           ])
    f.write(table)

    f.write((printTitle('Rule 2')))
    f.write('For ru-verbs: Replace る with られる')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'Passive Form'],
                          [[getHtmlString("食べる"), 'replace る with られる', getHtmlString("食べられる ")],
                           ])
    f.write(table)

    f.write((printTitle('Rule 3')))
    f.write('For exceptions: する becomes される and くる becomes こられる')
    table = generateTable(['Dictionary Form', 'Conditional Form'],
                          [[getHtmlString("する"), 'される'],
                           [getHtmlString("くる"), 'こられる'],
                           ])
    f.write(table)
    f.write((printTitle('Conjugation to other forms')))
    # f.write('# Conjugation to other forms')
    f.write('\n')

    f.write('Luckily, all the passive is ending with る「ru」.Therefore, we can use conjugate from passive to other forms just like る verbs.')
    f.write('\n')
    f.write("### Plain form")
    table = generateTable(['', 'affirmative', 'negative'],
                          [["**present**", getHtmlString('読まれる'), getHtmlString("読まれない")],
                           [getHtmlString("**past**"), getHtmlString("読まれた"), getHtmlString("読まれなかった")],
                           [getHtmlString("**て-form**"), getHtmlString('読まれて'), ""],
                           ])
    f.write(table)

    f.write("### Polite form")
    table = generateTable(['', 'affirmative', 'negative'],
                          [["**present**", getHtmlString('読まれます'), getHtmlString("読まれません")],
                           [getHtmlString("**past**"), getHtmlString("読まれた"), getHtmlString("読まれませんでした")],
                           [getHtmlString("**て-form**"), getHtmlString('読まれて'), ""],
                           ])
    f.write(table)
