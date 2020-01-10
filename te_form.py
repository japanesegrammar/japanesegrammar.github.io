from python_utils.generator import printTitle, printSecondaryTitle, getInfoBlock
from python_utils.html_generator import getHtmlString
from python_utils.table_generator import generateTable

with open('te_form.md', 'w', encoding="utf-8") as f:
    f.write(printTitle('Verb て-Form (Te-Form)'))
    f.write('Te-forms are a very important part of Japanese grammar. You can use in the following forms.\n \n')
    f.write('- [V て-form + いただけませんか](v_te-form_+_itadakemasenka.md)\n')
    f.write('- [V て-form + います](v_te-form_iru.md)\n')
    f.write('- [V て-form + おきます](v_te-form_okimasu.md)\n')

    f.write((printTitle('Rule 1')))
    f.write('For ru-verbs: Replace る with て')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'て-Form'],
                          [[getHtmlString("食べる"), 'Replace る with て', getHtmlString("食べて")],
                           ])

    f.write(table)

    f.write((printTitle('Rule 2')))
    f.write('For u-verbs: we have 5 subs categories.')
    f.write(printSecondaryTitle('u-verbs with final う, つ and る'))
    f.write('For u-verbs ending with う, つ and る, we should replace with って.')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'て-Form'],
                          [[getHtmlString("会う"), 'Replace う with って', getHtmlString("会って")],
                           [getHtmlString("待つ"), 'Replace つ with って', getHtmlString("待って")],
                           [getHtmlString("とる"), 'Replace る with って', getHtmlString("とって")]
                           ])
    f.write(table)

    f.write(printSecondaryTitle('u-verbs with final む, ぶ and ぬ'))
    f.write('For u-verbs ending with む, ぶ and ぬ, we should replace with んで.')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'て-Form'],
                          [[getHtmlString("読む"), 'Replace む with んで', getHtmlString("読んで")],
                           [getHtmlString("遊ぶ"), 'Replace ぶ with んで', getHtmlString("遊んで")],
                           [getHtmlString("死ぬ"), 'Replace ぬ with んで', getHtmlString("死んで")]
                           ])
    f.write(table)
    f.write('\n')

    f.write(printSecondaryTitle('u-verbs with final く'))
    f.write('For u-verbs ending with く, we should replace with いて.')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'て-Form'],
                          [[getHtmlString("書く"), 'Replace く with いて', getHtmlString("書いて")],
                           ])
    f.write(table)
    f.write('\n')
    f.write(getInfoBlock('There is exception in this class. The て-form of ' + getHtmlString("行く") + f'is {getHtmlString("行って")}.'))

    f.write(printSecondaryTitle('u-verbs with final ぐ'))
    f.write('For u-verbs ending with ぐ, we should replace with いで.')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'て-Form'],
                          [[getHtmlString("泳ぐ"), 'Replace ぐ with いで', getHtmlString("泳いで")],
                           ])
    f.write(table)

    f.write(printSecondaryTitle('u-verbs with final す'))
    f.write('For u-verbs ending with す, we should replace with して.')
    table = generateTable(['Dictionary Form', 'Replacing Method', 'て-Form'],
                          [[getHtmlString("話す"), 'Replace す with して', getHtmlString("話して")],
                           ])
    f.write(table)

    f.write((printTitle('Rule 3')))
    f.write('For irregular verbs する and くる, we should replace as the following')

    table = generateTable(['Dictionary Form', 'て-Form'],
                          [[getHtmlString("する"), getHtmlString("して")],
                           [getHtmlString("くる"), getHtmlString("きて")],
                           ])

    f.write(table)
