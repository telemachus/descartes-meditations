import csv

def isdcc(dcc):
    '''Return margin note or empty string depending on DCC status'''
    if dcc == 'true':
        return '\marginnote{*}'
    else:
        return ''

with open('latin-vocabulary.csv') as descartes:
    reader = csv.DictReader(descartes)
    for row in reader:
        note = isdcc(row['dcc'])
        print('\item[%s] %s%s' % (row['entry'], note, row['definition']))
