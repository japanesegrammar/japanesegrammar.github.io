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
                     Vocab('雨', 'rain'),
                     Vocab('降る', 'to fall (of rain, snow, ash, etc.)'),
                     Vocab('旅行', 'travel; trip'),
                     Vocab('切符', 'ticket​'),
                     Vocab('買う', 'buy; purchase'),
                     Vocab('来週', 'next week​'),
                     Vocab('レポート', 'report', isItKanji=False),
                     Vocab('書く', 'to write; to compose'),
                     Vocab('使う', 'to use (a thing, method, etc.); to make use of'),
                     Vocab('元', 'origin; source'),
                     Vocab('場所', 'place; location'),
                     Vocab('戻す', 'to put back'),
                     Vocab('彼', 'he; him'),
                     Vocab('部屋', 'room'),
                     ]


def generateVocabLines(vocabList: List[str]) -> str:
    filteredList = seq(_KNOWN_VOCAB_LIST).filter(lambda x: x.kanjiOrOther in vocabList)
    l1 = f'\n##Vocabulary\n'
    l2 = f'<ol>'
    v = seq(filteredList).map(lambda x: x.getHtmlString).to_list()
    l3 = ''.join(v)
    l4 = f'</ol>'
    return l1 + l2 + l3 + l4
