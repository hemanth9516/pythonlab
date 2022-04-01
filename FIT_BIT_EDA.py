#Import Essential Libraries

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import calendar
# READ FIT BIT HEALTH CARE DATA and print head

fit_bit_df=pd.read_csv("D:\Study\iNeuron-DS\EDA\FitBit\FitBit\FitBitdata.csv")
fit_bit_df.head()
Id	ActivityDate	TotalSteps	TotalDistance	TrackerDistance	LoggedActivitiesDistance	VeryActiveDistance	ModeratelyActiveDistance	LightActiveDistance	SedentaryActiveDistance	VeryActiveMinutes	FairlyActiveMinutes	LightlyActiveMinutes	SedentaryMinutes	Calories
0	1503960366	3/25/2016	11004	7.11	7.11	0.0	2.57	0.46	4.07	0.0	33	12	205	804	1819
1	1503960366	3/26/2016	17609	11.55	11.55	0.0	6.92	0.73	3.91	0.0	89	17	274	588	2154
2	1503960366	3/27/2016	12736	8.53	8.53	0.0	4.66	0.16	3.71	0.0	56	5	268	605	1944
3	1503960366	3/28/2016	13231	8.93	8.93	0.0	3.19	0.79	4.95	0.0	39	20	224	1080	1932
4	1503960366	3/29/2016	12041	7.85	7.85	0.0	2.16	1.09	4.61	0.0	28	28	243	763	1886
#describe dataset to calculate different Metrics for Central Tendency Measurement
fit_bit_df.describe()
#We can see that this dataset don't have any missing values so we are dont have to treat any missing value
fit_bit_df.isna().sum()
Id                          0
ActivityDate                0
TotalSteps                  0
TotalDistance               0
TrackerDistance             0
LoggedActivitiesDistance    0
VeryActiveDistance          0
ModeratelyActiveDistance    0
LightActiveDistance         0
SedentaryActiveDistance     0
VeryActiveMinutes           0
FairlyActiveMinutes         0
LightlyActiveMinutes        0
SedentaryMinutes            0
Calories                    0
year                        0
month                       0
date                        0
day                         0
dtype: int64
fit_bit_df.isnull().sum()
Id                          0
ActivityDate                0
TotalSteps                  0
TotalDistance               0
TrackerDistance             0
LoggedActivitiesDistance    0
VeryActiveDistance          0
ModeratelyActiveDistance    0
LightActiveDistance         0
SedentaryActiveDistance     0
VeryActiveMinutes           0
FairlyActiveMinutes         0
LightlyActiveMinutes        0
SedentaryMinutes            0
Calories                    0
year                        0
month                       0
date                        0
day                         0
dtype: int64
#Add Year/Month/Week for Narrowing for Analysis Scope w.r.t Date

fit_bit_df['year'] = pd.DatetimeIndex(fit_bit_df['ActivityDate']).strftime('%Y')
fit_bit_df['month'] =  pd.DatetimeIndex(fit_bit_df['ActivityDate']).strftime('%b') 
fit_bit_df['day'] = pd.DatetimeIndex(fit_bit_df['ActivityDate']).strftime('%a')
fit_bit_df.head()
Id	ActivityDate	TotalSteps	TotalDistance	TrackerDistance	LoggedActivitiesDistance	VeryActiveDistance	ModeratelyActiveDistance	LightActiveDistance	SedentaryActiveDistance	VeryActiveMinutes	FairlyActiveMinutes	LightlyActiveMinutes	SedentaryMinutes	Calories	year	month	date	day
0	1503960366	3/25/2016	11004	7.11	7.11	0.0	2.57	0.46	4.07	0.0	33	12	205	804	1819	2016	Mar	Fri	Fri
1	1503960366	3/26/2016	17609	11.55	11.55	0.0	6.92	0.73	3.91	0.0	89	17	274	588	2154	2016	Mar	Sat	Sat
2	1503960366	3/27/2016	12736	8.53	8.53	0.0	4.66	0.16	3.71	0.0	56	5	268	605	1944	2016	Mar	Sun	Sun
3	1503960366	3/28/2016	13231	8.93	8.93	0.0	3.19	0.79	4.95	0.0	39	20	224	1080	1932	2016	Mar	Mon	Mon
4	1503960366	3/29/2016	12041	7.85	7.85	0.0	2.16	1.09	4.61	0.0	28	28	243	763	1886	2016	Mar	Tue	Tue
#We will plot scatter plot to see the relationship between Calories with other variables
plt.scatter(fit_bit_df['VeryActiveDistance'],fit_bit_df['Calories'])
plt.xlabel("VeryActiveDistance --->")
plt.ylabel("Calories --->")
plt.title("Calories Vs VeryActiveDistance")
plt.show()

plt.scatter(fit_bit_df['ModeratelyActiveDistance'],fit_bit_df['Calories'])
plt.xlabel("ModeratelyActiveDistance --->")
plt.ylabel("Calories --->")
plt.title("Calories Vs ModeratelyActiveDistance")
plt.show()

plt.scatter(fit_bit_df['LightActiveDistance'],fit_bit_df['Calories'])
plt.xlabel("LightActiveDistance --->")
plt.ylabel("Calories --->")
plt.title("Calories Vs LightActiveDistance")
plt.show()

plt.scatter(fit_bit_df['SedentaryActiveDistance'],fit_bit_df['Calories'])
plt.xlabel("SedentaryActiveDistance --->")
plt.ylabel("Calories --->")
plt.title("Calories Vs SedentaryActiveDistance")
plt.show()

plt.scatter(fit_bit_df['VeryActiveMinutes'],fit_bit_df['Calories'])
plt.xlabel("VeryActiveMinutes --->")
plt.ylabel("Calories --->")
plt.title("Calories Vs VeryActiveMinutes")
plt.show()

plt.scatter(fit_bit_df['FairlyActiveMinutes'],fit_bit_df['Calories'])
plt.xlabel("FairlyActiveMinutes --->")
plt.ylabel("Calories --->")
plt.title("Calories Vs FairlyActiveMinutes")
plt.show()

plt.scatter(fit_bit_df['LightlyActiveMinutes'],fit_bit_df['Calories'])
plt.xlabel("LightlyActiveMinutes --->")
plt.ylabel("Calories --->")
plt.title("Calories Vs LightlyActiveMinutes")
plt.show()

plt.scatter(fit_bit_df['SedentaryMinutes'],fit_bit_df['Calories'])
plt.xlabel("SedentaryMinutes --->")
plt.ylabel("Calories --->")
plt.show()

#Ploting Bar Plot between Year/Month/Day vs Calories to Analysis how the Calories varies with these variables


fig = plt.figure(figsize = (10, 5)) 
plt.bar(fit_bit_df['month'],fit_bit_df.Calories)
plt.xlabel("Month")
plt.ylabel("Calories --->")
plt.title("Calories Vs Month")
plt.show()

#Ploting Bar Plot between Day vs Calories to Analysis how the Calories varies with these variables

fig = plt.figure(figsize = (10, 5)) 
plt.bar(fit_bit_df['day'],fit_bit_df.Calories)
plt.xlabel("Day")
plt.ylabel("Calories --->")
plt.title("Calories Vs Day")
plt.show()

#We will plot different activities based on mitues vs Calories 
col_select = ['Calories','VeryActiveMinutes','FairlyActiveMinutes','LightlyActiveMinutes','SedentaryMinutes']
wide_df = fit_bit_df[col_select]

# figure size
plt.figure(figsize=(15,8))

# timeseries plot using lineplot
ax = sns.lineplot(data=wide_df)

ax.set_title('Value of calories and Different Activities Based On Activity Minutes')
Text(0.5, 1.0, 'Value of calories and Different Activities Based On Activity Minutes')

 		
