```python
class CustomInstruction:
    def __init__(self, user_id, instruction):
        self.user_id = user_id
        self.instruction = instruction

    def apply_instruction(self, chat_id):
        # This is a placeholder for the actual implementation.
        # The actual implementation would depend on the specifics of the instruction.
        pass

def create_custom_instruction(user_id, instruction):
    return CustomInstruction(user_id, instruction)

def apply_custom_instruction(custom_instruction, chat_id):
    custom_instruction.apply_instruction(chat_id)
```