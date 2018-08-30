from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('models/nlu/default/bank_nlu')
agent = Agent.load('models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-425120221575-423514291121-425486176225-ef2c6b704e441593c4291c3f35fb16b3',
							'xoxb-425120221575-424086760514-gCS7A1vtLDOzAfG2JYZ6v4uA', # bot verification token
							'1qYDvp1AKXgKTsRuoiuZqTwP', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
