from textnode import TextNode
from htmlnode import HTMLNode

def main():
    text_node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    html_node = HTMLNode("h1", "Our Blog is the Best", [], {"href": "https://www.google.com", "target": "_blank"})
    print(text_node)
    print(html_node)


if __name__ == "__main__":
    main()
