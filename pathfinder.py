import re

def main(text_ : str, caterpillar):
    text = text_
    headings = re.findall(r"<h[1-6]>.*?</h[1-6]>", text)
    for heading in headings:
        replacing = re.sub(r"<h[1-6]>(.*?)</h[1-6]>", r"\1", heading, 0).replace(" ", "-").lower()
        heading_ = heading.split(">", 1)
        heading_[0] += f" id='{replacing}'><a href='#{replacing}'>#</a>"
        heading_ = "".join(heading_)
        text = re.sub(heading, heading_, text, 1)
    return text, caterpillar


