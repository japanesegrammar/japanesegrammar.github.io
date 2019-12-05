from dataclasses import dataclass
from typing import List

from functional import seq

from python_utils.generator import generateVocab
from python_utils.html_generator import getHtmlString


@dataclass
class Vocab:
    kanjiOrOther: str
    meaning: str
    isItKanji: bool = True

    @property
    def getHtmlString(self):
        vocab = getHtmlString(self.kanjiOrOther) if self.isItKanji else self.kanjiOrOther
        return '<li>' + vocab + '  ⇌  ' + self.meaning + '</li>'


# print('###Vocabulary')
# print('<ol>')
# print(generateVocab('先生 ', 'teacher'))
# print(generateVocab('紹介', 'introduction'))
# print(generateVocab('写真', 'photo; picture'))
# print(generateVocab('撮る', 'to take (a photo)'))
# print('</ol>')

_KNOWN_VOCAB_LIST = [Vocab('勉強', 'study'),
                     Vocab('今', 'now; the present time'),
                     Vocab('毎朝 ', 'every morning​'),
                     Vocab('ジョギング', 'jogging', isItKanji=False),
                     Vocab('私', 'I; me​'),
                     Vocab('英語', 'English language'),
                     Vocab('教える', 'to teach; to instruct​'),
                     Vocab('太る', 'to put on weight; to gain weight'),
                     Vocab('結婚', 'marriage​'),
                     Vocab('先生 ', 'teacher'),
                     ]


def generateVocabLines(vocabList: List[str]) -> str:
    filteredList = seq(_KNOWN_VOCAB_LIST).filter(lambda x: x.kanjiOrOther in vocabList)
    l1 = f'\n##Vocabulary\n'
    l2 = f'<ol>'
    v = seq(filteredList).map(lambda x: x.getHtmlString).to_list()
    l3 = ''.join(v)
    l4 = f'</ol>'
    return l1 + l2 + l3 + l4
