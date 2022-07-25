import re

s = '''
// I am a single comment and you must remove me :((
/*
I am a block comment and you must remove me
*/

#include<iostream>
using namespace std;

int main() {

int a, b;
cin » a » b; // Reading two variables from user (please remove me!! :frowning: )
cout « a + b « endl;

// End of the program (remove me please :))
return 0;
              lol
}
'''

# s = input()

p1 = r"(?://(?<=//).+)|(?:/\*[\s\S][^\*/]*[\*][/]*)" ## comments
p2 = r"(?:[\n]+)|(?:[\n]([ ]+))" ## excess new lines
p3 =  r"^(\n)|[\n]([ \t]+)" #white spaces and tabs


l = re.findall(p1, s)
# b = re.findall(p2, s)
c = re.sub(p1, "", s)
c = re.sub(p2, "\n", c)
c = re.sub(p3, "", c)
# l = re.findall(p3, c)
# print(f"{l}\n{c}")
print(c.strip())