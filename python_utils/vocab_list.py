from dataclasses import dataclass
from typing import List

from functional import seq

from python_utils.html_generator import getHtmlString
from python_utils.model import ForceReplace


@dataclass
class Vocab:
    kanjiOrOther: str
    meaning: str
    isItKanji: bool = True
    forceWord: ForceReplace = None

    @property
    def getHtmlString(self):
        if self.forceWord is not None:
            vocab = getHtmlString(self.kanjiOrOther, forceReplaceList=[self.forceWord]) if self.isItKanji else self.kanjiOrOther
        else:
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
                     Vocab('夏', 'summer'),
                     Vocab('川', 'river, stream'),
                     Vocab('泳ぐ', 'to swim'),
                     Vocab('待つ', 'to wait'),
                     Vocab('ご飯', 'cooked rice; meal', forceWord=ForceReplace('飯', 'はん')),
                     Vocab('食べる', 'to eat'),
                     Vocab('今夜', 'this evening; tonight'),
                     Vocab('早く', 'early; soon; quickly; swiftly'),
                     Vocab('寝る', 'to sleep, to lie down'),
                     Vocab('一緒に', 'together'),
                     Vocab('卒業', 'graduation; completion (e.g. of a course)​'),
                     Vocab('年後', 'years later'),
                     Vocab('来る', 'to come back; to become'),
                     Vocab('手伝う', 'to help; to assist'),
                     Vocab('友だち', 'friend'),
                     Vocab('言う', 'to say; to utter'),
                     Vocab('映画', 'movie; film'),
                     Vocab('見る', 'to see; to look'),
                     Vocab('園庭', 'garden'),
                     Vocab('散歩', 'walk; stroll'),
                     Vocab('試食', 'food sampling'),
                     Vocab('週末', 'weekend'),
                     Vocab('海', 'sea; ocean'),
                     Vocab('行く', 'to go; to move'),
                     Vocab('思う', 'to think; to consider'),
                     Vocab('今から', 'from now; from this time forward'),
                     Vocab('銀行', 'bank'),
                     Vocab('外国', 'foreign country'),
                     Vocab('働く', 'to work'),
                     Vocab('約束', 'arrangement; appointment'),
                     Vocab('時間', 'time​; period'),
                     Vocab('間に', 'while; during'),
                     Vocab('合う', 'to meet'),
                     Vocab('時期', 'time; season; period'),
                     Vocab('少し', 'small quantity; little; few'),
                     Vocab('安い', 'cheap; calm; peaceful; quiet'),
                     Vocab('画家', 'painter; artist'),
                     Vocab('一番', 'best; most; number one'),
                     Vocab('有名', 'famous'),
                     Vocab('楽しい', 'enjoyable; fun'),
                     Vocab('薬', 'medicine'),
                     Vocab('飲む', 'to drink'),
                     Vocab('音楽', 'music'),
                     Vocab('聞く', 'to hear; to listen (music)'),
                     Vocab('日本語', 'Japanese (language)​'),
                     Vocab('歌', 'song'),
                     Vocab('歌う', 'to sing'),
                     Vocab('洗濯', 'washing; laundry'),
                     Vocab('アルバイト', 'part-time job; side job', isItKanji=False),
                     Vocab('学校', 'school​'),
                     Vocab('大変', 'difficult; terrible; immense; greatly; terribly'),
                     Vocab('押す', 'to push; to press​'),
                     Vocab('窓', 'window​'),
                     Vocab('開く', 'to open'),
                     Vocab('健康', 'health​; health​y'),
                     Vocab('電話', 'telephone call; phone call​; telephone'),
                     Vocab('暇', 'spare time; free time '),
                     Vocab('天気', 'weather'),
                     Vocab('向こう', 'over there; that way; far away'),
                     Vocab('島', 'island​'),
                     Vocab('見える', 'to be seen; to be in sight​'),
                     Vocab('東京', 'Tokyo​'),
                     Vocab('連絡', 'to contact; to get in touch'),
                     Vocab('練習', 'to practice'),
                     Vocab('日本人', 'Japanese person; Japanese people'),
                     Vocab('言葉', 'language; dialect​; words; speech'),
                     Vocab('知る', 'to know; to notice; to comprehend'),
                     Vocab('元気', 'lively; healthy; in good health​'),
                     Vocab('水泳', 'swimming'),
                     ]


def generateVocabLines(vocabList: List[str]) -> str:
    for v in vocabList:
        if v not in seq(_KNOWN_VOCAB_LIST).map(lambda x: x.kanjiOrOther).to_list():
            assert False, f'This vocab is {v} in the list yet.'

    filteredList = seq(_KNOWN_VOCAB_LIST).filter(lambda x: x.kanjiOrOther in vocabList).to_list()
    assert len(filteredList) == len(vocabList)  # there will be error if there is duplicated vocab in vocabList
    l1 = f'\n##Vocabulary\n'
    l2 = f'<ol>'
    v = seq(filteredList).map(lambda x: x.getHtmlString).to_list()
    l3 = ''.join(v)
    l4 = f'</ol>'
    return l1 + l2 + l3 + l4
