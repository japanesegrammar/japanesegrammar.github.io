from typing import List, Tuple

from functional import seq

from python_utils.html_generator import getHtmlString, isAllHiragana
from python_utils.model import TextPair


def printTitle(text: str):
    return f'\n## {text} \n'


def generateCard(text: str, pairs: List[Tuple[str, str]]):
    '<div class="card">   <span><mark class="light_green">V て-form</mark> + <mark class="light_pink">いただけませんか</mark></span></div>'

    t1 = '<div class="card">'
    newText = text
    for p in pairs:
        newText = newText.replace(p[1], f'<mark class="{p[0]}">{p[1]}</mark>')

    return t1 + newText + '</div>'


def generate(pairs: List[TextPair]) -> str:
    head = '<div class="grid-container">'
    tail = '</div>'
    return head + seq(pairs).map(lambda x: generateItem(x)).make_string('') + tail


def generateItem(pair: TextPair):
    head = '<div class="grid-item">'
    tail = '</div>'
    newJapaneseText = pair.japaneseText.replace(' ', '-')  # this will replace space with '-' to make space later on
    furigana = getHtmlString(newJapaneseText, pair.forceReplaceList)
    if len(pair.highlightText) == 0:
        newFurigana = furigana
        # print('here')
    else:
        for t in pair.highlightText:
            if not isAllHiragana(t.text):
                r = getHtmlString(t.text)
                furigana = furigana.replace(r, f'<mark class="{t.color.value}">{r}</mark>')
            else:

                furigana = furigana.replace(t.text, f'<mark class="{t.color.value}">{t.text}</mark>')
        newFurigana = furigana

    t1 = f'{head} {newFurigana} {tail}' if not pair.addBullet else f'{head} <li> {newFurigana} </li> {tail}'
    t2 = f'{head} {pair.englishText} {tail}' if not pair.addBreak else f'{head} {pair.englishText} <br><br> {tail}'
    return t1 + t2


def generateVocab(kanjiOrOther: str, meaning: str, isItKanji: bool = True) -> str:
    vocab = getHtmlString(kanjiOrOther) if isItKanji else kanjiOrOther
    return '<li>' + vocab + '  ⇌  ' + meaning + '</li>'


def printBreakLine():
    print('---')


def writeNewLine(f):
    f.write('\n')


def getInfoBlock(info: str) -> str:
    return f'\n!!! info \n \t {info}'
