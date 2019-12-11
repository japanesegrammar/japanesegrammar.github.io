import re
from typing import Tuple, List, Optional

from functional import seq

import pykakasi

from python_utils.model import ForceReplace


def _getFromPair(pair):
    x = pair[0]
    y = pair[1]
    contents2 = re.findall('\[(.*?)\]', x)
    if len(contents2) > 0:
        startIndex = x.find('[')
        kanji = x[:startIndex].strip()
        hiragana = y
        newKanji, afterCommonHiragaIfExistedIsRemoved, reminderHiragana = _removeCommonHiraganaIfExist(kanji, hiragana)
        return f'[{newKanji}]' + "{" + f'{afterCommonHiragaIfExistedIsRemoved}' + "}" + f'{reminderHiragana}'
    return x


def _removeCommonHiraganaIfExist(kanji: str, hiragana: str) -> Tuple[str, str, str]:
    charList = list(set(kanji).intersection(hiragana))
    reminderHiragana = ''.join(charList)
    if len(charList) > 0:
        modifiedKanji = ''.join(list(set(kanji) - set(hiragana)))
        replacedHiragana = hiragana[:-len(charList)]    # assume that hiragana words are behind kanji
        return modifiedKanji, ''.join(replacedHiragana), reminderHiragana
    else:
        return kanji, hiragana, reminderHiragana


def isAllHiragana(text: str):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("J", "H")
    result = kakasi.getConverter().do(text)
    return result == text


def getHtmlString(text: str, forceReplaceList: Optional[List[ForceReplace]] = None):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("J", "aF")  # Japanese to furigana
    kakasi.setMode("s", True)
    conv = kakasi.getConverter()
    result1 = conv.do(text)

    kakasi = pykakasi.kakasi()
    kakasi.setMode("J", "H")  # Japanese to furigana
    kakasi.setMode("s", True)
    conv = kakasi.getConverter()
    result2 = conv.do(text)

    g1 = result1.split()
    g2 = result2.split()

    def performForceReplace(aFList: List[str], hList: List[str], v: ForceReplace):
        index, _ = seq(aFList).enumerate().filter(lambda x: v.kanji in x[1]).to_list()[0]
        hList[index] = v.hiragana
        return hList

    if forceReplaceList is not None:
        for f in forceReplaceList:
            g2 = performForceReplace(g1, g2, f)

    g = seq(zip(g1, g2)).map(lambda x: _getFromPair(x)).to_list()
    line = ' '.join(g).replace(' ', '').replace('-', ' ')
    return re.sub(r'\[(.*?)\]\{(.*?)\}', r'<ruby>\1<rp>（</rp><rt>\2</rt><rp>）</rp></ruby>', line)
