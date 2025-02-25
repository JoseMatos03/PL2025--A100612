import re
import sys

def lexical_analysis(text):
    tokens = []
    lines = text.splitlines()
    for line in lines:
        stripped = line.strip()
        if stripped == "":
            tokens.append({"type": "empty", "content": ""})
        elif stripped.startswith("### "):
            tokens.append({"type": "header", "level": 3, "content": stripped[4:]})
        elif stripped.startswith("## "):
            tokens.append({"type": "header", "level": 2, "content": stripped[3:]})
        elif stripped.startswith("# "):
            tokens.append({"type": "header", "level": 1, "content": stripped[2:]})
        elif re.match(r"^\d+\.\s", stripped):
            tokens.append({"type": "list_item", "content": re.sub(r"^\d+\.\s", "", stripped)})
        else:
            tokens.append({"type": "paragraph", "content": stripped})
    return tokens

def syntactic_analysis(tokens):
    nodes = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token["type"] == "list_item":
            list_items = []
            while i < len(tokens) and tokens[i]["type"] == "list_item":
                list_items.append(tokens[i]["content"])
                i += 1
            nodes.append({"type": "ol", "items": list_items})
            continue
        elif token["type"] == "header":
            nodes.append({"type": f'h{token["level"]}', "content": token["content"]})
        elif token["type"] == "paragraph":
            nodes.append({"type": "p", "content": token["content"]})
        i += 1
    return nodes

# Função para conversão inline (para bold, itálico, links e imagens)
def convert_inline(text):
    # Imagem: ![alt](url) -> <img src="url" alt="alt"/>
    text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', text)
    # Link: [texto](url) -> <a href="url">texto</a>
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    # Bold: **texto** -> <b>texto</b>
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Itálico: *texto* -> <i>texto</i>
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    return text

def semantic_analysis(parse_tree):
    html_lines = []
    for node in parse_tree:
        if node["type"] in ["h1", "h2", "h3"]:
            content = convert_inline(node["content"])
            html_lines.append(f'<{node["type"]}>{content}</{node["type"]}>')
        elif node["type"] == "ol":
            html_lines.append("<ol>")
            for item in node["items"]:
                content = convert_inline(item)
                html_lines.append(f'<li>{content}</li>')
            html_lines.append("</ol>")
        elif node["type"] == "p":
            html_lines.append(f'<p>{convert_inline(node["content"])}</p>')
    return "\n".join(html_lines)

def convert(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    tokens = lexical_analysis(markdown_text)
    parse_tree = syntactic_analysis(tokens)
    html_output = semantic_analysis(parse_tree)
    return html_output

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Uso: python markdown_converter.py <ficheiro_markdown> <ficheiro_html>")
        sys.exit(1)

    file_path = sys.argv[1]
    output_path = sys.argv[2]

    html_result = convert(file_path)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_result)

    print(f"Conversão concluída! Resultado guardado em: {output_path}")
