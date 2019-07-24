## Sofifa webscraper using scrapy

This directory contains the scrapy project used to collect individual player
attributes from the [sofifa.com website](https://sofifa.com/) which has a database
of stats relating to professional football players in the computer game FIFA.

To run the webscraper, run the following command in the prompt:

`scrapy crawl sofifa`

The scraper writes the data into a csv file (`data.csv`) line by 
line and the page link for each player after scraping is stored
a text file (`links_collected.txt`). Before scraping each player
profile, the scraper looks in the links_collected.txt file to 
see if the page has already been scraped. If it has, then it 
will move on to the next player (see pipelines.py). This has been
done so that you can stop and restart the webscraper at any time
without having to start from the beginning again - your progress
will have been saved.

__Note, that the `data.csv` and `link_collected.txt` files should both
be empty (except for the csv header) when starting the scraper
from scratch__

To be courteous to the website, a download delay has been set 
(see settings.py). As such, it can take a long time to download
everything so it is best run overnight.

Alternatively, __there is a very similar version of the dataset already
curated and maintained on the [Kaggle website](https://www.kaggle.com/karangadiya/fifa19)__
which I would recommend using instead to save you the time. 

I decided to collect the data myself (even though another version of the
dataset is available already) in order to improve my webscraping skills 
with the scrapy framework and develop data pipelines.


