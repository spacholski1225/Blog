import openai

class OpenAIService:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    async def completion(self, messages, model="gpt-4", stream=False):
        try:
            response = openai.ChatCompletion.create(
                messages=messages,
                model=model,
                stream=stream
            )

            if stream:
                return response
            else:
                return response['choices'][0]['message']['content']
        
        except Exception as e:
            print("Error in OpenAI completion:", e)
            raise e