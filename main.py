import utils
from pandas import DataFrame

links = utils.getLinks()
titles, viewCounts, likes, Links = [], [], [], []

for link in links:
    result = utils.getJSON(link)
    if result is None:
        continue
    title = result['title']['runs'][0]['text']
    viewCount = result['viewCount']['videoViewCountRenderer']['viewCount']['simpleText']
    viewCount = viewCount.split(' ')[0]
    if result['videoActions']['menuRenderer']['topLevelButtons'][0]. __contains__('toggleButtonRenderer'):
        like = result['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['defaultText']['simpleText']
        likes.append(like)
    else :
        likes.append(0)
    Links.append(link)
    titles.append(title)
    viewCounts.append(viewCount)
        

data = {
    'link': Links,
    'title': titles,
    'view': viewCounts,
    'like': likes
}

df = DataFrame(data)
df.to_csv('result.csv', encoding='utf-8')
