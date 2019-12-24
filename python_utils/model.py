from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List


class Color(Enum):
    LIGHT_PINK = 'light_pink'
    LIGHT_GREEN = 'light_green'
    LIGHT_INDIGO = 'light_indigo'


@dataclass
class ForceReplace:
    kanji: str
    hiragana: str


@dataclass
class HighlightText:
    text: str
    color: Color
    replaceAt: Optional[int] = None


@dataclass
class TextPair:
    japaneseText: str
    englishText: str
    highlightText: Optional[List[HighlightText]] = field(default_factory=lambda: [])
    addBreak: bool = False
    addBullet: bool = False
    forceReplaceList: Optional[List[ForceReplace]] = None

@dataclass
class FuriganaGridItem:
    japaneseText: str
    kanjiTextList: List[str]
    englishText: str
    highlightText: Optional[List[HighlightText]] = field(default_factory=lambda: [])
    addBreak: bool = False
    addBullet: bool = False

@dataclass
class FuriganaPair:
    kanji: str
    hiragana: str

@dataclass
class NewTextPair:
    japaneseText: str
    kanjiList: List[str]
