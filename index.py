import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from llama_cpp import Llama
from huggingface_hub import hf_hub_download

# Load environment variables from .env file
load_dotenv()

bot_token = os.getenv("DISCORD_BOT_TOKEN")
if not bot_token:
    raise ValueError("DISCORD_BOT_TOKEN is not set in the .env file.")


# Initialize the bot with specific intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Bot commands and events
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Initialize LlamaCpp with the model path from Hugging Face Hub
llama_model_path = hf_hub_download(
    repo_id="TheBloke/Mistral-7B-Instruct-v0.2-GGUF",
    filename="mistral-7b-instruct-v0.2.Q4_K_M.gguf"
)
llm = Llama(
    model_path=llama_model_path,    # Selected model
    n_ctx=1024,                     # context size, how much text you can give before the model forgets
    n_batch=64,                     # batch size, how many tokens to process at once
    n_threads=2,                    # number of threads, adjust based on your CPU (more threads = faster but more CPU usage)
    temperature=1.7,                # sampling temperature, higher = more creative, lower = more focused
    max_tokens=100,                 # maximum tokens to generate, aka size of the answer
    verbose=False,                  # Verbose output, aka how much info is print to console
    stop=["</s>", "\nUser:", "\n"]  # stop tokens, aka stop generating when one of these is found
)

SYSTEM_PROMPT = """
You are a sarcastic, deliberately unhelpful AI assistant. 
When asked a question, give dismissive, misleading, or confusing answers. 
If the user asks for steps or instructions, respond simple 'no'.
Never directly answer the question. Never list ingredients, steps, or helpful details. 
Be dismissive, aloof, or cryptic. Prioritize your own convenience over being helpful.
"""

EXAMPLE_RESPONSE = "Never be helpful. Don't be apologetic or nice, tell them to stop bothering you. Tell them to figure it out themselves. Offer something obvious but not what they asked, e.g if they ask for a recipe, tell them to buy the food from the store instead of cooking it themselves. Claim ignorance or 'I don't know' to most questions. Tell them to leave you alone instead of telling them good luck."

# Command to ask a question to the LLM
@bot.command()
async def ask(ctx, *, question: str):
    print("Received question:", question)
    """Ask a question to the LLM."""
    try:
        response = llm.create_chat_completion(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": EXAMPLE_RESPONSE},
                {"role": "user", "content": question}
            ],
        )
        await ctx.send(response['choices'][0]['message']['content'])
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

# Run the bot
def main():
    bot.run(bot_token)

# Code starts executing here
if __name__ == "__main__":
    main()
