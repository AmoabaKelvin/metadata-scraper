import requests
from bs4 import BeautifulSoup


def get_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return str(e)
    return response.text


def get_metadata(page, url):
    soup = BeautifulSoup(page, "html.parser")

    def get_meta_content(attrs):
        # safer way to access the content so we return None if the attribute is not found
        tag = soup.find("meta", attrs=attrs)
        return tag["content"] if tag and "content" in tag.attrs else None

    title = soup.title.string if soup.title else None
    description = get_meta_content({"name": "description"})
    image = get_meta_content({"property": "og:image"})
    favicon = (
        soup.find("link", rel="icon")["href"]
        if soup.find("link", rel="icon")
        else None
    )

    if not favicon:
        favicon_url = None
    elif favicon.startswith("http"):
        favicon_url = favicon
    else:
        favicon_url = url + favicon

    return {
        "title": title,
        "description": description,
        "image": image,
        "favicon": favicon_url,
    }


def get_metadata_from_url(url):
    try:
        page = get_page(url)
        metadata = get_metadata(page, url)
        return metadata
    except Exception as e:
        return {"error": str(e)}
