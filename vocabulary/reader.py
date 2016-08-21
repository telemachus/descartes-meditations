from cltk.stem.lemma import LemmaReplacer
from cltk.stem.latin.j_v import JVReplacer
from cltk.tokenize.word import WordTokenizer

meditatio_prima = open("../meditatio-prima.txt", "r").read()
meditatio_secunda = open("../meditatio-secunda.txt", "r").read()

jv = JVReplacer()
meditatio_prima = jv.replace(meditatio_prima)
meditation_secunda = jv.replace(meditatio_secunda)

t = WordTokenizer("latin")
l = LemmaReplacer("latin")

words = l.lemmatize(t.tokenize(meditatio_prima))
words += l.lemmatize(t.tokenize(meditatio_secunda))
words = sorted(list(set(words)))
print("\n".join(words))
