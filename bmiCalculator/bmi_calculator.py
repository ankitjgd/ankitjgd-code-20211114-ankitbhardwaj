'''
    This module open up "data.json" file in same directory, 
    reads data from it and 
    print the number of overweight people it finds in data.
'''

import json
import pandas as pd
import numpy as np

MIN_HEIGHT_CM = 63
MAX_HEIGHT_CM = 270
MIN_WEIGHT_KG = 25
MAX_WEIGHT_KG = 250

class calculator:
    def __init__(self,file):
        self.data_file = file
    
    def get_overweight_number(self):
        try:
            with open(self.data_file) as d:
                data = json.load(d) 

            df = pd.DataFrame(data)

            #dropping off the rows with wrong data
            df.dropna(inplace=True)
            index_names = df[ (df['HeightCm'] < MIN_HEIGHT_CM) | (df['HeightCm'] > MAX_HEIGHT_CM)].index
            df.drop(index_names, inplace = True)
            index_names = df[ (df['WeightKg'] < MIN_WEIGHT_KG) | (df['WeightKg'] > MAX_WEIGHT_KG)].index
            df.drop(index_names, inplace = True)

            #applying formula
            df['BMI (kg/m2)'] = df['WeightKg'] / ((df['HeightCm']/100)**2)

            #picking up conditions from provided table
            conditions = [
                (df['BMI (kg/m2)'] <= 18.4),
                (df['BMI (kg/m2)'] > 18.5) & (df['BMI (kg/m2)'] <= 24.9),
                (df['BMI (kg/m2)'] > 25) & (df['BMI (kg/m2)'] <= 29.9),
                (df['BMI (kg/m2)'] > 30) & (df['BMI (kg/m2)'] <= 34.9),
                (df['BMI (kg/m2)'] > 35) & (df['BMI (kg/m2)'] <= 39.9),
                (df['BMI (kg/m2)'] >= 40)
            ]

            categories_values = ['Underweight', 'Normal weight', 'Overweight', 'Moderately obese','Severely obese','Very severely obese']
            risk_values = ['Malnutrition risk', 'Low risk', 'Enhanced risk', 'Medium risk','High risk','Very high risk']

            df['Health risk'] = np.select(conditions, risk_values)
            df['BMI Category'] = np.select(conditions, categories_values)

            return df['BMI Category'].value_counts().Overweight

        except Exception as e:
            return e