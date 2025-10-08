import re, csv

s = open('task3.txt', encoding='utf-8').read().split()

id = [st for st in s if re.fullmatch(r'\d+', st)]
fam = [st for st in s if re.fullmatch(r'[A-Z][a-zA-Z]+', st)]
emails = [st for st in s if re.fullmatch(r'\S+@\S+', st)]
date = [st for st in s if re.fullmatch(r'\d{4}-\d{2}-\d{2}', st)]
web = [st for st in s if re.fullmatch(r'https?://\S+|www\.\S+', st)]

rows = [[id[i], fam[i], emails[i], date[i], web[i]] for i in range(len(id))]

#savecsv
with open('task3_out.csv','w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['ID','Фамилия','Email','Дата','Сайт'])
    w.writerows(rows)

print('✅', len(rows))
