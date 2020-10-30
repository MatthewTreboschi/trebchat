import unittest
import bot.py

KEY_INPUT = "input"
KEY_EXPECTED = "expected"
KEY_MESSAGE = "message"

class BotTestCase(unittest.TestCase):
    #note: my code was not designed with testing in mind, especially not unmocked.
    #for example, the !! check is done in app.py because my bot only comes up with
    #a response, not send (or not send) messages. I made my bot do an additional
    #check for the !! anyway, and come up with a unique message.
    
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "!!help",
                KEY_EXPECTED: {
                    KEY_MESSAGE: "Type !!funtranslate with a sentence for" +
                                "a translation to shakespearean english, " +
                                "!!joke for a joke, or !!STONKS for facebook stock info."
                }
            },
            {
                KEY_INPUT: "!!about",
                KEY_EXPECTED: {
                    KEY_MESSAGE: "Hello, I am MattBot, your translation assistant. " +
                                "I do make translations and jokes. type !!help for more."
                }
            },#2
            {
                KEY_INPUT: "!!joke",
                KEY_EXPECTED: {
                    KEY_MESSAGE: "why dont you see elephants hiding in trees? " +
                                "Because theyre so good at it."
                }
            },
            {
                KEY_INPUT: "!!glurb",
                KEY_EXPECTED: {
                    KEY_MESSAGE: "The command is not recognized."
                }
            },#4
            {
                KEY_INPUT: "!!jokes",
                KEY_EXPECTED: {
                    KEY_MESSAGE: "The command is not recognized."
                }
            },
            {
                KEY_INPUT: "!!help!!",
                KEY_EXPECTED: {
                    KEY_MESSAGE: "The command is not recognized."
                }
            },#6
            {
                KEY_INPUT: "help!!",
                KEY_EXPECTED: {
                    KEY_MESSAGE: "Not a command."
                }
            },
            {
                KEY_INPUT: "!?help",
                KEY_EXPECTED: {
                    KEY_MESSAGE: "Not a command."
                }
            },#8
            {
                KEY_INPUT: "!about",
                KEY_EXPECTED: {
                    KEY_MESSAGE: "Not a command."
                }
            },
            {
                KEY_INPUT: "!about",
                KEY_EXPECTED: {
                    KEY_MESSAGE: "Not a command."
                }
            }
        ]