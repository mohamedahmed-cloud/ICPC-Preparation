# Problem Link : https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true
# Problem Name : XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    count=0
    for i in node:
        count+=get_attr_number(i)
    return count+len(node.attrib)

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))