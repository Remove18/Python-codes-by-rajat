import argparse
import requests

def download_file(url, local_filename):
    if local_filename == None:
        local_filename = url.split('/')[-1]
        # NOTE the stream parameter bellow
    with requests.get(url, stream = True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size = 8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename

parser = argparse.ArgumentParser()

# add command line argument
parser.add_argument("url", help="url of the file to download")

# parser.add_argument("output", help="by which name do you want to save your file")
parser.add_argument("-o", "--output", type=str, help = "name of the file", default = None)

# parse the argument
args = parser.parse_args()

# use the argument in your code
download_file(args.url, args.output)