import pandas as pd
import numpy as np
from pathlib import Path

csv_file_path = Path(__file__).parent / "depression_anxiety_data.csv"
mental_health_dataset = pd.read_csv(csv_file_path)

# Showing basic info
print(mental_health_dataset.info(verbose=True))
print("-" * 40)
print(mental_health_dataset.describe(include="all"))
print("-" * 40)

# Number of men and woman with a diagnosis of depression
diagnosis_depression_men = 0
diagnosis_depression_woman = 0
for index, info in mental_health_dataset.iterrows():
    if (info["gender"] == "male") and (info["depression_diagnosis"] == True):
        diagnosis_depression_men +=1
    if (info["gender"] == "female") and (info["depression_diagnosis"] == True):
        diagnosis_depression_woman +=1

print("Number of men with a diagnosis of depression: ", diagnosis_depression_men)
print("Number of woman with a diagnosis of depression: ", diagnosis_depression_woman)
print("-" * 40)

# Average age between woman and men
print(mental_health_dataset[["age", "gender"]].groupby("gender", group_keys=False).mean())

print("-" * 40)
# People with severe depression having treatment
print(mental_health_dataset.loc[(mental_health_dataset["age"] < 20) & (mental_health_dataset["depression_severity"] == "Severe") & (mental_health_dataset["depression_treatment"] == True)])
print("-" * 40)
# People with severe anxiety having treatment
print(mental_health_dataset.loc[(mental_health_dataset["age"] < 20) & (mental_health_dataset["anxiety_severity"] == "Severe") & (mental_health_dataset["anxiety_treatment"] == True)])
print("-" * 40)
# People with severe depression and anxiety below 20 years
print(mental_health_dataset.loc[(mental_health_dataset["age"] < 20) & (mental_health_dataset["depression_severity"] == "Severe") & (mental_health_dataset["anxiety_severity"] == "Severe")])


"""
Showing the number of suicidal between woman and men using a dict to be the main data structure,
set was used to not repeat the age number since the idea is see the range and not repeat values
"""
suic_analisys = {}
woman_age_set = set()
man_age_set = set()
n_woman = 0
n_man = 0
for ind, info in mental_health_dataset.iterrows():
    if info["suicidal"] == True:
        if info["gender"] == "female":
            woman_age_set.add(info["age"])
            suic_analisys[info["gender"]] = {"Age's between": woman_age_set}
            n_woman += 1
            suic_analisys["Number of suicidal woman"] = n_woman
        else:
            man_age_set.add(info["age"])
            suic_analisys[info["gender"]] = {"Age's between": man_age_set}
            n_man += 1
            suic_analisys["Number of suicidal man"] = n_man
            
print(suic_analisys)