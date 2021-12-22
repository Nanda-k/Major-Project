import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle

class SVM:

    def detecting(test_file):

        #train_news = pd.read_csv(train_file)
        test_news = pd.read_csv(test_file)
        #tfidf = TfidfVectorizer(stop_words='english',use_idf=True,smooth_idf=True) #TF-IDF
        print("Start SVM Classification")

        #knn_pipeline = Pipeline([('lrgTF_IDF', tfidf), ('lrg_mn', KNeighborsClassifier())])

        filename = 'svm_model.sav'
        #pickle.dump(knn_pipeline.fit(train_news['review'], train_news['sentiment']), open(filename, 'wb'))
        train = pickle.load(open(filename, 'rb'))
        predicted_class = train.predict(test_news["review"])
        #print(predicted_class)
        print("SVM Model Successfully Predicted")
        return predicted_class

    def model_assessment(y_test, predicted_class):
        print('accuracy')
        # Accuracy = (TP + TN) / ALL
        accuracy = accuracy_score(y_test, predicted_class)
        
        return accuracy


if __name__ == "__main__":
    SVM.detecting('testset.csv')

