import sys
import csv


def load_spreadsheet(filepath='housing.csv', encoding='latin-1'):
    '''
        Loads all rows from the data-set

            Parameters:
                filepath (string) : Path to the input dataset csv file (default housing.csv)
                encoding (string) : Encoding of the data file (default latin-1)

            Returns:
                array of rows read from the input files
    '''
    if len(filepath) <= 0:
        raise ValueError('Please provide filepath to the csv dataset')
    # open file
    fp = open(filepath, encoding='latin-1')
    csvreader = csv.reader(fp)
    rows = []
    next(csvreader)  # skip one row
    for row in csvreader:
        rows.append(row)
    return rows


if __name__ == "__main__":

    if len(sys.argv) <= 1:
        raise ValueError('Usage: python spreadsheet.py <csv-filename>')

    filepath = sys.argv[1]
    spreadsheet = load_spreadsheet(filepath)
