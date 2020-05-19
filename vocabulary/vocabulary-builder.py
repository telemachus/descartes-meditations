import csv

lemma_to_defs = {}
lemma_to_entry = {}

with open('mydict.csv') as mydict:
    reader = csv.DictReader(mydict)
    for row in reader:
        lemma_to_defs[row['lemma']] = row['definition']
        lemma_to_entry[row['lemma']] = row['entry']

with open('shortdefs.csv') as shortdefs:
    reader = csv.DictReader(shortdefs)
    for row in reader:
        if row['lemma'] in lemma_to_defs:
            pass
        else:
            lemma_to_defs[row['lemma']] = row['definition']

words_file = open('words.txt', 'r')
wanted_words = words_file.read().splitlines()
words_file.close()

for wanted in wanted_words:
    if wanted in lemma_to_entry:
        entry = lemma_to_entry[wanted]
    else:
        entry = wanted

    if wanted in lemma_to_defs:
        definition = lemma_to_defs[wanted]
    else:
        definition = ''

    print('    \item[%s] %s' % (entry, definition))
