# Forecasting Home Prices on Long Island

This project will go over the (dreary) nature of the housing market on Long Island, and how it's changed throughout the years. We'll be grabbing data from various sources. Listed below are possible sources, which will be finalized as we obtain them:  

- Zillow: <https://www.zillow.com/research/data/>
  - Has a Postman API: <https://documenter.getpostman.com/view/9197254/UVsFz93V>
- Redfin: <https://www.redfin.com/news/data-center/>
- Census: <https://www.census.gov/construction/nrs/index.html>
  - Here's some historical data: <https://www.census.gov/construction/nrs/historical_data/index.html>
- Kaggle: <https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset>
- Google Datasets:
  - [Mortgage Prices](https://datasetsearch.research.google.com/search?src=0&query=mortgage%20prices&docid=L2cvMTFzaHY3M2diaw%3D%3D)
  - [Search Query for Interest Rates](https://datasetsearch.research.google.com/search?src=0&query=mortgage%20interest%20rates&docid=L2cvMTFweDI0NjBiOA%3D%3D)  

## Other option: Buyer Confidence in housing market vs ethnicity and income

I found a dataset within the Stony Brook Library: <https://guides.library.stonybrook.edu/az.php?t=26457>  
It's the [roper center public opinion archives](http://proxy.library.stonybrook.edu/login?url=https://ropercenter.cornell.edu/ipoll). I searched "Mortgage" and found a dataset that may be useful.

## Story

### Fernando

I spent the initial time looking for possible datasets where we can obtain information from. However, all datasets I've come across are on the national scale. I'm parsing through each one to extract out the Long Island Counties.

The following sources provided the best information:

- Redfin: I was able to obtain a summary of the housing market, but it can be combined with other sources to get more information.
- [Consumer Financial Protection Bureau](https://www.consumerfinance.gov/data-research/hmda/)
- [HMDA Dataset Browser](https://ffiec.cfpb.gov/data-browser/data/2022?category=counties&items=36103,36059)
- [FHFA](https://www.fhfa.gov/DataTools/Downloads)
- [Freddie Mac](https://www.freddiemac.com/research/datasets/sf_loanlevel_dataset.page)
- [Roper Center](http://proxy.library.stonybrook.edu/login?url=https://ropercenter.cornell.edu/ipoll)

#### Unavailable Data

Zillow's Postman API appears to have the most value to search quickly.  
It goes down to the neighborhood level, not property-level however.  

The data is not public, and required a commercial API Key.  
**Note: I was familiar with Zillow's ZTRAX database, but it was discontinued and all information on it was wiped out of public sources.**
