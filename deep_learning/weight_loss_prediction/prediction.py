import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import StandardScaler

loaded_model = tf.keras.models.load_model("weight_loss_ann.h5")

dataset = pd.read_csv('weight_loss_data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:,4] = le.fit_transform(X[:,4])

#Feature Scaling
sc = StandardScaler()
X = sc.fit_transform(X)

#print(ann.predict(sc.transform([[몸무게, 주당 운동시간, 1일 섭취 칼로리, 나이, 성별(여자=0,남자=1), 체지방량]])))
print(loaded_model.predict(sc.transform([[52, 6, 1800, 24, 1, 27.0]])))