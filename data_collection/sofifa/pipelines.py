# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import csv

class SofifaPipeline(object):

    def open_spider(self, spider):
        self.link_store = open('links_collected.txt', 'a') #stores links already explored
        self.output = open('data.csv','a',newline='',encoding='utf-8-sig') #adds data to new line in csv


    def close_spider(self, spider):
        self.link_store.close()
        self.output.close()


    def process_item(self, item, spider):
        
        #store the link in a text file to keep track of players 
        self.link_store.write(item['link'] + "\n")

        #write item to new row in csv file
        w = csv.writer(self.output)
        w.writerow(item.values())

        return item
