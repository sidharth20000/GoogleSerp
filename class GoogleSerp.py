class GoogleSerp:
    def __init__(self):
        self.host = 'as.6f757bda1aeab8dc.abcproxy.vip'
        self.port = 4950
        self.username = 'idfl5FDdpz-zone-star-region-IN'
        self.password = '25512033'
        self.proxy = f'http://{self.username}:{self.password}@{self.host}:{self.port}'
        self.proxies = {
            'http': self.proxy,
            'https': self.proxy
        }
        
    def serperImg(self, query):
        url = "https://google.serper.dev/images"
        payload = json.dumps({"q": query,"gl":"in"})
        headers = {'X-API-KEY': 'a0e466b0d17cfe2bf2e25b3a36ef0b0d4e523d1b',
                   'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            data = response.json()
            return [i.get('imageUrl') for i in data['images'] if "imageUrl" in list(i.keys()) and ".jpg" in i['imageUrl'] or ".png" in i['imageUrl']]
        
    def serper(self, query):
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query,"gl":"in"})
        headers = {'X-API-KEY': 'a0e466b0d17cfe2bf2e25b3a36ef0b0d4e523d1b',
                   'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            data = response.json()
#             data1 = [{'title':i.get('title'), 'snippet':i.get('snippet'), 'links':i.get('link')} for i in data["organic"]]
            link_output = [(i['link'], i['snippet'], i['title']) for i in data['organic'] if "snippet" in list(i.keys()) and "title" in list(i.keys()) and "link" in list(i.keys())]

            if "answerBox" in data.keys():
                ansbox = [(data["answerBox"]['link'], data["answerBox"]['snippet'], data["answerBox"]['title']) if "link" in  data["answerBox"].keys() and "snippet" in data["answerBox"].keys() else ("", data["answerBox"]["answer"], "")]
                if bool(re.match(r'^[-+]?[0-9]+$', ansbox[0][1].replace(" ", ""))) or bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$',ansbox[0][1].replace(" ", ""))):
                    description = [i[2]+ " " + i[1] for i  in link_output][:5]
                    link = [i[0] for i in link_output][:5]
                    return {"chat":f"{query} = {ansbox[0][1].replace(' ', '')}", "links": link,"descriptions": description, "related_search": related_search, "images": [],"lastQuestion":f"{query} = {ansbox[0][1].replace(' ', '')}","lastquery":query}
                else:
                    link_output = ansbox + link_output
            return {"crawl":link_output}
    
    def imageSearch(self, query, results, i):
        try:
            s = time.perf_counter()
            query = "+".join(query.split())
            url = "https://www.google.com/search?q="+query+"&source=lnms&tbm=isch&num=10"
            webpage = requests.get(url, proxies=self.proxies, timeout=2)
            if time.perf_counter()<s+4:
                if webpage.status_code == 200:
                    soup = bs(webpage.content, 'html.parser')
                    image_tags = soup.find_all('img', class_='DS1iW')
                    results[i]= [image_tag['src'] for image_tag in image_tags]
                else:
                    results[i]= self.serperImg(query)
            else:
                results[i]= self.serperImg(query)
        except Exception as e:
            results[i]= self.serperImg(query)
        
    def webSearch(self, query, results, i):
        try:
            pattern = r'(http.*?)&'
            s = time.perf_counter()
            query = query.replace(" ", "+")
            url = f"https://www.google.com/search?q={query}"
            searchResult = requests.get(url, proxies=self.proxies,timeout=2.5)
            if time.perf_counter()<=s+4:
                if searchResult.status_code == 200:
                    scrap= bs(searchResult.text)
                    crawl= [{"title" :i.find("h3").text, "snippet": re.sub(r'\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}\s·\s',"",re.sub(r"Missing:.*",'', re.sub(r".*?ago ·", "",i.find("div", class_="BNeawe s3v9rd AP7Wnd").text).strip())),"links" : re.sub(r'(?<=%)25', '',re.findall(pattern,re.sub(r'%3F|%3D', lambda match: '?' if match.group(0) == '%3F' else '=', i.find("a").get("href")))[0])} for i in scrap.find_all("div", class_="Gx5Zad fP1Qef xpd EtOod pkphOe")]
                    link_output = [(i.get('links'), i.get('snippet'), i.get('title')) for i in crawl ]
                    results[i] =  {"crawl":link_output}

                else:
                    results[i] = self.serper(query)
            else:
                results[i]=  self.serper(query)
        except Exception as e:
            results[i]= self.serper(query)
            