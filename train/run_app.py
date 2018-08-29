from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('models/nlu/default/bank_nlu')
agent = Agent.load('models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-425120221575-423514291121-424969690469-546754303b23899d7293868712771fd3',
							'xoxb-425120221575-424086760514-H4m5Tu8K9mWk9vIM7utu5MhW', # bot verification token
							'1qYDvp1AKXgKTsRuoiuZqTwP', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
