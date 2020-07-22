import argparse

import metadata

parser=argparse.ArgumentParser(description='Get metadata value of query parameters')

parser.add_argument('--dir_path',type=str,help='Path to the directory of the metadata file', required=True)

parser.add_argument('--get', type=str,help='Query to execute. If query parameter is found,it return the value/dict of values')

args=parser.parse_args()

mtd=metadata.Metadata(args.dir_path)

mtd.get_cli(args.get)



