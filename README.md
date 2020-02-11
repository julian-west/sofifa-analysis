# Predicting football player values from FIFA statistics
**12th October 2019**

**View final analysis notebook in nbviewer <a href="https://nbviewer.jupyter.org/github/julian-west/sofifa-analysis/blob/master/predicting%20player%20value.ipynb" target="_blank">here</a>**

## Project Objective
**Can the value of a football player be predicted from their playing attributes and meta data?**  
**Which factors are most important for determining a player's market value?**  
**Which players are over or undervalued compared to the market?**  

In this notebook I will use a dataset of player attributes curated from the FIFA game's official website in order to answer the three questions above. While factors like player form and team results may have a short-term impact on the perceived value of a player, ultimately the value of a player should be linked to their fundamental skills and attributes - how good are their skills compared to others? 

Being able to predict the value of each player and understanding the main drivers of the predictions has two main benefits:

> 1. Football teams/scouts can identify whether a target player is currently over or undervalued and what price they should be willing to pay for a player of that quality (regardless of current form).
> 2. Understanding which factors most affect value could inform up and coming players which skills are most in demand in the market and which skills they should focus on improving to increase their value.

For this analysis I will carry out some basic exploratory data analysis to gain a high level insight into the features in the dataset, before preparing the data for modeling (data cleaning; train/test split; scaling etc..) and evaluate different regression models to predict the value of football players in the dataset.


### Methods Used
* Statistics
* Regression
* Exploratory Data Analysis
* Machine Learning
* Data Visualization
* Predictive Modeling
* SHAP values for model interpretation
* Webscraping

### Technologies 
* Python
* Jupyter
* Libraries: pandas, numpy, statsmodels, sklearn, matplotlib, seaborn, scipy, xgboost, shap, Scrapy
* Statistics: linear regression, multiple linear regression
* ML Models: decision tree, random forrest, xgboost


## Repository Contents

* **predicting player value.ipynb**  
	- notebook containing EDA, modeling and analysis  
* assets  
	- images saved for analysis  
* data
	- raw data from webscrape  
	- script to clean raw data  
	- processed data used for the analysis (data_clean.csv)  
* data_collection  
	- folder contains scrapy webcrawler to get raw data from website  


-------------------
