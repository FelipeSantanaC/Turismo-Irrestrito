import joblib
filename = "recommendations\kmeans.joblib"
loaded_model = joblib.load(filename)


def PredictCluster(userData):
    return loaded_model.predict(userData)