from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            splitted_node_parts: list = node.text.split(delimiter)
            if len(splitted_node_parts) % 2 == 0:
                raise ValueError(f"'{delimiter}' delimiter is not valid Markdown syntax.")
            # Process splitted parts...
            for i in range(len(splitted_node_parts)):
                # ignore empty strings
                if splitted_node_parts[i] == "":
                    continue
                # even indices are always standard text
                if i % 2 == 0:
                    new_nodes.append(TextNode(splitted_node_parts[i], TextType.TEXT))
                # odd indices are always the formatted text type
                elif i % 2 != 0:
                    new_nodes.append(TextNode(splitted_node_parts[i], text_type))

    return new_nodes

