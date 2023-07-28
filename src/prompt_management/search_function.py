```python
from typing import List
from prompt_management.prompt_schemas import PromptSchema

def search_prompts(query: str, prompts: List[PromptSchema]) -> List[PromptSchema]:
    """
    Function to search through the prompts based on the query.
    Args:
    query : str : search query
    prompts : List[PromptSchema] : list of prompts

    Returns:
    List[PromptSchema] : list of prompts that match the query
    """
    return [prompt for prompt in prompts if query.lower() in prompt.text.lower()]
```