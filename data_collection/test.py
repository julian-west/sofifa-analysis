"""Functions to quickly see how incremental webscraper is progressing"""
import json

def count_data():
    links = open('links_collected.txt').read().split('\n')
    links = [l for l in links if links != '']
    num_links = len(links)

    data = open('data.csv', 'r',encoding='utf-8-sig').read()
    data = data.split('\n')[:-1]
    num_data = len(data) - 1

    print(f"links explored\t\t:\t{num_links}")
    print(f"datapoints collected\t:\t{num_data}")
    print(f"\nmissing datapoints\t:\t{num_links-num_data}")

if __name__ == '__main__':
    count_data()

