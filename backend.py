import censusdis.data as ced
from censusdis.datasets import ACS1, ACS5
import pandas as pd

ACS1_START_YEAR = 2005
ACS1_END_YEAR   = 2022
ACS1_SKIP_YEARS = [2020]

years = [year 
         for year in range(ACS1_START_YEAR, ACS1_END_YEAR + 1) 
         if year not in ACS1_SKIP_YEARS]

def get_labels_for_variable(var_name, acs):
    df_final = None

    for year in years: 
        try:
            if acs == 1:
                label = ced.variables.get(ACS1, year, var_name)['label']
            else:
                label = ced.variables.get(ACS5, year, var_name)['label']
        except Exception as e: # e.g. 404 - variable does not exist
            label = pd.NA

        df_new = pd.DataFrame({'Year': year,
                            'Name': var_name,
                            'Label': label}, index=[None])
 
        if df_final is None:
            df_final = df_new.copy()
        else:    
            df_final = pd.concat([df_final, df_new])

    return df_final