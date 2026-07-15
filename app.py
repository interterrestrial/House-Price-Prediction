import joblib
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import json

# Load Model & Columns
try:
    model = joblib.load("models/tuned_gradient_boosting.pkl")
    with open("models/training_columns.json", "r") as f:
        training_columns = json.load(f)
except Exception as e:
    print(f"Error loading model artifacts: {e}")

DEFAULT_HOUSE = {
    "MSSubClass": 20,
    "MSZoning": "RL",
    "LotFrontage": 70,
    "LotArea": 10000,
    "Street": "Pave",
    "Alley": "None",
    "LotShape": "Reg",
    "LandContour": "Lvl",
    "Utilities": "AllPub",
    "LotConfig": "Inside",
    "LandSlope": "Gtl",
    "Neighborhood": "NAmes",
    "Condition1": "Norm",
    "Condition2": "Norm",
    "BldgType": "1Fam",
    "HouseStyle": "1Story",
    "OverallQual": 6,
    "OverallCond": 5,
    "YearBuilt": 1970,
    "YearRemodAdd": 1990,
    "RoofStyle": "Gable",
    "RoofMatl": "CompShg",
    "Exterior1st": "VinylSd",
    "Exterior2nd": "VinylSd",
    "MasVnrType": "None",
    "MasVnrArea": 0,
    "ExterQual": "TA",
    "ExterCond": "TA",
    "Foundation": "PConc",
    "BsmtQual": "TA",
    "BsmtCond": "TA",
    "BsmtExposure": "No",
    "BsmtFinType1": "Unf",
    "BsmtFinSF1": 0,
    "BsmtFinType2": "Unf",
    "BsmtFinSF2": 0,
    "BsmtUnfSF": 500,
    "TotalBsmtSF": 1000,
    "Heating": "GasA",
    "HeatingQC": "Ex",
    "CentralAir": "Y",
    "Electrical": "SBrkr",
    "1stFlrSF": 1200,
    "2ndFlrSF": 0,
    "GrLivArea": 1200,
    "BsmtFullBath": 0,
    "BsmtHalfBath": 0,
    "FullBath": 2,
    "HalfBath": 0,
    "BedroomAbvGr": 3,
    "KitchenAbvGr": 1,
    "KitchenQual": "TA",
    "TotRmsAbvGrd": 6,
    "Fireplaces": 0,
    "FireplaceQu": "None",
    "GarageType": "Attchd",
    "GarageYrBlt": 1980,
    "GarageFinish": "Unf",
    "GarageCars": 2,
    "GarageArea": 500,
    "GarageQual": "TA",
    "GarageCond": "TA",
    "PavedDrive": "Y",
    "WoodDeckSF": 0,
    "OpenPorchSF": 0,
    "EnclosedPorch": 0,
    "3SsnPorch": 0,
    "ScreenPorch": 0,
    "PoolArea": 0,
    "PoolQC": "None",
    "Fence": "None",
    "MiscFeature": "None",
    "MiscVal": 0,
    "MoSold": 6,
    "YrSold": 2010,
    "SaleType": "WD",
    "SaleCondition": "Normal"
}

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        
        # Merge input data with default house
        house = DEFAULT_HOUSE.copy()
        for key in data:
            if key in house:
                house[key] = data[key]
        
        # Feature Engineering (as in 09_Inference.ipynb)
        house["HouseAge"] = house["YrSold"] - house["YearBuilt"]
        house["RemodelAge"] = house["YrSold"] - house["YearRemodAdd"]
        house["IsRemodeled"] = int(house["YearBuilt"] != house["YearRemodAdd"])
        
        house["TotalSF"] = house["TotalBsmtSF"] + house["1stFlrSF"] + house["2ndFlrSF"]
        
        house["TotalPorchSF"] = (
            house["OpenPorchSF"] + house["EnclosedPorch"] +
            house["3SsnPorch"] + house["ScreenPorch"]
        )
        house["OutdoorArea"] = house["WoodDeckSF"] + house["TotalPorchSF"]
        house["TotalBathrooms"] = house["FullBath"] + 0.5 * house["HalfBath"]
        
        house["HasGarage"] = int(house["GarageArea"] > 0)
        house["HasBasement"] = int(house["TotalBsmtSF"] > 0)
        house["HasPool"] = int(house["PoolArea"] > 0)
        house["HasFireplace"] = int(house["Fireplaces"] > 0)
        house["HasSecondFloor"] = int(house["2ndFlrSF"] > 0)
        
        house_df = pd.DataFrame([house])
        
        # Encode categorical variables
        house_df = pd.get_dummies(house_df, drop_first=True)
        
        # Align with training columns
        house_df = house_df.reindex(columns=training_columns, fill_value=0)
        
        # Predict
        prediction = model.predict(house_df)[0]
        
        return jsonify({"success": True, "predicted_price": float(prediction)})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
