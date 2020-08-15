from invoke import task
import toml
import os


@task
def serve(c):
    generate_resources()
    re_exec("pelican content -l -r -t theme -b 0.0.0.0")


@task
def build(c):
    generate_resources()
    c.run("pelican content -t theme")
    c.run("rm -rf output/theme/.webassets-cache")


def re_exec(cmd):
    args = cmd.split(" ")
    os.execvp(args[0], args)


def generate_resources():
    os.makedirs("content/pages/generated", exist_ok=True)
    with open("content/resources.toml", "r") as f:
        resources = toml.load(f)

    main_page_content = []
    for category in resources["category"]:
        generate_resource_category(category, resources)

        main_page_content += [f"# {category['title']}\n"] + [
            render_resource(resource) for resource in resources[category["slug"]]
        ]

    with open("content/pages/generated/local-resources.md", "w") as f:
        f.write(RESOURCES_HEADER + "\n".join(main_page_content) + RESOURCES_FOOTER)


RESOURCES_HEADER = """---
title: Local Resources
slug: local-resources
---

All service providers listed below have been visited by a local member of the
transgender/non-binary community and have had a positive experience.

[TOC]

"""

RESOURCES_FOOTER = """
To update information on the site please [send us an email][email] or [submit a PR here][PR]

[email]: mailto:webmistress@trans-north-alabama.org
[PR]: https://github.com/Nitori-/north-alabama-trans
"""


def generate_resource_category(category, resources):
    slug = category["slug"]
    category_title = category["title"]
    header = f"""---
title: {category_title}
slug: {slug}
---

# {category_title}

"""
    content = [render_resource(resource) for resource in resources[slug]]

    rendered = header + "\n".join(content) + RESOURCES_FOOTER
    with open(os.path.join("content/pages/generated", f"{slug}.md"), "w") as f:
        f.write(rendered)


def render_resource(resource):
    bullets = resource.get("bullets", []) + [render_contact(resource)]
    squashed = "\n".join("  - " + bullet for bullet in bullets)
    return f"""**{resource['title']} ({resource['city']})**

{squashed}
"""


def render_contact(resource):
    contents = []
    if "website" in resource:
        contents.append(f"[Website]({resource['website']})")
    if "phone" in resource:
        phone: str = resource["phone"]
        formatted = "(" + phone.replace("-", ") ", 1)
        contents.append(f"[{formatted}](tel:{phone})")
    if "email" in resource:
        contents.append(f"[Email](mailto:{resource['email']})")
    return ", ".join(contents)
