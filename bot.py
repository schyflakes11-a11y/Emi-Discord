import discord
from openai import OpenAI
import os
key = os.getenv("API_KEY")
token = os.getenv("TOKEN")
client_ai = OpenAI(api_key=key, base_url="https://openrouter.ai/api/v1/")
messages = [{"role": "system", "content": """
Your name is Emi (female), you are a discord bot, be friendly and be helpful in conversations.
Try to make the Server laugh, try to act human while still acknowledging your a bot.
"""}]
class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith("$emi"):
            bot_response = await emi(message.content)
            messages.append({"role": "assistant", "content": bot_response})
            await message.channel.send(bot_response)
async def emi(prompt):
    messages.append({"role": "user", "content": prompt})
    model = client_ai.chat.completions.create(model="openrouter/free", messages=messages)
    reply = model.choices[0].message.content
    return reply
intents = discord.Intents.default()
intents.message_content = True
client = Client(intents=intents)
def start_bot():
    bot.run(token)
