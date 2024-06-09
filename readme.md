<h1 align="center">Metadata Scraper</h1>

<p align="center">
  Scrapes metadata from a URL and returns it in JSON format.
</p>

<p align="center">
  <a href="#introduction"><strong>Introduction</strong></a> ·
  <a href="#self-hosting"><strong>Self-hosting</strong></a> ·
  <a href="#tech-stack"><strong>Tech Stack</strong></a> ·
</p>

<br/>

## Introduction

Metadata Scraper is a simple API that scrapes metadata from a URL and returns it in JSON format. It uses [FastAPI](https://fastapi.tiangolo.com/) as the framework, [Requests](https://docs.python-requests.org/en/master/) for making HTTP requests, and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for parsing HTML.

### Endpoints

- `GET /metadata?url={url}` – Scrapes metadata from the given URL and returns it in JSON format. URL should be a FQDN (Fully Qualified Domain Name).

### Example

```bash
curl -X GET "http://meta.kelvinamoaba.com/metadata?url=https://www.google.com"
```

```json
{
  "title": "Google",
  "description": "Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for.",
  "image": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
}
```

## Self-hosting
You can run the project with docker. First, clone the repository and navigate to the project directory.

```bash
git clone
cd metadata-scraper
```

Then, build the docker image.

```bash
docker build -t metadata-scraper .
```

Finally, run the docker container.

```bash
docker run -d -p 9000:9000 metadata-scraper
```

The API will be available at `http://127.0.0.1:9000`.


## Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/) – framework
- [Requests](https://docs.python-requests.org/en/master/) – HTTP library
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) – HTML parser
