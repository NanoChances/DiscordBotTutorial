# Discord Bot Guide
![Discord Bot](Preview.jpg/)

Why is he so annoyed?
## Overview
This guide will help you set up a Discord bot that uses a local language model to respond to messages. The bot is built using Python and the `discord.py` library, and it leverages models from Hugging Face.

Created by [Nano Chances](https://www.youtube.com/@NanoChances). Tutorial video TBD.

## File Structure
| File | Description |
|------|-------------|
| `index.py` | Main bot code. |
| `requirements.txt` | List of required Python libraries. |
| `.env` | Environment variables (e.g., Discord bot token). |
| `readme.md` | This guide. |
| `venv/` | Virtual environment folder (created during setup). |

## Setup Instructions
Download Python `3.10.6` from [python.org](https://www.python.org/downloads/release/python-3106/).

Make sure to check the box that says `Add Python to PATH` during installation.

You can find required libraries in `requirements.txt`.

## Discord Dev Portal
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on "New Application" and give it a name.
3. Navigate to the "Bot" tab and reset the token. Copy this token and save it in the `.env` file as `DISCORD_BOT_TOKEN=your_token_here`.
4. Scroll down to "Privileged Gateway Intents" and enable the "Message Content Intent".
5. Go to the "OAuth2" tab, then "URL Generator". Under "Scopes", select `bot`. Under "Bot Permissions", select `Send Messages`. Copy the generated URL and open it in your browser to invite the bot to your server.
6. Run the bot using `python index.py` in your terminal and check if it comes online in your server.

## Opening a Terminal
You will need to open a terminal to run the commands below.

Navigate to your project folder in File Explorer. Click on the address bar, type `cmd`, and press Enter. This will open a command prompt in that directory. You can also use:
```bash
cd [path to your project folder]
# For example:
cd C:\Dev\Discord\MyBot
```

## Create a virtual environment:
Create a virtual environment named `venv`:
```bash
python -m venv venv
```

Activate the virtual environment:
```bash
venv\Scripts\activate
```

Install the required packages:
```bash
pip install -r requirements.txt
```

Once you've done it once, you'll only need to activate the virtual environment in the future. You'll know it's activated when you see `(venv)` in your terminal.

## Configuration
Create a `.env` file in the root directory and add your Discord bot token:
```env
DISCORD_BOT_TOKEN=your_token_here
```

## Running the Bot
Run the bot using:
```bash
python index.py
```

## Common Issues
| Issue | Solution |
|-------|----------|
| Python not recognized | Ensure Python is installed and added to your system PATH. You can verify by running `python --version` in your terminal. |
| No such file or directory | Make sure you're in the correct directory where `index.py` is located. Use `cd [path to your project folder]` to navigate there. |
| Intents not enabled | Go to the Discord Developer Portal, select your bot, navigate to the "Bot" section, and enable the necessary intents (e.g., "Message Content Intent"). |
| Token not working | Double-check that you've copied the token correctly from the Discord Developer Portal and that it's correctly set in your `.env` file. |
| Bot not responding | Ensure the bot is online in your server and that it has the necessary permissions to read and send messages. |
| Model is too large | Try using a smaller model like TinyLlama 1.1B. |
| Llama-cpp fails to install | Make sure you have a C++ build environment set up. On Windows, you can install the [Build Tools for Visual Studio](https://visualstudio.microsoft.com/visual-cpp-build-tools/). |

## Changing the Model
To change the model, modify the `MODEL_PATH` variable in `index.py` to point to your desired model. For example:
```python
llama_model_path = hf_hub_download(
    repo_id="TheBloke/Mistral-7B-Instruct-v0.2-GGUF",
    filename="mistral-7b-instruct-v0.2.Q4_K_M.gguf"
)
```
Different models may have different capabilities and performance characteristics, so choose one that fits your needs. Basically anything in GGUF format should work, some might require logging in to Hugging Face. Models are mainly limited by your GPU VRAM.

Example models:
| Model | Description |
|-------|-------------|
| [Mistral 7B Instruct v0.2 GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF) | A basic model able to run on basic laptops. |
| [TinyLlama 1.1B GGUF](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF) | Really small weight model for quick responses. Doesn't give good responses. |
