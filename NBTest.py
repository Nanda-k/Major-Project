import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle

class NB:

    def detecting(tweets):

        #train_news = pd.read_csv(train_file)
        #tfidf = TfidfVectorizer(stop_words='english',use_idf=True,smooth_idf=True) #TF-IDF
        print("Start Naive Bayes Classification")

        #knn_pipeline = Pipeline([('lrgTF_IDF', tfidf), ('lrg_mn', KNeighborsClassifier())])

        filename = 'svm_model.sav'
        #pickle.dump(knn_pipeline.fit(train_news['review'], train_news['sentiment']), open(filename, 'wb'))
        train = pickle.load(open(filename, 'rb'))
        predicted_class = train.predict(tweets)
        #print(type(test_news["review"])
        print("Naive Bayes Model Successfully Predicted")
        return predicted_class



if __name__ == "__main__":
    pass
    #NB.detecting('testset.csv')

