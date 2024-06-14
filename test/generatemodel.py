import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Charger les données du fichier CSV
data = pd.read_csv('donnees_medicales.csv')

# Diviser les données en fonction de la maladie et du traitement
X = data['Disease']
y = data['Treatment']

# Vectorisation des maladies (nous utilisons CountVectorizer ici)
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Entraînement du modèle de classification (Naive Bayes dans cet exemple)
model = MultinomialNB()
model.fit(X_vec, y)

# Sauvegarde du modèle entraîné
joblib.dump(model, 'Treatment_predict.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Modèle entraîné et vectorizer sauvegardés.")
