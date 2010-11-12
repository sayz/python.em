import re
from Stacks import *

def HtmlChecker(Html):

    fin = open(Html)
    fin = fin.read()
    HtmlList = re.findall(r'<[/]*\w+[^>]*>', fin)
    HtmlList = [i for i in HtmlList if i[-2]!='/']
    newList = list()
    for i in HtmlList:
        if ' ' in i:
            a = i.find(' ')
            newList.append(i[:a] + '>')
        else:
            newList.append(i)


    s = Stack()
    balanced = True
    index = 0

    while index < len(newList) and balanced:
        string = newList[index]
        if not "/" in string:
            s.push(string)
        else:
            if s.isEmpty():
                balanced = False
                print string,"tagi hic acilmadi!"
            else:
                top = s.pop()
                if not matches(top, string):
                    if not s.ins(string[0]+string[2:]):
                        print string, "tagi hic acilmadi!"
                    else:
                        balanced = False
                        print "Acik kalan bir", top, "tagi kapatilmadi!"
                    s.push(top)

        index = index + 1

    if balanced and s.isEmpty():
        print "Dengeli!"
    elif balanced and not s.isEmpty():
        print s.pop(), "tagi acik kaldi.\nDengesiz!"
    else:
        print "Dengesiz!"

def matches(open, close):
    i = close.find("/")
    close = close[:i] + close[i+1:]
    return open == close


#HtmlChecker('index.html')
