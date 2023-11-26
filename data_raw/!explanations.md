# Data Explanations

## cfpb_loan_level_li  

Details on the loan-level data from the Consumer Financial Protection Bureau (CFPB)  
Known as LAR, and has numbers as values which specify things like the type and purchase of loan.  
<https://ffiec.cfpb.gov/documentation/publications/modified-lar/modified-lar-schema>  

## LI_Home_Census_Data_2020

Year-Over-Year Census Data involving Mortgage households, income of renters, etc. Until 2020.

## Redfin_Market_Tracker_Li

Reviews different house types, their median sale prices, number of homes sold / pending, amount of new listings & inventory, as well as cases like sold over list price or time to sell.  
Downloaded from <https://www.redfin.com/news/data-center/> and filtered for Long Island.  
Header Information at: <https://www.redfin.com/news/data-center-metrics-definitions/>  

## Roper_FM_Home_Sentiment_Index_2022

<https://ropercenter-cornell-edu.proxy.library.stonybrook.edu/ipoll/study/31119780>
Compiled List of Questions from Fannie Mae, usually done monthly.  
The columns related to each question is found in the link above, with a quick review of each average answer.

## Freddie Mac Single Family Loan-Level Datasets

I obtained access at <https://www.freddiemac.com/research/datasets/sf-loanlevel-dataset> to get large datasets of loans which went thru Freddie Mac. I added a sample output to send.  
The data contains things like Credit Score, Year/Month of First Payment, PMI if any, Interest Rate, and Postal Codes. Pipe-Deliminated with no header (But attaching one can be easy)  
I attached a PDF that contains the Data Dictionary, explaining which columns are which. The following may be of use:

- Col 1: Credit Score
- Col 2: First Payment Date (YYYYMM)
- Col 6: PMI (Private Mortgage Insurance), usually if down payment is less than 20%
- Col 8: Occupancy Status (Primary, Secondary, Investment)
- Col 10: Debt to Income Ratio
- Col 11: Original UPB (Unpaid Principal Balance) AKA Home Price minus down payment
- Col 13: Interest Rate (We can get the average rate over the year)
- Col 19: Postal Code
- Col 21: Loan Purpose (Purchase, Refinance, Cash-Out Refinance) We're interested in Purchases

We're interested in the following postal codes as they relate to Long Island based ones:

- 11000
- 11500
- 11700
- 11800
- 11900
