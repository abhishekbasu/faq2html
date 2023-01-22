from dataclasses import dataclass
import docx
import logging
from typing import Dict, List

from .errors import ParseError
from .qna import QnA

logger = logging.getLogger(__name__) 

def extract_text(
    filename,
    question_identifier="Q. ",
    answer_identifier="A. "
) -> Dict[str, List[QnA]]:
    document: docx.Document = docx.Document(filename)
    sections: Dict[str, List[QnA]] = {}  # Python 3.7+ preserves insertion order
    current_section: str = None
    current_question: QnA = None
    
    for paragraph in document.paragraphs:
        text: str = paragraph.text
        if len(text) == 0:
            continue
        elif text.startswith(question_identifier):
            if current_question is not None:
                raise ParseError("Last question didn't have an answer."+"\n"+text)
            current_question = QnA(question=text[len(question_identifier):].strip(), answer="")
            if current_section is None:
                current_section = ""
                logger.info("no section found, starting default section:"+current_section)
                sections[current_section] = []
            sections[current_section].append(current_question)
        elif text.startswith(answer_identifier):
            if current_question is None:
                raise ParseError("Encountered two answers for same question."+"\n"+text)
            current_question.answer = text[len(answer_identifier):].strip()
            current_question = None
        else:
            current_section = text.strip()
            sections[current_section] = []
            logger.info("starting a new section:"+current_section)       
    return sections
