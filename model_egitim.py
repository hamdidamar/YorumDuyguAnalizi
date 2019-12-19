
#%%

#Kütüphanelerin eklenmesi
import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn.externals import joblib
#%%

#Veri setinin eklenip başlığının belirlenmesi
column = ['yorum']
df = pd.read_csv('data/yorumlar.csv', encoding ='utf8', sep='\t')
#%%


df_olumlu = df[df.Puan > 0.9]
df_olumsuz = df[df.Puan < 0.1]
df = pd.concat([df_olumlu, df_olumsuz], ignore_index = True)
df = shuffle(df)
#%%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df['Yorum'], df['Puan'], random_state = 0,test_size =0.1)
#%%

#CountVectorizer'ı başlatıyoruz ve eğitim verilerimize uyguluyoruz.
from sklearn.feature_extraction.text import CountVectorizer
max_features = 1000

vect = CountVectorizer(max_features= max_features,encoding ='utf8').fit(X_train)



feature_list = vect.get_feature_names()

joblib.dump(feature_list,'feature_list.pkl')
#%%

#X_train'deki belgeleri bir belge terim matrisine dönüştürürüz
X_train_vectorized = vect.transform(X_train) 
#%%
#Bu özellik matrisi X_ train_ vectorized'e dayanarak Lojistik Regresyon sınıflandırıcısını eğiteceğiz
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)
#%%
from sklearn.externals import joblib
joblib.dump(model, 'LogistigRegressionModel.pkl')
print("LogisticRegression dumped!")

model_columns = list(df.columns)
joblib.dump(model_columns, 'model_columns.pkl')
print("Models columns dumped!")

#
#%%
def analiz(yorum):
    
	prediction = LR.predict(vect.transform([yorum]))
			
	if(prediction == 0):
		return  False
	else:
		return  True


LR = joblib.load('LogistigRegressionModel.pkl')
#%%



