import csv

def isdcc(dcc):
    '''Return margin note or empty string depending on DCC status'''
    if dcc == 'true':
        return '\marginnote{*}'
    else:
        return ''

def cleanup(lemma):
    '''Clean up first part of entry to become lemma'''

    # Trim space on either side.
    lemma = lemma.strip()
    # Remove macrons.
    lemma = lemma.translate(str.maketrans("āēīōūȳ", "aeiouy"))
    lemma = lemma.translate(str.maketrans("ĀĒĪŌŪȲ", "AEIOUY"))
    # Remove everything except what precedes first internal comma.
    lemma = lemma.split(',', maxsplit=1)[0]
    # Remove everything except what preceded first internal space.
    lemma = lemma.split(' ', maxsplit=1)[0]

    return lemma

print("lemma,entry,definition,dcc")

with open('latin-vocabulary.csv') as descartes:
    reader = csv.DictReader(descartes)
    for row in reader:
        lemma = cleanup(row['entry'])
        print('"%s","%s","%s","%s"' %
                (lemma, row['entry'],row['definition'], row['dcc']))
