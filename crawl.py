from lxml import html

def get_urls_from_string (page_content : str, base_url : str):
    dom = html.fromstring(page_content, base_url):
    dom.make_links_absolute(base_url)

    links = []
    for elem in dom.iter():
        if elem.tag == "a":
            links.append(elem.get("href"))
    
    return links
