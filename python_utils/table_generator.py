from typing import List

from functional import seq


def generateTable(titles: List[str], contents: List[List[str]]):
    t0 = '\n \n'
    headerList = seq(titles).map(lambda x: f'| {x}')
    header = ''.join(headerList) + '\n'
    barList = seq(range(len(titles))).map(lambda x: '--- |')
    bar = ''.join(barList) + '\n'

    def generateContentCell(contentList: List[str]):
        temp = seq(contentList).map(lambda x: f'{x} |')
        return ''.join(temp) + '\n'

    contentsTableList = seq(contents).map(lambda x: generateContentCell(x)).to_list()
    return t0 + header + bar + ''.join(contentsTableList) + '\n'
