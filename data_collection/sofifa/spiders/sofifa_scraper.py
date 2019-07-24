import scrapy

class QuotesSpider(scrapy.Spider):
    name = "sofifa"

    start_urls = [f'https://sofifa.com/?offset={offset}' for offset in range(0,20000,60)]


    def parse(self, response):
        """parse the list of players on each page in start_urls, collect links to each player profile"""

        #for each link on the page
        for link in response.xpath('//a/@href').extract():
            
            #if the link contains "player/" and is not present in the 'links_collected.txt' file, then follow the link
            if 'player/' in link and link not in open('links_collected.txt').read():
                yield response.follow(link, self.parse_player)


    def parse_player(self, response):
        """parse the player profile page and collect various attributes and identifiers"""

        
        data = {}

        #--------------------
        # COLLECT NAME, COUNTRY, AGE
        #--------------------
        data['link'] = response.url
        data['name'] = response.xpath('//div[contains(@class,"meta bp3-text-overflow-ellip")]/text()')[0].extract().strip()
        data['country'] = response.xpath('//div[contains(@class,"meta bp3-text-overflow-ellip")]/a/@title').get()
        data['country_link'] = response.xpath('//div[contains(@class,"meta bp3-text-overflow-ellip")]/a/@href').get()
        data['age'] = response.xpath('//div[contains(@class,"meta bp3-text-overflow-ellip")]/text()').re("Age\s(\d*)")[0]


        #--------------------
        # COLLECT OVERAL RATINGS
        #--------------------
        overall_stats = response.xpath('//div[contains(@class,"column col-4 text-center")]/span/text()').extract()
        overall_stats = [stat for stat in overall_stats if '-' not in stat and '+' not in stat]

        assert len(overall_stats)==4, overall_stats

        data['overall_rating'] = overall_stats[0]
        data['potential'] = overall_stats[1]
        data['value'] = overall_stats[2]
        data['wage'] = overall_stats[3]



        #--------------------
        # COLLECT POPULARITY METRICS
        #--------------------
        popularity = response.xpath('//div/button/span/span[contains(@class,"count")]/text()').extract()
        data['likes'] = popularity[0]
        data['dislikes'] = popularity[1]
        data['followers'] = popularity[2]


        #---------------------
        # COLLECT ATTRIBUTES
        #---------------------
        ATTRIBUTES=['Crossing','Finishing','Heading Accuracy',
                'Short Passing','Volleys','Dribbling','Curve',
                'FK Accuracy','Long Passing','Ball Control','Acceleration',
                'Sprint Speed','Agility','Reactions','Balance',
                'Shot Power','Jumping','Stamina','Strength',
                'Long Shots','Aggression','Interceptions','Positioning',
                'Vision','Penalties','Composure','Marking',
                'Standing Tackle','Sliding Tackle','GK Diving',
                'GK Handling','GK Kicking','GK Positioning','GK Reflexes']

        #collect the player attributes - note that we only want the last 34 instances (len(ATTRIBUTES)) from the xpath result
        attrs = response.xpath('//li/span[contains(@class,"bp3-tag")]/text()').extract()[-len(ATTRIBUTES):]
        assert len(attrs)==len(ATTRIBUTES), attrs
        for index, attr in enumerate(attrs):
            data[ATTRIBUTES[index]]=attr

        yield data




























#------REGEX IMPLEMENTATION--------DOESN'T WORK 100%
#get attributes using regex patterns
# page_text = ''.join(response.xpath("//body//text()").extract()).strip()  

# pattern = ''
# for attr in ATTRIBUTES:
#     pattern += r""".*?(\d*([-+](\d\s)|(\s))"""+attr+r""")"""

# pat=re.compile(pattern, re.DOTALL)    #parsing multiline text

# a=pat.match(page_text)

# stats = [stat for stat in a.groups()[::4]] #conslidate stats

# for index, attr in enumerate(ATTRIBUTES):
#     data[attr] = stats[index].split(' ')[0]