class ParseError(Exception):
    """Raise when parsing fails, 
    mainly because of order issues between a question and an answer"""
    pass