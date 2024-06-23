from openai import OpenAI

class GPT3Chatbot:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def chat_with_gpt(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()

    def start_chat(self, initial_prompt):
        response = self.chat_with_gpt(initial_prompt)
        print("Chatbot: ", response)
        return response

if __name__ == "__main__":
    bot = GPT3Chatbot(api_key='xxxxxxxxxx')
    bot.start_chat()
