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
