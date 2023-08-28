import joblib
import numpy as np
filename = "recommendations\kmeans.joblib"
loaded_model = joblib.load(filename)


def PredictCluster(userData):
    userData = userData / np.linalg.norm(userData)
    return loaded_model.predict(userData)