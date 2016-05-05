import numpy as np
def rp(phrase,change = ['"','?','!',',',':','.','/','*',"'",'(',')']):
	for c in change:
		phrase = phrase.replace(c,' ')
	return phrase

def cleaning(phrase):
	"""
		cleanning phrasal
	"""
	phrase = phrase.lower()

	return rp(phrase)
def vector(phrase):
	phrase = cleaning(phrase)
	return [word.strip() for word in phrase.split(' ') if word.strip()!='']
def hash(phrase,stopwords = [],n_grams=2):
	vect = vector(phrase)
	dvect = {}
	for v in vect:
		if v not in stopwords:
			if v not in dvect:
				dvect[v]=1
			else:
				dvect[v] += 1
	for i in xrange(len(vect)-n_grams-1):
		v_i = vect[i]
		if v_i not in stopwords:
			tmp= [v_i]
			for j in xrange(i+1,i+n_grams):
				if vect[j] not in stopwords:
					tmp.append(vect[j])
			if len(tmp) >1:
				gram = ' '.join([w for w in tmp])
				if gram not in dvect:
					dvect[gram] = 1
				else:
					dvect[gram] = 1
	return dvect
def df_(dvects):
	size_documents = len(dvects)
	df = {}
	for dv in dvects:
		for word in dv:
			if word not in df:
				df[word] = 1
			else:
				df[word] += 1
	return df,size_documents 
def tfidf_(dvects):
	df,size_docs = df_(dvects)
	tfidf = {}
	tf_tot = 0.0
	for dv in dvects:
		for word in dv:
			tf_tot += dv[word]
			if word not in tfidf:
				tfidf[word] = dv[word]
			else:
				tfidf[word] += dv[word]
	for word in tfidf:
		tfidf[word] = (tfidf[word]/tf_tot)*np.log(size_docs/df[word] )
	return tfidf

########### SCIKIT LEARN
def tfidf_sk(dvecttext):
	from sklearn.feature_extraction.text import TfidfVectorizer
	tfidf = TfidfVectorizer( encoding='utf-8', decode_error='replace', strip_accents=True, lowercase=True, preprocessor=None, tokenizer=None, analyzer='word', stop_words=None, token_pattern='(?u)\b\w\w+\b', ngram_range=(1, 2), max_df=1.0, min_df=1, max_features=None, vocabulary=None, binary=False,  use_idf=True, smooth_idf=True, sublinear_tf=False)
	return tfidf.fit(dvecttext),tfidf.get_feature_names()
