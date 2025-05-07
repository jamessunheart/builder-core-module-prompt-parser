# prompt_parser module

def run(instruction: str) -> dict:
    """
    Parse a user instruction and extract the intended action and relevant parameters.
    """
    import re

    # Basic intent parsing logic (expandable)
    instruction = instruction.strip().lower()
    if 'create' in instruction or 'generate' in instruction:
        action = 'create'
    elif 'analyze' in instruction:
        action = 'analyze'
    elif 'test' in instruction:
        action = 'test'
    elif 'optimize' in instruction:
        action = 'optimize'
    else:
        action = 'unknown'

    # Simple parameter extraction using regex
    params = re.findall(r"\b\w+\b", instruction)

    return {
        'action': action,
        'params': params,
        'raw': instruction
    }