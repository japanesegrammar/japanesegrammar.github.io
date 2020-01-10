import collections
import re
from typing import Tuple, List, Optional

import pykakasi
from functional import seq

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


def _removeCommonHiraganaIfExist(japaneseText: str, hiragana: str) -> Tuple[str, str, str]:
    # the following line does same as set function. but set can sometimes change order so don't use set
    charList = seq(collections.OrderedDict.fromkeys(x for x in japaneseText if x in hiragana)).map(lambda x: x[0]).to_list()
    reminderHiragana = ''.join(charList)
    if len(charList) > 0:
        a = collections.OrderedDict.fromkeys(japaneseText)
        b = collections.OrderedDict.fromkeys(hiragana)
        kanjiOnlyList = seq(collections.OrderedDict.fromkeys(x for x in a if x not in b)).map(lambda x: x[0]).to_list()
        kanjiOnly = ''.join(kanjiOnlyList)
        replacedHiragana = hiragana[:-len(charList)]  # assume that hiragana words are behind kanji
        return kanjiOnly, ''.join(replacedHiragana), reminderHiragana
    else:
        return japaneseText, hiragana, reminderHiragana


def isAllHiragana(text: str):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("J", "H")
    result = kakasi.getConverter().do(text)
    return result == text


def generateFuriganaHtml(t: str) -> str:
    line = ' '.join(t).replace(' ', '').replace('-', ' ')
    return re.sub(r'\[(.*?)\]\{(.*?)\}', r'<ruby>\1<rp>（</rp><rt>\2</rt><rp>）</rp></ruby>', line)


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
