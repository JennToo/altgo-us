AUTHOR = "Jennifer Wilcox"
SITENAME = "ALTGO"
SITEURL = "https://altgo.us"
LOGO = "https://altgo.us/theme/images/logo.png"

PATH = "content"

TIMEZONE = "America/Chicago"

DEFAULT_LANG = "en"

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = None
SOCIAL = None

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["assets", "sitemap"]
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.toc": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

STATIC_PATHS = ["extra_static"]
EXTRA_PATH_METADATA = {
    "extra_static/favicon.ico": {"path": "favicon.ico"},
    "extra_static/robots.txt": {"path": "robots.txt"},
    "extra_static/.htaccess": {"path": ".htaccess"},
}

SITEMAP = {
    "format": "xml",
    "exclude": ["tags.html", "categories.html", "authors.html", "archives.html"],
}
