from django.http import HttpResponse
from django.shortcuts import render

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Initialize the ChatBot
bot = ChatBot(
    'chatbot',
    read_only=False,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Sorry, I don’t know what that means.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

# Custom training data
custom_conversations = [
    "hi",
    "Hello there!",
    "what's your name?",
    "I'm just a friendly chatbot created to help you.",
    "what is your favorite food?",
    "I love virtual cheese!",
    "do you have children?",
    "Nope, I'm just code.",
    "what's your favorite sport?",
    "Swimming is fun to watch!",
    "how are you?",
    "I'm doing great, thanks for asking!",
    "bye",
    "Goodbye! Have a nice day!"
]

# Train using ListTrainer
list_trainer = ListTrainer(bot)
list_trainer.train(custom_conversations)

# Train using built-in corpus
corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')

# Views
def home(request):
    return render(request, 'blog/index.html')

def specific(request):
    return HttpResponse("This is the specific URL")

def getResponse(request):
    user_message = request.GET.get('userMessage')
    bot_response = bot.get_response(user_message)
    return HttpResponse(str(bot_response))
