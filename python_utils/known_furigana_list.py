from dataclasses import dataclass
from typing import List

from functional import seq


@dataclass
class Furigana:
    kanji: str
    hiraganaList: List[str]


_KNOWN_FURIGANA_LIST = [
    Furigana('友', ['とも']),
    Furigana('言', ['い']),
    Furigana('映画', ['えいが']),
    Furigana('見', ['み']),
]


def generateFuriganaText(v: str, kanjiList: List[str]) -> str:
    modifiableText = v
    knownKanjiList = seq(_KNOWN_FURIGANA_LIST).map(lambda x: x.kanji).to_list()
    for k in kanjiList:
        assert k in knownKanjiList
        h = seq(_KNOWN_FURIGANA_LIST).filter(lambda x: x.kanji == k).to_list()
        assert len(h) == 1
        modifiableText = modifiableText.replace(k, "[" + k + "]" + '{' + h[0].hiraganaList[0] + "}")

    return modifiableText
