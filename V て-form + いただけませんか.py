from python_utils.generator import generate, printBreakLine, generateVocab
from python_utils.model import TextPair, HighlightText, Color

l1 = TextPair('いい 先生を 紹介して いただけませんか。', 'Would you please introduce a good teacher to me?', [HighlightText('紹介して', Color.LIGHT_GREEN), HighlightText('いただけませんか', Color.LIGHT_PINK)] , addBullet=True)
print(generate([l1]))
printBreakLine()
l2 = TextPair('写真を 撮って いただけませんか。', 'Would you please take a picture?', [HighlightText('撮って', Color.LIGHT_GREEN), HighlightText('いただけませんか', Color.LIGHT_PINK)], addBullet=True)
print(generate([l2]))

print('###Vocabulary')
print('<ol>')
print(generateVocab('先生 ', 'teacher'))
print(generateVocab('紹介', 'introduction'))
print(generateVocab('写真', 'photo; picture'))
print(generateVocab('撮る', 'to take (a photo)'))
print('</ol>')