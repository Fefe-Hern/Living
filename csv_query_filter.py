import pandas as pd

def filter_data(location:str, output:str, query:str, test_run=False, chunk=10000, sep=','):
    # create empty variable dataset, and include only the Sliced queries in it
    data_slice = pd.DataFrame()
    with pd.read_csv(location, chunksize=chunk, sep=sep, header=0) as reader:
        if test_run:
            data_slice = data_slice._append(reader.get_chunk(chunk).query(query))
        else:
            for chunk in reader:
                data_slice = data_slice._append(chunk.query(query))
    
    # Save the data to a csv file
    data_slice.to_csv(output)
    return data_slice





if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Filter CSV by query')
    parser.add_argument('location', type=str, help='location of the CSV file')
    parser.add_argument('output', type=str, help='location of the output CSV file')
    parser.add_argument('query', type=str, help='query to filter the CSV file')
    parser.add_argument('--test', action='store_true', help='run a test of the first 10000 rows')
    parser.add_argument('--chunk', type=int, default=10000, help='chunksize for the CSV reader')
    parser.add_argument('--sep', type=str, default=',', help='separator for the CSV reader')
    args = parser.parse_args()

    filter_data(args.location, args.output, args.query, args.test, args.chunk, args.sep)

