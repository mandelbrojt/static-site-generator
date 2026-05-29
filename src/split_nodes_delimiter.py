from textnode import TextNode, TextType


def filter_nodes(nodes, operation, node_text_type):
    if operation == "eq":
        return list(filter(lambda x: x.text_type == node_text_type))



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    text_nodes = list(filter(lambda x: x.text_type == TextType.TEXT))
    new_nodes.extend()
