import re

txt = "the rain in Spain"

x = re.findall("^the", txt) # get patterns

print(x)

y = re.search("^the", txt)

print(y.start())