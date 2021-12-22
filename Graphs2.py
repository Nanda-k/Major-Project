import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import sys
import sqlite3

def f1view():
    

    conn = sqlite3.connect('sentiment.db')
    print(conn)
    cursor = conn.execute("SELECT * from f1score")
    for row in cursor:
        rlist=row

    height=rlist
    bars = ('RandomForest', 'Naive Bayes', 'SVM', )
    y_pos = np.arange(len(bars))
    plt.bar(bars, height, color=['orange', 'pink', 'purple'])
    plt.xlabel('Algorithms')
    plt.ylabel('F1-Score ')
    plt.title('F1-Score Measure')
    plt.show()

if __name__ == "__main__":
    f1view()



