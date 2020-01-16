from python_utils.generator import printTitle, getInfoBlock, printSecondaryTitle, generateCard
from python_utils.html_generator import getHtmlString
from python_utils.table_generator import generateTable

with open('past_tense_form.md', 'w', encoding="utf-8") as f:
    f.write(printTitle('Past Tense Verb Conjugation Rules'))
    # f.write('In this lesson, we will learn how to form the past and past-negative verbs. You can use in the following forms.\n \n')
    f.write('\n')

    # cardText = '<b>Rule 1:</b> For u-verbs: Replace the u-vowel sound with the お equivalent and attach う' +  '<br>' \
    #            '<b>Rule 2:</b> For ru-verbs: Replace る with よう' + '\n' + '\n' + \
    #            '<b>Rule 3:</b> For exceptions: する becomes しよう and くる becomes こよう'

    cardText = '<b>Rule 1:</b> For ru-verbs: Replace る with た' + '<br>' + \
               '<b>Rule 2:</b> <br> &emsp; For u-verbs ending with う, つ and る: Replace those ending with った' + '<br>' + \
               '&emsp; For u-verbs ending with む, ぶ and ぬ: Replace those ending with んだ' + '<br>' + \
               '&emsp; For u-verbs ending with く: Replace those ending with いて' + '<br>' + \
               '&emsp; For u-verbs ending with ぐ: Replace those ending with いだ' + '<br>' + \
               '&emsp; For u-verbs ending with す: Replace those ending with した' + '<br>' + \
               '&emsp; u-verbs exception: past tense form of 行く is 行った' + '<br>' + \
               '<b>Rule 3:</b> For exceptions: する becomes した and くる becomes きた'

    f.write(generateCard(cardText, [], useLeft=True))

    f.write((printTitle('Rule 1')))
    f.write('For ru-verbs: Replace `る` with `た`')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'Past Tense Form'],
                          [[getHtmlString("食べる"), 'Replace る with た', getHtmlString("食べた")],
                           ])

    f.write(table)

    f.write((printTitle('Rule 2')))
    f.write('For u-verbs: we have 5 subs categories.')
    f.write(printSecondaryTitle('u-verbs with final う, つ and る'))
    f.write('For u-verbs ending with う, つ and る, we should replace with った.')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'Past Tense Form'],
                          [[getHtmlString("会う"), 'Replace う with った', getHtmlString("会った")],
                           [getHtmlString("待つ"), 'Replace つ with った', getHtmlString("待った")],
                           [getHtmlString("とる"), 'Replace る with った', getHtmlString("とった")]
                           ])
    f.write(table)

    f.write(printSecondaryTitle('u-verbs with final む, ぶ and ぬ'))
    f.write('For u-verbs ending with む, ぶ and ぬ, we should replace with んだ.')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'Past Tense Form'],
                          [[getHtmlString("読む"), 'Replace む with んで', getHtmlString("読んだ")],
                           [getHtmlString("遊ぶ"), 'Replace ぶ with んで', getHtmlString("遊んだ")],
                           [getHtmlString("死ぬ"), 'Replace ぬ with んで', getHtmlString("死んだ")]
                           ])
    f.write(table)
    f.write('\n')

    f.write(printSecondaryTitle('u-verbs with final く'))
    f.write('For u-verbs ending with く, we should replace with いて.')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'Past Tense Form'],
                          [[getHtmlString("書く"), 'Replace く with いた', getHtmlString("書いた")],
                           ])

    f.write(table)
    f.write('\n')
    f.write(getInfoBlock('There is exception in this class. The て-form of ' + getHtmlString("行く") + f'is {getHtmlString("行った")}.'))

    f.write(printSecondaryTitle('u-verbs with final ぐ'))
    f.write('For u-verbs ending with ぐ, we should replace with いで.')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'て-Form'],
                          [[getHtmlString("泳ぐ"), 'Replace ぐ with  いだ', getHtmlString("泳いだ")],
                           ])
    f.write(table)

    f.write(printSecondaryTitle('u-verbs with final す'))
    f.write('For u-verbs ending with す, we should replace with した.')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'Past Tense Form'],
                          [[getHtmlString("話す"), 'Replace す with した', getHtmlString("話した")],
                           ])
    f.write(table)

    f.write((printTitle('Rule 3')))
    f.write('For irregular verbs する and くる, we should replace as the following')

    table = generateTable(['Dictionary Form', 'て-Form'],
                          [[getHtmlString("する"), getHtmlString("した")],
                           [getHtmlString("くる"), getHtmlString("きた")],
                           ])

    f.write(table)
