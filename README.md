# Minor-Project
Smart Banking Chat Bot- This is an AI based project which uses several ML algorithms for Natural Language Understanding which identifies intent and entities from user issues and generates dialogue.

This project can help Banks to add chatbot in their web-application, so that customer can ask question to chatbot to Banks without visiting to Bank.

# Requirements
  - Python (v3.6.3) and Libraries required for AI and Natural Language Processing(NLP)
  - Rasa Core (v0.11.12)
  - Rasa NLU (v0.13.7)
  - Bootstrap (v3.3.7)
  - AngularJS (v1.6.4)
  - jQuery (v1.10.2)
  - SQL Server 2014
  - PHP (v5.6.32)
 
To install database with data, we have added sql file in repostory.
To train model,
  1. go to train directory
    - cd train
  2. run command to train nlu which actually understands natural langauge examples given in training_data.json which have classfied
    - python Bank-bot.py train-nlu
  3. run command to train core which predicts actions using training data given in stories.md file
    - python Bank-bot.py train-nlu
  4. to train model online, run (using this we can have more data of predicting action which makes model more accurate :) )
    - $ python -m rasa_core_sdk.endpoint --actions actions & python -m rasa_core.train --online -o models/dialogue -u models/nlu/default/bank_nlu  -d bank_domain.yml -s data/stories.md --endpoints endpoints.yml --batch_size 500 --epochs 200 --history 15 --validation_split 0.2 --nlu_threshold 0.2 --core_threshold 0.2 --fallback_action_name action_fallback
  5. And to finally run bot, use
    - $ python -m rasa_core.run --enable_api  -d models/dialogue -u models/nlu/default/bank_nlu --endpoints endpoints.yml 
    - $ python -m rasa_core_sdk.endpoint --actions actions
    - which have to run both in different terminals
  
