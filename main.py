import spacy

nlp = spacy.load("en_core_web_sm")
# print(nlp)

with open("data/us.txt", "r") as f:
    text = f.read()

print(text)

doc=nlp(text)
print(doc)

print(len(text))
print(len(doc))

# for token in text[0:10]:
#     print(token)

for token in doc[0:10]:
    print(token)

# for sent in doc.sents:
#     for w in sent:
#     print(type(w))

sentence1 = list(doc.sents)[0]
print(sentence1)

token2 = sentence1[2]
print(token2)

print(token2.left_edge)
print(token2.right_edge)
print(token2.ent_type_)
print(token2.ent_iob_)
print(token2.lemma_)
print(sentence1[12].lemma_)
print(token2.morph)
print(sentence1[12].morph)
print(token2.dep_)
print(token2.lang_)

from spacy import displacy
displacy.render(sentence1, style="dep")

text = 'Mike enjoys playing football'
doc2 = nlp(text)
print(doc2)

for token in doc2:
    print(token.text, token.pos_, token.dep_)

for ent in doc.ents:
    print (ent.text, ent.label_)

displacy.render(doc, style="ent")

# experiment=doc.sents.throw
# print(experiment)

# for w in doc.sents in range(1, 20):
#     print(w)

    