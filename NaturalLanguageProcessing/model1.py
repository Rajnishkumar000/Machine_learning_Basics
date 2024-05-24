import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('Restaurant_Reviews.tsv',delimiter='\t',quoting=3)

#CLEANING TEXT

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords                 #These are words like the to of
from nltk.stem.porter import PorterStemmer       # It takes the roots of the word like loved will be consiodered as love
                                                 #It also reduces the dimension of sparse matrix

corpus=[]
for i in range(0,1000):
    review=re.sub('[^a-zA-Z]',' ',dataset['Review'][i])
    review=review.lower()
    review=review.split()
    ps=PorterStemmer()
    all_stopwords=stopwords.words('english')
    all_stopwords.remove('not')
    review=[ps.stem(word) for word in review if not word in set(all_stopwords)]
    review=' '.join(review)
    corpus.append(review)
print(corpus)


#CREATING BAG OF WORDS
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=1500)
x=cv.fit_transform(corpus).toarray()
y=dataset.iloc[:,-1].values
print(x)
print(len(x[0]))


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)
print(X_train)

# Training the Logistic Regression model on the Training set
from sklearn.naive_bayes import GaussianNB
classifier =GaussianNB()
classifier.fit(X_train, y_train)

# predicting the test set result
y_pred=classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))


#accuracy check

from sklearn.metrics import accuracy_score,confusion_matrix
cm=confusion_matrix(y_test,y_pred)
accuracy=accuracy_score(y_test,y_pred)
print(cm)
print(accuracy)
