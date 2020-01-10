from python_utils.generator import printTitle, generateCard, writeNewLine, generate, getInfoBlock
from python_utils.html_generator import getHtmlString
from python_utils.model import TextPair, HighlightText, Color
from python_utils.vocab_list import generateVocabLines

with open('v_te-form_iru.md', 'w') as f:
    f.write(printTitle('Usage Form'))
    f.write('\n')
    f.write(generateCard('V て-form + います', [('light_green', 'V て-form'), ('light_pink', 'います')]))
    f.write('\n')

    f.write((printTitle('To describe continuous states')))
    writeNewLine(f)

    f.write('You can describe what kind of action is in progress by using the helping verb `ている`.')
    l1 = TextPair('スーさんは 今勉強 しています。', 'Sue is studying now.', [HighlightText('して', Color.LIGHT_GREEN), HighlightText('います', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)
    writeNewLine(f)
    f.write('You could also add `まだ` to show that the state is on going.')
    l1 = TextPair('まだ 雨が 降っています。', 'It is still raining.', [HighlightText('まだ', Color.LIGHT_INDIGO), HighlightText('降って', Color.LIGHT_GREEN), HighlightText('います', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))

    f.write((printTitle('To describe habitual actions')))
    f.write('\n')
    morning = getHtmlString('毎朝')
    f.write('You can also use `ている` to describe habitual actions.' + f'There is a time indicator such as {morning} to show when actions are occurring regularly.')
    l1 = TextPair('毎朝 ジョギングを しています。', 'I jog every morning.', [HighlightText('毎朝', Color.LIGHT_INDIGO), HighlightText('して', Color.LIGHT_GREEN), HighlightText('います', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)
    f.write('\n')

    f.write((printTitle('To describe occupation')))
    f.write('You can describe what a person does by occupation.')
    l1 = TextPair('私は 英語を 教えています。', 'I teach English.', [HighlightText('教えて', Color.LIGHT_GREEN), HighlightText('います', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    writeNewLine(f)
    f.write(getInfoBlock('This sentence has two meanings; You are teaching English right now OR You are an English teacher. Just like in English language `I am teaching English` which can be interpreted in two ways.'))
    writeNewLine(f)
    f.write((printTitle('To describe change in state')))
    writeNewLine(f)
    f.write('This `ています` describe changes from one state to another; indicate the significant change from the past to the current state.')
    l1 = TextPair('トムさんは ちょっと 太っています。', 'Tom is a little fat.', [HighlightText('太って', Color.LIGHT_GREEN), HighlightText('います', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    f.write('\n')
    f.write(getInfoBlock('Previously Tom is not chubby. But now he is in a little overweight state.'))
    f.write('\n')
    l1 = TextPair('トムさんは 結婚しています。', 'Tom is married.', [HighlightText('結婚して', Color.LIGHT_GREEN), HighlightText('います', Color.LIGHT_PINK)], addBullet=True)
    f.write(generate([l1]))
    f.write('\n')
    f.write(getInfoBlock('Previously Tom is single. But now he is no longer single. Note that it does not mean `Tom is getting married`.'))

    # to generate vocab
    vocabListInThisPage = ['今', '勉強', '毎朝', 'ジョギング', '私', '英語', '教える', '太る', '結婚', '雨', '降る']
    vocabLines = generateVocabLines(vocabListInThisPage)
    f.write(vocabLines)
