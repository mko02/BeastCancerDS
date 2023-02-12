import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import scipy.stats as stats
import distribution as dist

medical_doctors_access_df = pd.read_excel('access.xlsx') 
medical_doctors_access_df.head()

mini_medical_doctors_access_df = medical_doctors_access_df[["Unnamed: 0","Density of medical doctorsw (per 10 000 population) "]]
mini_medical_doctors_access_df = mini_medical_doctors_access_df[mini_medical_doctors_access_df['Density of medical doctorsw (per 10 000 population) '].notna()]
mini_medical_doctors_access_df.head()

medical_access_col = "Density of medical doctorsw (per 10 000 population) "
medical_access_mean, medical_access_std = dist.dist_info(medical_doctors_access_df, medical_access_col)
dist.dist_plot(medical_doctors_access_df, medical_access_col, medical_access_mean, medical_access_std, 0.2, 84)
mini_medical_doctors_access_df = dist.add_norm(mini_medical_doctors_access_df, medical_access_col, "Med Access Scaled")
mini_medical_doctors_access_df.head()

life_exp_df = pd.read_excel('WHO22LifeExpectancy&InfantMortality.xlsx') 
life_exp_df.head()

infant_death_col = "Under-five mortality ratee (per 1000 live births)"
infant_death_mean, infant_death_std = dist.dist_info(life_exp_df, infant_death_col)
life_exp_df = life_exp_df[life_exp_df[infant_death_col] < 180]
dist.dist_plot(life_exp_df, infant_death_col, infant_death_mean, infant_death_std, 2, 115)
life_exp_df = dist.add_norm(life_exp_df, infant_death_col, "Infant Death Scaled")
life_exp_df.head()


life_exp_col = "Life Expectancy for Both Sexes"
life_exp_mean, life_exp_std = dist.dist_info(life_exp_df, life_exp_col)
# life_exp_df = life_exp_df[life_exp_df[infant_death_col] < 180]
dist.dist_plot(life_exp_df, life_exp_col, life_exp_mean, life_exp_std, 2, 115)
life_exp_df = dist.add_norm(life_exp_df, life_exp_col, "Life Exp Scaled")
life_exp_df.head()

