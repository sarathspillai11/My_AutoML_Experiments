# -*- coding: utf-8 -*-
"""PyCaret for Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jZrgH5DlgiClXygoOC4ZTSwL3XE5gfHc

# Installation
"""

!pip install pycaret

"""## We will try out a classic example of Regression i.e the Kaggle House Price Prediction Challenge"""

from pycaret.regression import * 
import pandas as pd

"""### Adding data files to Colab"""

from google.colab import files
uploaded = files.upload()

import io
test = pd.read_csv(io.BytesIO(uploaded['test.csv']))
train = pd.read_csv(io.BytesIO(uploaded['train.csv']))
sample = pd.read_csv(io.BytesIO(uploaded['sample_submission.csv']))

train.shape

test.shape

train.head()

train.info()

#list of columns that are categorical
cat_f = ['MSZoning','Exterior1st','Exterior2nd','KitchenQual','Functional','SaleType',
                                     'Street','LotShape','LandContour','LotConfig','LandSlope','Neighborhood',   
                                     'Condition1','Condition2','BldgType','HouseStyle','RoofStyle','RoofMatl',    
                                     'MasVnrType','ExterQual','ExterCond','Foundation','BsmtQual','BsmtCond',   
                                     'BsmtExposure','BsmtFinType1','BsmtFinType2','Heating','HeatingQC','CentralAir',   
                                     'Electrical','GarageType','GarageFinish','GarageQual','GarageCond','PavedDrive',
                                     'SaleCondition']

"""# Setting up Transformation pipeline in PyCaret

The setup() method must be called before any other function in PyCaret. When this function is executed, PyCarets inference algorithm automatically determines the data types of all features. The results of this step are also displayed to the user, wherein he can configure them correctly if some features are wrongly identified to a different data type. 
"""

exp_reg101 = setup(data = train, target = 'SalePrice', categorical_features = cat_f,
                   ignore_features= ['Alley','PoolQC','MiscFeature','Fence','FireplaceQu','Utilities'],
                   normalize = True,session_id = 123)

"""# Compare all regression Models"""

# all the models that are available are 
models()

"""# Train all the models and select the best one according to the R2 score:"""

best = compare_models(exclude = ['ransac'])

"""**Selecting the model with the best R2 score. Gradient Boosting in this case**"""

gbr = create_model('gbr')

tuned_gbr = tune_model(gbr)

tuned_gbr

"""# Visualisation of Predictions"""

plot_model(tuned_gbr)

plot_model(tuned_gbr, plot = 'error')

"""## Feature Importance Plot"""

plot_model(tuned_gbr, plot = 'feature')

"""### Interactive dashboard visualization to plot the graph of user's choice"""

evaluate_model(tuned_gbr)

"""# Validation of predictions on Test Data"""

predict_model(tuned_gbr)

"""# Finalize the model for deployment"""

final_gbr = finalize_model(tuned_gbr)
final_gbr

predict_model(final_gbr)

"""# Final Prediction on real data. Unseen data in this case"""

final_predictions = predict_model(final_gbr, data=test)
final_predictions.head()

"""# Saving the model"""

save_model(final_gbr,'HousePricePrediction_PyCaret_GBR')