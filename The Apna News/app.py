    from flask import Flask, render_template,request
    from bs4 import BeautifulSoup
    import pandas as pd
    import ssl
    import requests
    import bs4
    import json


    app = Flask(__name__)


    @app.route("/")
    def index():
        url = "https://m.dailyhunt.in/news/india/english"
        headers = {
                    'Agent-Encoding':'qzip,deflate,sdch',
                    'Accept-Language':'en-IN,en:q=0.8 ',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36.',
                    'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
                    'Referer':'https://www.wikipedia.org/',
                    'Connection':'keep-alive',

        }
        r=  requests.get(url,headers=headers)
    

        Soup =  BeautifulSoup(r.text, 'html.parser')
        

    
        imgV = []
        titleV = []
        timeV = []
        linkV = []
        summaryV = []


        for x in Soup.findAll("ul" , {'id':'newsHeadline'}):

            for y in x.findAll('li', {'class':'lang_en'}):
                title = y.find('h2')
                titleV.append(title.text)

                link = y.find('a')["href"]
                base_url = "https://" + link[1::]
                linkV.append(link)

                img = y.find('img')["src"]
                imgV.append(img)
                
                summary = y.find('p')
                summaryV.append(summary.text)
        
                    

        data = zip(titleV,linkV,imgV,summaryV)
        return render_template('index.html', data = data)

    @app.route("/article")
    def cnews():
        url = "https://m.dailyhunt.in/news/india/english"
        headers = {
                    'Agent-Encoding':'qzip,deflate,sdch',
                    'Accept-Language':'en-IN,en:q=0.8 ',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36.',
                    'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
                    'Referer':'https://www.wikipedia.org/',
                    'Connection':'keep-alive',

        }
        r=  requests.get(url,headers=headers)
    

        Soup =  BeautifulSoup(r.text, 'html.parser')

        linkV = []

        for x in Soup.findAll("ul" , {'id':'newsHeadline'}):

                link = x.find('a')["href"]
                base_url = "https://" + link[1::]
                linkV.append(link)

        linkV = linkV  

        re = requests.get(linkV,headers=headers)
        soup2 = BeautifulSoup(re.content,'html.parser')
        
        heading = []
        art = []
        img = []



        for y in soup2.findAll('div',{'class':'details_data'}):
            for a in y.findAll('h1'):
                heading.append(a.text)

        
        for y in soup2.findAll('div',{'class':'details_data'}):
            for x in y.findAll('figure'):
                image = x.find('img')["src"]
                img.append(image)

            
        for y in soup2.findAll('div',{'class':'details_data'}) : 
            for x in y.findAll("div",{"class":"data"}):  
                content = x.findAll('p')
                art.append(x.text)

        data2 = zip(heading,img,art)

        return render_template('content.html',data2=data2)
            

    @app.route("/biharnews")
    def home():
        url = "https://navbiharpatrika.com/"
        headers = {
                    'Agent-Encoding':'qzip,deflate,sdch',
                    'Accept-Language':'en-IN,en:q=0.8 ',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36.',
                    'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
                    'Referer':'https://www.wikipedia.org/',
                    'Connection':'keep-alive',
                }
        r=  requests.get(url,headers=headers)

        Soup =  BeautifulSoup(r.text, 'html.parser')


        imgb = []
        titleb = []
        timeb = []
        linkb = []
        summaryb = []
            

        for x in Soup.findAll("div" , {'class':'td_module_6 td_module_wrap td-animation-stack'}):

            
            title = x.find('h3')
            titleb.append(title.text)

            link = x.find('a')["href"]
            #base_url = "https://news.google.com" + link[1::]
            linkb.append(link)

            img = x.find('img')["src"]
            imgb.append(img)



        data = zip(titleb,linkb,imgb)
            #df = pd.DataFrame(data=data)
        # print(df)
        return render_template('bihar.html', data = data)


    @app.route("/worldnews")
    def world():
        url ="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
        headers = {
                    'Agent-Encoding':'qzip,deflate,sdch',
                    'Accept-Language':'en-IN,en:q=0.8 ',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36.',
                    'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
                    'Referer':'https://www.wikipedia.org/',
                    'Connection':'keep-alive',

                }
        r=  requests.get(url,headers=headers)

        Soup =  BeautifulSoup(r.text, 'html.parser')


        imgV = []
        titleV = []
        timeV = []
        linkV = []
        summaryV = []
            

        for x in Soup.findAll("div" , {'jscontroller':'d0DtYd'}):

            for y in x.findAll('div', {'class':'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}):
                title = y.find('h3')
                titleV.append(title.text)

                link = y.find('a')["href"]
                base_url = "https://news.google.com" + link[1::]
                linkV.append(base_url)

                img = y.find('img')["src"]
                imgV.append(img)
                
                summary = y.find('h4')
                summaryV.append(summary.text)


        data = zip(titleV,linkV,imgV,summaryV)
            #df = pd.DataFrame(data=data)
        # print(df)
        return render_template('worldnews.html', data = data)
        
    @app.route("/buissness")
    def buissness():
        url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
        headers = {
                    'Agent-Encoding':'qzip,deflate,sdch',
                    'Accept-Language':'en-IN,en:q=0.8 ',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36.',
                    'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
                    'Referer':'https://www.wikipedia.org/',
                    'Connection':'keep-alive',

                }
        r=  requests.get(url,headers=headers)

        Soup =  BeautifulSoup(r.text, 'html.parser')


        imgV = []
        titleV = []
        timeV = []
        linkV = []
        summaryV = []
            

        for x in Soup.findAll("div" , {'jscontroller':'d0DtYd'}):

            for y in x.findAll('div', {'class':'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}):
                title = y.find('h3')
                titleV.append(title.text)

                link = y.find('a')["href"]
                base_url = "https://news.google.com" + link[1::]
                linkV.append(base_url)

                img = y.find('img')["src"]
                imgV.append(img)
                
                summary = y.find('h4')
                summaryV.append(summary.text)


        data = zip(titleV,linkV,imgV,summaryV)
            #df = pd.DataFrame(data=data)
        # print(df)
        return render_template('buissness.html', data = data)

    @app.route("/tech")
    def tech():
        url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
        headers = {
                    'Agent-Encoding':'qzip,deflate,sdch',
                    'Accept-Language':'en-IN,en:q=0.8 ',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36.',
                    'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
                    'Referer':'https://www.wikipedia.org/',
                    'Connection':'keep-alive',

                }
        r=  requests.get(url,headers=headers)

        Soup =  BeautifulSoup(r.text, 'html.parser')


        imgV = []
        titleV = []
        timeV = []
        linkV = []
        summaryV = []
            

        for x in Soup.findAll("div" , {'jscontroller':'d0DtYd'}):

            for y in x.findAll('div', {'class':'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}):
                title = y.find('h3')
                titleV.append(title.text)

                link = y.find('a')["href"]
                base_url = "https://news.google.com" + link[1::]
                linkV.append(base_url)

                img = y.find('img')["src"]
                imgV.append(img)
                
                summary = y.find('h4')
                summaryV.append(summary.text)


        data = zip(titleV,linkV,imgV,summaryV)
            #df = pd.DataFrame(data=data)
        # print(df)
        return render_template('tech.html', data = data)


    @app.route("/sports")
    def sports():
        url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
        headers = {
                    'Agent-Encoding':'qzip,deflate,sdch',
                    'Accept-Language':'en-IN,en:q=0.8 ',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36.',
                    'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
                    'Referer':'https://www.wikipedia.org/',
                    'Connection':'keep-alive',

                }
        r=  requests.get(url,headers=headers)

        Soup =  BeautifulSoup(r.text, 'html.parser')


        imgV = []
        titleV = []
        timeV = []
        linkV = []
        summaryV = []
            

        for x in Soup.findAll("div" , {'jscontroller':'d0DtYd'}):

            for y in x.findAll('div', {'class':'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}):
                title = y.find('h3')
                titleV.append(title.text)

                link = y.find('a')["href"]
                base_url = "https://news.google.com" + link[1::]
                linkV.append(base_url)

                img = y.find('img')["src"]
                imgV.append(img)
                
                summary = y.find('h4')
                summaryV.append(summary.text)


        data = zip(titleV,linkV,imgV,summaryV)
            #df = pd.DataFrame(data=data)
        # print(df)
        return render_template('sports.html', data = data)

    @app.route("/science")
    def science():
        url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
        headers = {
                    'Agent-Encoding':'qzip,deflate,sdch',
                    'Accept-Language':'en-IN,en:q=0.8 ',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36.',
                    'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
                    'Referer':'https://www.wikipedia.org/',
                    'Connection':'keep-alive',

                }
        r=  requests.get(url,headers=headers)

        Soup =  BeautifulSoup(r.text, 'html.parser')


        imgV = []
        titleV = []
        timeV = []
        linkV = []
        summaryV = []
            

        for x in Soup.findAll("div" , {'jscontroller':'d0DtYd'}):

            for y in x.findAll('div', {'class':'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}):
                title = y.find('h3')
                titleV.append(title.text)

                link = y.find('a')["href"]
                base_url = "https://news.google.com" + link[1::]
                linkV.append(base_url)

                img = y.find('img')["src"]
                imgV.append(img)
                
                summary = y.find('h4')
                summaryV.append(summary.text)


        data = zip(titleV,linkV,imgV,summaryV)
            #df = pd.DataFrame(data=data)
        # print(df)
        return render_template('science.html', data = data)

    @app.route("/rashifal")
    def rashifal():
        url = "https://www.amarujala.com/astrology/predictions"
        headers = {
                    'Agent-Encoding':'qzip,deflate,sdch',
                    'Accept-Language':'en-IN,en:q=0.8 ',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36.',
                    'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
                    'Referer':'https://www.wikipedia.org/',
                    'Connection':'keep-alive',

                }
        r=  requests.get(url,headers=headers)

        Soup =  BeautifulSoup(r.text, 'html.parser')


        imgV = []
        titleV = []
        timeV = []
        linkV = []
        summaryV = []
            

        for x in Soup.findAll("div" , {'class':'col-xs-12 col-md-4'}):

            for y in x.findAll("section",{'class':'listing-kit-square divider-dot small80 txt-cut-80 auw-lazy-load'}):

                title = y.find('h3')
                titleV.append(title.text)

                link = y.find('a')["href"]
                base_url ="https://www.amarujala.com/" + link[1::]
                linkV.append(base_url)

                img = y.find('img')["src"]
                imgV.append(img)

                #summary = y.find('p')
                #summaryV.append(summary.text)

        data = zip(titleV,linkV,imgV)
            #df = pd.DataFrame(data=data)
        # print(df)
        return render_template('rashifal.html', data = data)

    @app.route("/hindi")
    def hindinews():
        url = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtaHBLQUFQAQ?hl=hi&gl=IN&ceid=IN%3Ahi"
        headers = {
                    'Agent-Encoding':'qzip,deflate,sdch',
                    'Accept-Language':'en-IN,en:q=0.8 ',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36.',
                    'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
                    'Referer':'https://www.wikipedia.org/',
                    'Connection':'keep-alive',

                }
        r=  requests.get(url,headers=headers)

        Soup =  BeautifulSoup(r.text, 'html.parser')


        imgV = []
        titleV = []
        timeV = []
        linkV = []
        summaryV = []
            

        for x in Soup.findAll("div" , {'jscontroller':'d0DtYd'}):

            for y in x.findAll('div', {'class':'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}):
                title = y.find('h3')
                titleV.append(title.text)

                link = y.find('a')["href"]
                base_url = "https://news.google.com" + link[1::]
                linkV.append(base_url)

                img = y.find('img')["src"]
                imgV.append(img)
                
                summary = y.find('h4')
                summaryV.append(summary.text)


        data = zip(titleV,linkV,imgV,summaryV)
            #df = pd.DataFrame(data=data)
        # print(df)
        return render_template('hindex.html', data = data)

    @app.route("/hindi/world")
    def hindinewsworld():
        url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtaHBHZ0pKVGlnQVAB?hl=hi&gl=IN&ceid=IN%3Ahi"
        headers = {
                    'Agent-Encoding':'qzip,deflate,sdch',
                    'Accept-Language':'en-IN,en:q=0.8 ',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36.',
                    'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
                    'Referer':'https://www.wikipedia.org/',
                    'Connection':'keep-alive',

                }
        r=  requests.get(url,headers=headers)

        Soup =  BeautifulSoup(r.text, 'html.parser')


        imgV = []
        titleV = []
        timeV = []
        linkV = []
        summaryV = []
            

        for x in Soup.findAll("div" , {'jscontroller':'d0DtYd'}):

            for y in x.findAll('div', {'class':'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}):
                title = y.find('h3')
                titleV.append(title.text)

                link = y.find('a')["href"]
                base_url = "https://news.google.com" + link[1::]
                linkV.append(base_url)

                img = y.find('img')["src"]
                imgV.append(img)
                
                summary = y.find('h4')
                summaryV.append(summary.text)


        data = zip(titleV,linkV,imgV,summaryV)
            #df = pd.DataFrame(data=data)
        # print(df)
        return render_template('hworld.html', data = data)

    @app.route("/hindi/buissness")
    def hindinewsbuissness():
        url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtaHBHZ0pKVGlnQVAB?hl=hi&gl=IN&ceid=IN%3Ahi"
        headers = {
                    'Agent-Encoding':'qzip,deflate,sdch',
                    'Accept-Language':'en-IN,en:q=0.8 ',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36.',
                    'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
                    'Referer':'https://www.wikipedia.org/',
                    'Connection':'keep-alive',

                }
        r=  requests.get(url,headers=headers)

        Soup =  BeautifulSoup(r.text, 'html.parser')


        imgV = []
        titleV = []
        timeV = []
        linkV = []
        summaryV = []
            

        for x in Soup.findAll("div" , {'jscontroller':'d0DtYd'}):

            for y in x.findAll('div', {'class':'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}):
                title = y.find('h3')
                titleV.append(title.text)

                link = y.find('a')["href"]
                base_url = "https://news.google.com" + link[1::]
                linkV.append(base_url)

                img = y.find('img')["src"]
                imgV.append(img)
                
                summary = y.find('h4')
                summaryV.append(summary.text)


        data = zip(titleV,linkV,imgV,summaryV)
            #df = pd.DataFrame(data=data)
        # print(df)
        return render_template('hbuissness.html', data = data)

    @app.route("/hindi/sports")
    def hindinewssports():
        url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtaHBHZ0pKVGlnQVAB?hl=hi&gl=IN&ceid=IN%3Ahi"
        headers = {
                    'Agent-Encoding':'qzip,deflate,sdch',
                    'Accept-Language':'en-IN,en:q=0.8 ',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36.',
                    'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
                    'Referer':'https://www.wikipedia.org/',
                    'Connection':'keep-alive',

                }
        r=  requests.get(url,headers=headers)

        Soup =  BeautifulSoup(r.text, 'html.parser')


        imgV = []
        titleV = []
        timeV = []
        linkV = []
        summaryV = []
            

        for x in Soup.findAll("div" , {'jscontroller':'d0DtYd'}):

            for y in x.findAll('div', {'class':'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}):
                title = y.find('h3')
                titleV.append(title.text)

                link = y.find('a')["href"]
                base_url = "https://news.google.com" + link[1::]
                linkV.append(base_url)

                img = y.find('img')["src"]
                imgV.append(img)
                
                summary = y.find('h4')
                summaryV.append(summary.text)


        data = zip(titleV,linkV,imgV,summaryV)
            #df = pd.DataFrame(data=data)
        # print(df)
        return render_template('hsports.html', data = data)







    if __name__ == "__main__":
        app.run(debug=True)



                                            