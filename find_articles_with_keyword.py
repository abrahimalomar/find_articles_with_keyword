
# مثال للبحث عن المقالات التي تحتوي على كلمة معينة
def find_articles_with_keyword(keyword, articles_data):
    matching_articles = []
    for article_id, keywords in articles_data.items():
        if keyword in keywords:
            matching_articles.append(article_id)
    return matching_articles

articles={'1270':['it','programming','database'],
           '1271':['it','programming'],
           '1272':['database','markting','seo'],
           '1273':['seo','markting']
        }

keyword_to_search = 'programming'
result = find_articles_with_keyword(keyword_to_search, articles)
print(f"Articles related to '{keyword_to_search}': {result}")