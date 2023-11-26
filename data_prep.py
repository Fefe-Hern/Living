from csv_query_filter import filter_data


# Redfin dataset
redfin_data = filter_data('f:/Programming/homeli/county_market_tracker.tsv000',
                 'data/redfin_market_tracker_LI.csv',
                 'region == "Suffolk County, NY" | region == "Nassau County, NY"',
                 sep='\t',
                 test_run=False)

# CFPB dataset
SUFFOLK_COUNTY_CODE = '36103'
NASSAU_COUNTY_CODE = '36059'
cfpb_data = filter_data('f:/Programming/homeli/2022_public_loan_level_dataset.csv',
                        'data/2022_cfpb_loan_level_LI.csv',
                 'county_code == ' + SUFFOLK_COUNTY_CODE + ' or county_code == ' + NASSAU_COUNTY_CODE,
                 test_run=True)
