import requests
import re
import lxml.html
import urllib.parse

CATEGORIES = [
    "art_and_design", "auto_and_vehicles","books_and_reference",
    "brain", "business", "comics","communication",
    "education","entertainment", "finance",
    "game", "health_and_fitness", "house_and_home",
    "libraries_and_demo", "lifestyle", "media_and_video",
    "medical", "music_and_audio", "news_and_magazines",
    "personalization", "photography", "productivity",
    "shopping", "social", "sports", "tools",
    "transportation", "travel_and_local", "weather"
]



TOPSELLING_FREE = 'topselling_free'
TOPSELLING_PAID = 'topselling_paid'


BASE_URL = "https://play.google.com"

def _get_float(s):
    for i in s.split():
        try:
            return float(i)
        except:
            continue

def _get_text(doc, _path):
    els = doc.xpath(_path)
    if len(els) > 0:
        return els[0].text_content().strip()
    else:
        return None
    

def _get_attrs(doc, _path, attr):
    return [el.get(attr) for el in doc.xpath(_path)]


def _get_apps(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None

    doc = lxml.html.fromstring(r.content)
    pattern = r"id=(.+)"
    hrefs = _get_attrs(doc, '//a', 'href')
    
    apps = list(set([re.search(pattern, el).group(1)
         for el in hrefs if el.startswith('/store/apps/details')]))
    
    return apps


def leaderboard(identifier, category=None, start=0, num=24, hl="en"):
    if identifier not in ('topselling_paid', 'topselling_free'):
        raise Exception("identifier must be topselling_paid or topselling_free")

    url = 'https://play.google.com/store/apps'
    if category:
        if category not in CATEGORIES:
            raise Exception('%s not exists in category list' % category)
        url += "/category/" + str(category).upper()

    url += "/collection/%s?start=%s&num=%s&hl=%s" % (identifier, start, num, hl)
    return _get_apps(url)

def search(query, hl="en", c="apps"):
    url = ('https://play.google.com/store/search'
           '?q=%s&hl=%s&c=%s') % (query, hl, c)
    return _get_apps(url)


def developer(developer, num=24, hl="en", c="apps"):
    url = ('https://play.google.com/store/apps/developer'
           '?id=%s&num=%s&hl=%s&c=%s') % (
                   urllib.parse.quote_plus(developer), num, hl, c)
    return _get_apps(url)


class App(object):
    def __init__(self, package):
        self.url = "{}/store/apps/details?id={}&hl=en".format(BASE_URL, package)
        page = requests.get(self.url)
        tree = lxml.html.fromstring(page.content)
        
        for i in tree.xpath('//div[@class="IxB2fe"]/child::div[@class="hAyfc"]'):
            sel = i.xpath('div/text()')
            ans = i.xpath('span/div/span/text()')
            if len(sel) and len(ans) > 0:
                if sel[0] == 'Updated':
                    self.updated = ans[0]
                elif sel[0] == 'Size':
                    self.size = ans[0]
                elif sel[0] == 'Installs':
                    self.installs = ans[0]
                elif sel[0] == 'Current Version':
                    self.version = ans[0]
                elif sel[0] == 'Requires Android':
                    self.android = ans[0]
                elif sel[0] == 'Content Rating':
                    self.content_rating = ans[0]
            
        self.name = _get_text(tree, '//h1[@itemprop="name"]')
        self.package_name = package
        self.description = _get_text(tree, '//div[@itemprop="description"]/content/div')
        self.category = _get_text(tree, '//a[@itemprop="genre"]')
        self.logo = _get_attrs(tree, '//img[@alt="Cover art"]', 'src')[0]
        self.price = _get_attrs(tree, '//meta[@itemprop="price"]', 'content')[0]
        self.free = self.price == 0
        self.developer_name = _get_text(tree, '//a[@class="hrTbp R8zArc"]')
        self.developer_email = _get_attrs(tree, '//a[starts-with(@href, "mailto")]', 'href')[0][7:]
        self.developer_website = _get_attrs(tree, '//a[text()="Visit website"]', 'href')[0]
        self.rating = _get_float(_get_attrs(tree, '//div[starts-with(@aria-label, "Rated")]', 'aria-label')[0])
        self.reviews = _get_text(tree, '//span[contains(@aria-label, "ratings")]').replace(',', '')
        self.images = list(filter(None, _get_attrs(tree, '//img[@alt="Screenshot Image"]', 'data-src')))
        self.similar = _get_apps(_get_attrs(tree, '//a[@aria-label="Check out more content from Similar"]', 'href')[0])

    def __repr__(self):
        return '<app title={}; package={}>'.format(self.name, self.package_name)

    def __str__(self):
        return self.name

    def __getitem__(self, key):
        return self.__dict__[key]
