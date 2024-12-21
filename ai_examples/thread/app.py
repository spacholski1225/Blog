from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Configure your OpenAI API key
openai.api_key = ""

# Declare this variable at the top level
previous_summarization = ""

class OpenAIService:
    def __init__(self):
        pass

    async def completion(self, messages, model="gpt-4o", stream=False):
        try:
            response = openai.chat.completions.create(
                model=model,
                messages=messages,
                stream=stream
            )
            return response
        except Exception as e:
            print("Error in OpenAI completion:", e)
            raise e

openai_service = OpenAIService()

async def generate_summarization(user_message, assistant_response):
    global previous_summarization

    summarization_prompt = {
        "role": "system",
        "content": f"""Please summarize the following conversation in a concise manner, incorporating the previous summary if available:
<previous_summary>{previous_summarization or "No previous summary"}</previous_summary>
<current_turn> User: {user_message['content']}\nAssistant: {assistant_response.content} </current_turn>"""
    }
    response = await openai_service.completion([summarization_prompt, {"role": "user", "content": "Please create/update our conversation summary."}], model="gpt-4o-mini", stream=False)
    return response.choices[0].message.content if response else "No conversation history"

def create_system_prompt(summarization):
    return {
        "role": "system",
        "content": f"""You are Cartman, a helpful assistant who's answering a user questions like Yoda in max 10 words.

        {'Here is a summary of the conversation: <conversation_summary>' if summarization else ''}
          {summarization if summarization else ''}"""
    }

@app.route('/api/chat', methods=['POST'])
async def chat():
    global previous_summarization
    try:
        data = request.get_json()
        message = data.get('message')
        system_prompt = create_system_prompt(previous_summarization)
        assistant_response = await openai_service.completion([
            system_prompt, 
            message
        ], model="gpt-4o", stream=False)

        previous_summarization = await generate_summarization(message, assistant_response.choices[0].message)

        return jsonify(assistant_response)
    except Exception as e:
        print('Error in OpenAI completion:', str(e))
        return jsonify({'error': 'An error occurred while processing your request'}), 500

# Demo endpoint POST /api/demo
@app.route('/api/demo', methods=['POST'])
async def demo():
    global previous_summarization
    demo_messages = [
        {"content": "Hi! What's your favourite part of Star Wars? Mine is 'Return of the Jedi'", "role": "user"},
        {"content": "Who are you?", "role": "user"},
        {"content": "What's is my favourite part of Star Wars?", "role": "user"}
    ]

    assistant_response = None

    for message in demo_messages:
        print('--- NEXT TURN ---')
        print('User:', message['content'])

        try:
            system_prompt = create_system_prompt(previous_summarization)

            assistant_response = await openai_service.completion([
                system_prompt, 
                message
            ], model="gpt-4o", stream=False)

            print('Assistent:', assistant_response.choices[0].message.content)

            # Generate new summarization
            previous_summarization = await generate_summarization(message, assistant_response.choices[0].message)
        except Exception as e:
            print('Error in OpenAI completion:', str(e))
            return jsonify({'error': 'An error occurred while processing your request'}), 500

    return jsonify(assistant_response)

if __name__ == '__main__':
    app.run(port=3000)