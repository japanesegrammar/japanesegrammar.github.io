from typing import List, Tuple

from functional import seq

from python_utils.html_generator import getHtmlString, isAllHiragana, generateFuriganaHtml
from python_utils.known_furigana_list import generateFuriganaText
from python_utils.model import TextPair, FuriganaGridItem


def printTitle(text: str):
    return f'\n## {text} \n'


def generateCard(text: str, pairs: List[Tuple[str, str]], useLeft: bool = False):
    '<div class="card">   <span><mark class="light_green">V て-form</mark> + <mark class="light_pink">いただけませんか</mark></span></div>'

    t1 = '<div class="card_left">' if useLeft else '<div class="card">'
    newText = text
    for p in pairs:
        newText = newText.replace(p[1], f'<mark class="{p[0]}">{p[1]}</mark>')

    return t1 + newText + '</div>'


def generate(pairs: List[TextPair]) -> str:
    head = '<div class="grid-container">'
    tail = '</div>'
    return head + seq(pairs).map(lambda x: generateItem(x)).make_string('') + tail


def generateGridContainer(pairs: List[FuriganaGridItem]):
    head = '<div class="grid-container">'
    tail = '</div>'
    return head + seq(pairs).map(lambda x: generateGridItem(x)).make_string('') + tail


# https://stackoverflow.com/questions/35091557/replace-nth-occurrence-of-substring-in-string
def nth_repl(s, sub, repl, nth):
    find = s.find(sub)
    # if find is not p1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != nth:
        # find + 1 means we start at the last match start index + 1
        find = s.find(sub, find + 1)
        i += 1
    # if i  is equal to nth we found nth matches so replace
    if i == nth:
        return s[:find] + repl + s[find + len(sub):]
    return s


def generateItem(pair: TextPair):
    head = '<div class="grid-item">'
    tail = '</div>'
    newJapaneseText = pair.japaneseText.replace(' ', '-')  # this will replace space with '-' to make space later on
    furigana = getHtmlString(newJapaneseText, pair.forceReplaceList)
    if len(pair.highlightText) == 0:
        newFurigana = furigana
    else:
        for t in pair.highlightText:
            if not isAllHiragana(t.text):
                r = getHtmlString(t.text)
                furigana = furigana.replace(r, f'<mark class="{t.color.value}">{r}</mark>')
            else:
                if t.replaceAt is not None:
                    furigana = nth_repl(furigana, t.text, f'<mark class="{t.color.value}">{t.text}</mark>', t.replaceAt)
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
    f.write('<br>')


def getInfoBlock(info: str) -> str:
    return f'\n!!! info \n \t {info}'


def generateGridItem(pair: FuriganaGridItem):
    head = '<div class="grid-item">'
    tail = '</div>'
    newJapaneseText = pair.japaneseText.replace(' ', '-')  # this will replace space with '-' to make space later on
    furigana = generateFuriganaText(newJapaneseText, pair.kanjiTextList)
    furiganaHtml = generateFuriganaHtml(furigana)

    # furiganaHtml = getHtmlString(newJapaneseText, pair.forceReplaceList)
    if len(pair.highlightText) == 0:
        newFurigana = furiganaHtml
    else:
        for t in pair.highlightText:
            if not isAllHiragana(t.text):
                r = getHtmlString(t.text)
                furiganaHtml = furiganaHtml.replace(r, f'<mark class="{t.color.value}">{r}</mark>')
            else:
                if t.replaceAt is not None:
                    furiganaHtml = nth_repl(furiganaHtml, t.text, f'<mark class="{t.color.value}">{t.text}</mark>', t.replaceAt)
                else:
                    furiganaHtml = furiganaHtml.replace(t.text, f'<mark class="{t.color.value}">{t.text}</mark>')

        newFurigana = furiganaHtml

    t1 = f'{head} {newFurigana} {tail}' if not pair.addBullet else f'{head} <li> {newFurigana} </li> {tail}'
    t2 = f'{head} {pair.englishText} {tail}' if not pair.addBreak else f'{head} {pair.englishText} <br><br> {tail}'
    return t1 + t2
