from python_utils.generator import generate, printBreakLine, generateVocab
from python_utils.model import TextPair, HighlightText, Color

print('###Case Study')
print('(1) When the speaker gueesses the reason or the cause as to what he has seen or heard an the confirms wherther he is correct.')
l1 = TextPair('渡辺さんは-時々-大阪弁を-使いますね。', 'Ms. Watanabe, you sometimes speak Osaka dialect.', [], addBullet=True)
l2 = TextPair('大阪に住んで いたんですか。', "Have you lived in Osaka?", highlightText= [HighlightText('んですか', Color.LIGHT_PINK)], addBreak=True)
l3 = TextPair('...ええ,15 歳まで 大阪に 住んで います。', "Yes, I lived in Osaka until I was fifteen.", [], forceReplaceList=[ForceReplace('歳', 'さい')])
print(generate([l1, l2, l3]))
printBreakLine()

print('(2) When the speaker asks for the information about what he has been heard.')
l1 = TextPair('おもしろい デザインの 靴ですね。どこで-買ったんですか。', 'The design of your shoes is interesting. Where did you buy them?',
              [HighlightText('んですか', Color.LIGHT_PINK)], addBullet=True, )
l2 = TextPair('イドヤストアで 買いました。', '...I bought this pair at Edoya Store.', )
print(generate([l1, l2]))
printBreakLine()


print('(3) When the speaker asks the listener to explain the reason or the cause of what he has seen or heard.')
l1 = TextPair('どうして 遅れたんですか。', 'Why were you late?', [HighlightText('んですか', Color.LIGHT_PINK)], addBullet=True, )
print(generate([l1]))

print('###Vocabulary')
print('<ol>')
print(generateVocab('時々', 'sometimes; at times;'))
print(generateVocab('大阪弁', 'Osaka dialect'))
print(generateVocab('使う', 'to use (a thing, method, etc.)'))
print(generateVocab('大阪', 'Osaka city'))
print(generateVocab('住む', 'to live; to reside;'))
print(generateVocab('靴', 'shoes; footwear;'))
print(generateVocab('買う', 'to buy; to purchase;'))
print(generateVocab('遅れる', 'to be late; to be delayed;'))
print(generateVocab('ストア', 'store; shop​;'))
print('</ol>')
