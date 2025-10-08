import re




#task1

# text='ададд и лаба и дадад и сс'
import re

text = open('task1-ru.txt', encoding='utf-8').read()

print(re.findall(r'\bс[а-яё]+', text, flags=re.I))
print(re.findall(r'\bи\s+([а-яё]+)', text, flags=re.I))

#task2

html = open('task2.html', encoding='utf-8').read()
print( re.findall(r'font-family(.*)', html, flags=re.I))
