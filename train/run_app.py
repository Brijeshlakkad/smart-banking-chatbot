from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter

# load your trained agent
agent = Agent.load("models/dialogue", interpreter=RegexInterpreter())

input_channel = SlackInput(
            slack_token="xoxb-425120221575-424086760514-1QebIV5pDMdQjLyb1YA6Hceh",
            # this is the `bot_user_o_auth_access_token`
			slack_channel="example"
            # the name of your channel to which the bot posts (optional)
    )
# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel], 5004, serve_forever=True)
