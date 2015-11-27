#!/usr/bin/env python
import requests
import argparse
import sys

key_upload_url = 'http://keymaster.sjodle.com/k'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload SSH key to Keymaster")
    parser.add_argument('filename', help='Public keyfile to upload.')
    args = parser.parse_args()

    try:
        print("Uploading key " + args.filename)
        with open(args.filename[0]) as key_file:
            public_key = key_file.read()
            key_req = requests.post(key_upload_url,
                                    data={'public_key': public_key})
            key_req.raise_for_status()
            print("Your key has been uploaded successfully!")
            print("View or install it from any browser on any device:")
            print(key_req.text)
    except IOError as error:
        sys.exit('File not found: ' + filename)
