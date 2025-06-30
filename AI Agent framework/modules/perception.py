def parse(text: str) -> dict:
    """
    Purpose: trim any whitespace and wrap the user input in a dict 
    allows us to extend parsing later
    """
    cleaned = text.strip()
    return {"raw":cleaned}  
