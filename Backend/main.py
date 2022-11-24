import sys
import pandas as pd
import pickle
import sklearn
# print("Double = " + str(2*float(sys.argv[1])))

def predict_potability(ph,hard,sol,chlor,sul,cond,org,tri,tur):
    ph=pd.Series([ph])
    hard=pd.Series([hard])
    sol=pd.Series([sol])
    chlor=pd.Series([chlor])
    sul=pd.Series([sul])
    cond=pd.Series([cond])
    org=pd.Series([org])
    tri=pd.Series([tri])
    tur=pd.Series([tur])
    data=pd.DataFrame({'ph':ph,'Hardness':hard,'Solids':sol,'Chloramines':chlor,'Sulphate':sul,'Conductivity':cond,'Organic_carbon':org,'Trihalomethanes':tri,'Turbidity':tur})
    
    loaded = pickle.load(open("predictor.pkl", 'rb'))
    
    y_pred = loaded.predict(data)
    return y_pred

print(predict_potability(float(sys.argv[1]),
float(sys.argv[2]),
float(sys.argv[3]),
float(sys.argv[4]),
float(sys.argv[5]),
float(sys.argv[6]),
float(sys.argv[7]),
float(sys.argv[8]),
float(sys.argv[9]))[0])