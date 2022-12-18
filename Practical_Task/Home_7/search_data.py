from export_data import export_data
from print_data import print_data

def search_data(seek_out, data):
    if len(data) > 0:
        for item in data:
            if seek_out in item:
                return item
    else:
        return None