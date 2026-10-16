"""Public search lead discovery. No Facebook login or automated posting."""
import csv
import datetime as dt
import html
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

SEARCHES = [
    'site:facebook.com/groups/ Cincinnati looking for carpenter door installation',
    'site:facebook.com/groups/ Cincinnati need trim baseboard contractor',
    'site:facebook.com/groups/ Northern Kentucky need carpenter cabinets decks',
    'site:reddit.com/r/cincinnati looking for carpenter doors trim',
]

def rss_search(query):
    url = 'https://www.bing.com/search?format=rss&q=' + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=18) as response:
        root = ET.fromstring(response.read())
    for item in root.findall('.//item'):
        yield {
            'title': item.findtext('title', ''),
            'url': item.findtext('link', ''),
            'description': re.sub('<[^>]+>', ' ', html.unescape(item.findtext('description', ''))),
            'search': query,
            'checked_utc': dt.datetime.now(dt.timezone.utc).isoformat()
        }

rows = []
seen = set()
for query in SEARCHES:
    try:
        for item in rss_search(query):
            if item['url'] not in seen:
                seen.add(item['url'])
                rows.append(item)
    except Exception as exc:
        print(f'Search unavailable: {query}: {exc}')

with open('results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'url', 'description', 'search', 'checked_utc'])
    writer.writeheader()
    writer.writerows(rows)
print(f'Collected {len(rows)} public search results; not verified active jobs.')
