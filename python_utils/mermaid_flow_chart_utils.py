import string
from typing import List


def getMermaidScript():
    return '<script src="//cdn.jsdelivr.net/npm/mermaid@8.4.4/dist/mermaid.min.js"></script>'


# <div class="mermaid">
#       graph LR
#       A(聞く) -->|convert dictionary to stem verb| B(聞き)
#       B -->|combine with ながら| C(聞きながら)
# </div>

def getFlowChart(diagrams: List[str], inBetweenText: List[str]):
    assert len(diagrams) - 1 == len(inBetweenText)
    t1 = '<div class="mermaid"> \n'
    t2 = 'graph LR \n'
    t3 = '</div>'
    aToZ = string.ascii_uppercase[:len(diagrams)]
    links = []
    for i in range(len(diagrams)):
        if i != len(diagrams) - 1:
            p = f'{aToZ[i]}({diagrams[i]}) -->|{inBetweenText[i]}| {aToZ[i + 1]}({diagrams[i + 1]}) \n'
            links.append(p)

    return t1 + t2 + "".join(links) + t3


getFlowChart(["test", "test2", "test3"], ["pp", "gg"])


def getCssFlowChartWithTwoBlock(firstKanjiHtml: str, conversion: str, secondKanji: str):
    dash = '<div class="arrow">&mdash;</div>'
    arrow = '<div class="arrow">&rarr;</div>'
    t1 = '<div id="flowChart">'
    t2 = f'<div class="step">{firstKanjiHtml}</div>'
    t4 = f'<div class="nostep"   style="display: inline-block; white-space: nowrap;">{conversion}</div>'
    t5 = f'<div class="step">{secondKanji}</div>'
    t6 = '</div>'
    return t1 + t2 + dash + t4 + arrow + t5 + t6


def getCssFlowChartWithThreeBlock(firstKanjiHtml: str, firstConversion: str, secondKanji: str, secondConversion: str, thirdKanji):
    dash = '<div class="arrow">&mdash;</div>'
    arrow = '<div class="arrow">&rarr;</div>'
    t1 = '<div id="flowChart">'
    t2 = f'<div class="step">{firstKanjiHtml}</div>'
    t4 = f'<div class="nostep"   style="display: inline-block; white-space: nowrap;">{firstConversion}</div>'
    t5 = f'<div class="step">{secondKanji}</div>'
    t7 = f'<div class="nostep"   style="display: inline-block; white-space: nowrap;">{secondConversion}</div>'
    t8 = f'<div class="step">{thirdKanji}</div>'
    t9 = '</div>'
    return t1 + t2 + dash + t4 + arrow + t5 + dash + t7 + arrow + t8 + t9
