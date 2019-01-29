import re
matcher=re.finditer('\w','a7b@ k9z')
count=0
for m in matcher:
    count+=1
    print('match is at:(),End:(),patternfound(),m.group()'\
          .format(m.start(), m.end(), m.group()))
print('Total count: ',count)
