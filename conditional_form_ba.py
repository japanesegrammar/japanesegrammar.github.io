from python_utils.generator import printTitle, generateCard, writeNewLine, generate, getInfoBlock, printSecondaryTitle
from python_utils.model import TextPair, HighlightText, Color, ForceReplace
from python_utils.html_generator import getHtmlString
from python_utils.mermaid_flow_chart_utils import getCssFlowChartWithTwoBlock, getCssFlowChartWithThreeBlock
from python_utils.model import TextPair, HighlightText, Color, ForceReplace
from python_utils.table_generator import generateTable
from python_utils.vocab_list import generateVocabLines

with open('conditional_form_ba.md', 'w', encoding="utf-8") as f:
    f.write('When using conditional form, first part of the sentence describes the requirement for something to happen; just like `IF` in English.')

    f.write(printTitle('Prerequisite'))
    f.write(f'Please see [these rules](conditional_form.md) if you want to know how to do verb conjugation for conditional form.')
    writeNewLine(f)
    writeNewLine(f)
    f.write('\n')
    # we need to add this dummy. otherwise, there is brake line between explanation and example sentence
    l1 = TextPair('', '', [], )
    f.write(generate([l1]))

    f.write('<b>Example A : U-Verb</b>')
    f.write('<br>')
    f.write('In this example, we should convert `押す` to `押せ` to get え equivalent sound. And then attach `ば` to obtain the final form `押せば`.')
    l1 = TextPair('ボタンを 押せば、 窓が 開きます。', "If you press the button, the window will open.", [HighlightText('押せ', Color.LIGHT_GREEN), HighlightText('ば', Color.LIGHT_PINK)], addBullet=True,
                  forceReplaceList=[ForceReplace('開き', "あき")])
    f.write(generate([l1]))
    writeNewLine(f)

    f.write('<b>Example B: U-Verb</b>')
    f.write('<br>')
    f.write('In this example, we should convert `行く` to `行け` to get え equivalent sound. And then attach `ば` to obtain the final form `行けば`.')
    l1 = TextPair('彼が 行けば、私も行きます。', "If he goes, I will go too.", [HighlightText('行け', Color.LIGHT_GREEN), HighlightText('ば', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)
    f.write('\n')

    f.write('<b>Example C: Ru-Verb</b>')
    f.write('<br>')
    f.write('In this example, we convert `食べる` to `食べ` and attach `れば` to get the final form `食べれば`.')
    l1 = TextPair('これを食べれば 健康になる。', "If you eat this, you will be healthy.", [HighlightText('食べ', Color.LIGHT_GREEN), HighlightText('れば', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)
    f.write('\n')

    f.write('<b>Example D: Suru-Verb</b>')
    f.write('<br>')
    f.write('In this example, we should convert `する` dictionary form to the final form `すれば`.')
    l1 = TextPair('電話すれば よかったのに。', "You should've called.", [HighlightText('電話', Color.LIGHT_GREEN), HighlightText('すれば', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)
    f.write('\n')

    f.write('<b>Example E: I-Adjective</b>')
    f.write('<br>')
    f.write('In this example, we change from `安い` to `安` and attach `ければ` to get the final form `安いければ`.')
    f.write(
        '<div class="grid-container"><div class="grid-item"> <li> もう <ruby>少<rp>（</rp><rt>すこ</rt><rp>）</rp></ruby>し <mark class="light_green"><ruby>安<rp>（</rp><rt>やす</rt><rp>）</rp></ruby></mark><mark class="light_pink">ければ</mark>．．． </li> </div><div class="grid-item"> If a little cheaper. . . </div></div><br>')

    f.write('<b>Example F: Na-Adjective</b>')
    f.write('<br>')
    f.write('In this example, we are attaching `なら` to `暇` (Na-Adjective) to obtain the final form `暇なら`.')
    l1 = TextPair('暇なら、手伝ってください。', "If you are free, please help.", [HighlightText('暇', Color.LIGHT_GREEN), HighlightText('なら', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)
    f.write('\n')

    f.write('<b>Example G: Noun</b>')
    f.write('<br>')
    f.write('In this example, we are attaching `なら` to `天気` (Noun) to get the final form `天気なら`.')

    l1 = TextPair('いい 天気なら、向こうに 島が 見えます。', "When it is fine, an island can be seen over there.", [HighlightText('天気', Color.LIGHT_GREEN), HighlightText('なら', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)
    f.write('\n')

    vocabListInThisPage = ['押す', '窓', '行く', '開く', '彼', '私', '食べる', '健康', '電話', '安い', '暇', '手伝う', '天気', '向こう', '島', '見える']
    vocabLines = generateVocabLines(vocabListInThisPage)
    f.write(vocabLines)
