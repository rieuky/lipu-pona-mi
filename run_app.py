#!/usr/bin/env python3
import yaml

from src.bottle import route, run, static_file, template


@route("/static/css/<filename>")
def serve_css(filename):
    return static_file(filename, root="./static/css")


@route("/")
def index():
    with open("example-sites.yaml", "r") as file:
        data = yaml.safe_load(file)

    content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LipuPonaMi</title>
        <link rel="stylesheet" type="text/css" href="/static/css/main.css">
    </head>
    <body>
        <h1>Useful Research Sites</h1>
        % for category in data['research_sites']:
            <h2>{{category['category']}}</h2>
            <ul>
            % for site in category['sites']:
                <li><a href="{{site['link']}}" target="_blank">{{site['name']}}</a></li>
            % end
            </ul>
        % end
    </body>
    </html>
    """
    return template(content, data=data)


if __name__ == "__main__":
    run(host="localhost", port=8282, reloader=True)
