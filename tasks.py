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
    c.run("pelican content -t theme --verbose")
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
        main_page_content += [f'# {category["title"]}\n<div class="resources">'] + [
            render_resource(resource) for resource in resources[category["slug"]]
        ] + ["</div>\n"]

    with open("content/pages/generated/local-resources.md", "w") as f:
        f.write(RESOURCES_HEADER + "\n".join(main_page_content) + RESOURCES_FOOTER)


RESOURCES_HEADER = """---
title: Local Resources
slug: local-resources
description: A collection of Alabama businesses and services that are friendly to transgender and non-binary people
---

All service providers listed below have been visited by a local member of the
transgender / non-binary community and have had a positive experience.

**If you would like to submit an update for this list, please send us an email
at [website@altgo.us][email] or [submit a GitHub PR here][PR]**

[TOC]

"""

RESOURCES_FOOTER = """
[email]: mailto:website@altgo.us
[PR]: https://github.com/JennToo/altgo-us
"""


def render_resource(resource):
    bullets = render_contact(resource) + resource.get("bullets", [])
    squashed = "\n".join(f"<li>{bullet}</li>" for bullet in bullets)
    return f"""<div class="resource">
<div class="resource-title">{resource['title']}</div>
<ul class="resource-bullets">
<li><span class="resource-label">Location:</span> {resource['city']}</li>
{squashed}
</ul>
</div>
"""


def render_contact(resource):
    contents = []
    if "website" in resource:
        contents.append(f"""
            <span class="resource-label">Website:</span> <a href="{resource["website"]}" class="website">{resource["website"]}</a>
        """)
    if "phone" in resource:
        phone: str = resource["phone"]
        formatted = "(" + phone.replace("-", ") ", 1)
        contents.append(f"""
            <span class="resource-label">Phone Number:</span> <a href="tel:{phone}">{formatted}</a>
        """)
    if "email" in resource:
        contents.append(f"""
            <span class="resource-label">Email:</span> <a href="mailto:{resource["email"]}" class="email">{resource["email"]}</a>
        """)
    return contents
