import sqlite3

class F1Store:

	@staticmethod
	def store(rf, nb, svm):
		conn = sqlite3.connect('sentiment.db')
		
		
		
		query = "delete from f1score"		
		conn.execute(query)
		conn.commit()
		query = "insert into f1score values("+str(rf)+","+str(nb)+","+str(svm)+")"		
		conn.execute(query)
		conn.commit()
		print ("Records created successfully");
		conn.close()

        




if __name__ == "__main__":
	F1Store.store(21,33,44)

