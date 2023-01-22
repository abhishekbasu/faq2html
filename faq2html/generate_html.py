from dominate import document
from dominate.tags import br, h1, h2, html_tag, li, style, ul
from typing import Dict, List

from .qna import QnA

qna_style = """
    question {
      color: black;
      font-weight: 75;
    }
    answer {
      color:purple;
      font-weight: 150;
      margin: 20px;
    }
"""

class question(html_tag):
    pass

class answer(html_tag):
    pass

def generate_faq_html(
    parsed_faqs: Dict[str, List[QnA]],
    apply_style: bool = True
):
    html_document = document(title = "FAQ")

    with html_document.head:
        if apply_style:
            style(qna_style)
    
    with html_document:
        h1("FAQ")
        for section in parsed_faqs:
            h2(section)
            list = ul()
            for qna in parsed_faqs[section]:
                list += li(question(qna.question), br(), answer(qna.answer))
                
    return html_document.render()
