import re

def main(text_ : str, caterpillar, *args):
    args = args[0]
    if args[0] == True:
        ToC = True
    else:
        ToC = False
    try:
        if ToC_header != "":
            ToC_header = args[1]
        else:
           ToC_header = "Table of Contents" 
    except:
        ToC_header = "Table of Contents"
    ToC_source = []
    text = text_
    headings = re.findall(r"<h[1-6]>.*?</h[1-6]>", text)
    for heading in headings:
        replacing = re.sub(r"<h[1-6]>(.*?)</h[1-6]>", r"\1", heading, 0).replace(" ", "-").lower()
        ToC_source.append(replacing)
        heading_ = heading.split(">", 1)
        heading_[0] += f" id='{replacing}'><a href='#{replacing}'>#</a>"
        heading_ = "".join(heading_)
        text = re.sub(heading, heading_, text, 1)

    if ToC == True:
        for i in range(len(ToC_source)):
            ToC_source[i] = f"<li><a href='#{ToC_source[i]}'>"+re.sub(r"<h[1-6]>(.*?)</h[1-6]>", r"\1", headings[i])+"</a></li>"

            

        text = f"<div class='ToC-pathfinder'\n><h1 class='ToC-header'>{ToC_header}</h1>\n<ul>"+"\n".join(ToC_source)+"</ul></div>" + text
    return text, caterpillar


