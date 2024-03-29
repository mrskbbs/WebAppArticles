def htmlBuilder(editor: bool, blocks: list) -> str:
    html: str = ""

    if editor:
        TEMPLATES: dict = {
            "h1": "<textarea class = 'h1' rows = '1'>{}</textarea>",
            "p": "<textarea class = 'p' rows = '10'>{}</textarea>",
        }
    else:
        TEMPLATES: dict = {
            "h1": "<h1>{}</h1>",
            "p": "<p>{}</p>",
        }
    
    for block in blocks:
        node = ""
        
        for element in block:
            node += TEMPLATES[element["type"]].format(element["content"])
        
        html += f"<div class = 'block'>{node}</div>"
    
    return html

# {'packet': ['{"title":"dsfds",
# "blocks":
#       [[{"type":"h1","content":"sdffsdfsdfs"},{"type":"p","content":"sdfsdfsd"}]]