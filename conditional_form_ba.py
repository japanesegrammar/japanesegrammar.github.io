from python_utils.generator import printTitle, generateCard, writeNewLine, generate, getInfoBlock, printSecondaryTitle
from python_utils.model import TextPair, HighlightText, Color, ForceReplace
from python_utils.html_generator import getHtmlString
from python_utils.mermaid_flow_chart_utils import getCssFlowChartWithTwoBlock, getCssFlowChartWithThreeBlock
from python_utils.model import TextPair, HighlightText, Color, ForceReplace
from python_utils.table_generator import generateTable
from python_utils.vocab_list import generateVocabLines

with open('conditional_form_ba.md', 'w', encoding="utf-8") as f:
    f.write('When using conditional form, first part of the sentence describes the requirement for something to happen; just like `IF` in English.')
    # f.write(printTitle('Conditional Form ば (Ba)'))
    # f.write(
    #     'In this lesson, we will learn how to change from dictionary form to conditional form to express condition in Japanese.')
    # cardText = '<b>Rule 1:</b> For u-verbs: Replace the u-vowel sound with the え equivalent and attach ば' + '\n' + '\n' + \
    #            '<b>Rule 2:</b> For ru-verbs: Replace る with れば' + '\n' + '\n' + \
    #            '<b>Rule 3:</b> For verb exceptions: する becomes すれば and くる becomes くらば' + '\n' + '\n' + \
    #            '<b>Rule 4:</b> For い-Adj:  Change the last い of the い-adjective into ければ' + '\n' + '\n' + \
    #            '<b>Rule 5:</b> For な-Adj: Change the last な of the な-adjective and attach なら' + '\n' + '\n' + \
    #            '<b>Rule 6:</b> For Noun: Attach なら to the noun'

    # f.write(generateCard(cardText, [], useLeft=True))

    f.write(printTitle('Prerequisite'))
    f.write(f'Please see [these rules](conditional_form.md) if you want to know how to do verb conjugation for conditional form.')
    writeNewLine(f)
    writeNewLine(f)
    f.write('\n')
    # we need to add this dummy. otherwise, there is brake line between explanation and example sentence
    l1 = TextPair('', '', [], )
    f.write(generate([l1]))

    # writeNewLine(f)
    # f.write('\n')
    f.write('<b>Example A : U-Verb</b>')
    l1 = TextPair('ボタンを 押せば、 窓が 開きます。', "If you press the button, the window will open.", [HighlightText('押せ', Color.LIGHT_GREEN), HighlightText('ば', Color.LIGHT_PINK)], addBullet=True,
                  forceReplaceList=[ForceReplace('開き', "あき")])
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example B: U-Verb</b>')
    l1 = TextPair('彼が 行けば、私も行きます。', "If he goes, I will go too.", [HighlightText('行け', Color.LIGHT_GREEN), HighlightText('ば', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)
    f.write('\n')

    f.write('<b>Example C: Ru-Verb</b>')
    f.write('<br>')
    f.write('In this example, we convert `食べる` to `食べ` and attach `れば` to form a sentence.')
    l1 = TextPair('これを食べれば 健康になる。', "If you eat this, you will be healthy.", [HighlightText('食べ', Color.LIGHT_GREEN), HighlightText('れば', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)
    f.write('\n')

    #  電話すればよかったのに。
    # これを食べれば健康になる

    f.write('<b>Example D: Suru-Verb</b>')
    f.write('<br>')
    f.write('In this example, we replace with `する` with `すれば` to form a sentence.')
    l1 = TextPair('電話すれば よかったのに。', "You should've called.", [HighlightText('電話', Color.LIGHT_GREEN), HighlightText('すれば', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)
    f.write('\n')

    f.write('<b>Example E: I-Adjective</b>')
    f.write('<br>')
    f.write('In this example, we convert `安い` to `安` and attach `ければ` to form a sentence.')
    f.write(
        '<div class="grid-container"><div class="grid-item"> <li> もう <ruby>少<rp>（</rp><rt>すこ</rt><rp>）</rp></ruby>し <mark class="light_green"><ruby>安<rp>（</rp><rt>やす</rt><rp>）</rp></ruby></mark><mark class="light_pink">ければ</mark>．．． </li> </div><div class="grid-item"> If a little cheaper. . . </div></div><br>')

    f.write('<b>Example F: Na-Adjective</b>')
    f.write('<br>')
    f.write('In this example, we are attaching `なら` to `暇` (Na-Adjective) to form a sentence.')
    l1 = TextPair('暇なら、手伝ってください。', "If you are free, please help.", [HighlightText('暇', Color.LIGHT_GREEN), HighlightText('なら', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)
    f.write('\n')

    f.write('<b>Example G: Noun</b>')
    f.write('<br>')
    f.write('In this example, we are attaching `なら` to `天気` (Noun) to form a sentence.')

    l1 = TextPair('いい 天気なら、向こうに 島が 見えます。', "When it is fine, an island can be seen over there.", [HighlightText('天気', Color.LIGHT_GREEN), HighlightText('なら', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)
    f.write('\n')

    # f.write('<b>Example C</b>')
    #
    #
    #
    # l1 = TextPair('もう 少し 安ければ．．．', "If a little cheaper. . .", [HighlightText('安', Color.LIGHT_GREEN), HighlightText('ければ', Color.LIGHT_PINK)], addBullet=True)
    # f.write(generate([l1]))
    # writeNewLine(f)
    #
    # f.write('\n')
    # f.write('<b>Example C</b>')
    # l1 = TextPair('もう 少し 安ければ．．．', "If a little cheaper. . .", [HighlightText('安け', Color.LIGHT_GREEN), HighlightText('ければ', Color.LIGHT_PINK)], addBullet=True)
    # f.write(generate([l1]))
    # writeNewLine(f)

    # f.write('もう少し安ければ．．．')

    # f.write((printTitle('')))
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

    f.write(getInfoBlock('You should attach `であれば` to な-Adj when you want to use it for writing report/formal write up because なら form is usually used in conversion.'))

    f.write((printTitle('Rule 6')))
    f.write('For Noun: Attach なら to the noun')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'Conditional Form'],
                          [[getHtmlString("雨"), 'attach なら', getHtmlString("雨なら ")],
                           ])
    f.write(table)

    f.write(getInfoBlock('You should attach `であれば` to Noun when you want to use it for writing report/formal write up because なら form is usually used in conversion.'))
