import scrapy


class MatchCenterSpider(scrapy.Spider):
    name = "match-center"
    allowed_domains = ["www.yallakora.com"]
    start_urls = ["https://www.yallakora.com/match-center/"]

    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
    ]

    def parse(self, response):
        leagues = response.css('.matchCard')
        for i in range(len(leagues)):
            matches = leagues[i].css('.teamsData')
            for j in range(len(matches)):
                result = matches[j].css('.MResult span')
                yield {
                    'league' : leagues[i].css('h2 ::text').get().strip(),
                    'Team A': matches[j].css('.teamA p::text').get(),
                    'Team B': matches[j].css('.teamB p::text').get(),
                    'Result': result[0].css('span::text').get() + result[1].css('span::text').get() + result[2].css('span::text').get() ,
                    'time'  : result[3].css('span::text').get(),
                    'date'  : response.css('.dayName h2 span::text').get()
                }