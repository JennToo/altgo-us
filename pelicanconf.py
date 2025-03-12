AUTHOR = "Jennifer Wilcox"
SITENAME = "ALTGO"
SITESUBTITLE = "A collection of support groups, resources, and legal help for Alabamians included in the transgender umbrella."
SITEURL = "https://altgo.us"
GITHUB_URL = "https://github.com/JennToo/altgo-us"
LOGO = "https://altgo.us/theme/images/logo.png"
PATH = "content"
TIMEZONE = "America/Chicago"
DEFAULT_LANG = "en"
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
DEFAULT_PAGINATION = False
FEED_ALL_ATOM = None
LINKS = None
TRANSLATION_FEED_ATOM = None

SEO_REPORT = True
SEO_ENHANCER = True
SEO_ENHANCER_OPEN_GRAPH = True
SEO_ENHANCER_TWITTER_CARDS = True

SITEMAP = {
    "format": "xml",
    "exclude": ["tags.html", "categories.html", "authors.html", "archives.html"],
}

STATIC_PATHS = ["extra_static"]
EXTRA_PATH_METADATA = {
    "extra_static/favicon.ico": {"path": "favicon.ico"},
    "extra_static/robots.txt": {"path": "robots.txt"},
    "extra_static/.htaccess": {"path": ".htaccess"},
}

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.toc": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}
