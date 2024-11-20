AI Voice Bot
This is an AI-based Voice Bot that recognizes voice commands and performs various tasks such as opening applications, creating files, or locking the laptop.
Features
- **Voice Recognition**: Uses the Vosk API to process voice commands.
- **Text-to-Speech**: Provides audio feedback using `pyttsx3`.
- **GUI Interface**: Displays a simple GUI with an owl icon that changes color during operation.
- **Intent Handling**: Handles various intents such as:
  - Greeting
  - Opening Chrome
  - Opening Camera
  - Locking the laptop
  - Creating a file
Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Victor-Dhrubo/new-folder.git
   ```
2. Install dependencies:
   ```bash
   pip install pyttsx3 vosk pyaudio tkinter
   ```
3. Download and extract the [Vosk model](https://alphacephei.com/vosk/models) and place it in the project directory.
Usage
Run the bot with the following command:
```bash
python AI_voice_bot.py
```
Once running, the bot will start listening for your commands.
Files
- **AI_voice_bot.py**: The main script for the bot.
- **intents.json**: Contains intents and their corresponding actions and responses.
Future Improvements
- Add more commands and intents.
- Improve the GUI design.
- Implement error handling for missing dependencies.
License
This project is open-source and available under the [MIT License](LICENSE).
