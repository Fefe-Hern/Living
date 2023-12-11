# Function to plot:
import seaborn as sns
import pandas as pd
from datetime import datetime

current_period = datetime.now().year
property_types = ["property_type_All Residential","property_type_Condo/Co-op","property_type_Multi-Family (2-4 Unit)","property_type_Single Family Residential","property_type_Townhouse"]

def plotRedfinScatter(xVal, yVal, dataset):
    plot = sns.scatterplot(x=xVal, y=yVal, data=dataset,
                alpha=getYearAlpha(dataset['period_begin']),
                hue=dataset[property_types].apply(getHue, axis=1))
    plot.set(xlim=(200000, 800000), ylim=(200000, 900000))
    return plot

def getYearAlpha(data):
    dates = pd.to_datetime(data)
    dates = data.map(datetime.fromordinal).astype("string")
    period = dates.str[:4].astype(int)
    return 1 - (current_period - period) / (current_period - period.min())

def getHue(tuple):
    #print(max(tuple, key=lambda x: x))
    for key, value in tuple.items():
        if value == 1.0:
            return key.removeprefix("property_type_")