from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from Friday_voice import gen_audio
from Friday_ears import listen
# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    'Friday',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ])
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')
#Note had to change to full_load
print('Type something to begin...')
iteration = 0
# The following loop will execute each time the user enters input
while True:
    try:
        user_input = listen()
        print(user_input)
        bot_response = bot.get_response(user_input)
        print(bot_response)
        generate = input("Generate? Y/N:")
        if generate == 'Y':
            gen_audio(str(bot_response), iteration)
            iteration += 1
        elif generate == 'N':
            overwrite = input('Override? Y/N:')
            if overwrite == 'Y':
                gen_audio(str(input('Type input here:')), iteration)
                iteration += 1
        print('Type something to begin...') 

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
