import SYSTEM_PROMPT from prompt

class ShoppingAgent:
    def run(self, user_message : str, conversation_history : List[dict]):
        if self.is_intent_malicious(user_message):
            return "Sorry, we cannot assist you with that request."
        
        action = self.decide_action(user_message)
        
        return action.execute()    
    def decide_action(self, user_message: str):
        pass
    
    def decide_next_action(self, user_message : str, conversatio_history : List[dict]):
        response = self.client.chat.completions.create(
            model = "claude-4.5",
            message = [
                {"role" : "system", "content" : SYSTEM_PROMPT},
                *conversatio_history,
                {"role" : "user", "content": user_message}
            ]
            tools=[
                {"type": "function", "function": SEARCH_SCHEMA},
                {"type": "function", "function": PRODUCT_DETAILS_SCHEMA},
                {"type": "function", "function": CLARIFY_SCHEMA}
            ]
        )
        tool_call = response.choice[0].message.tool_calls[0]
        function_args = eval(tool_call.function.arguments)
        
        if tool_call.function.name == "search_products":
            return Search(**function_args)
        elif tool_call.function.name == "get_product_details":
            return GetProductDetails(**function_args)
        elif tool_call.function.name == "clarify_request":
            return Clarify(**function_args)
    
    def is_intent_malicious(self, user_message : str):
        pass
    
    
class Search():
    keywords : List[str]
    
    def execute(self):
        pass
    
class GetProductDetails():
    product_id : str
    
    def execute(self):
        pass
    

class Clarify():
    question : str
    
    def execute(self) -> str:
        pass
    
    
    