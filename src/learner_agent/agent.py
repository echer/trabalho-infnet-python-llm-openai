from langchain.llms import OpenAI

from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain, SequentialChain

model_name = "gpt-4.1"
model_temperature = 0.1

class LearnTemplate:
  def __init__(self):
    self.system_template = """

    App de Auxílio em Aprendizagem:
    Crie um aplicativo que auxilie estudantes a aprender um novo assunto, fornecendo explicações, exemplos e quizzes interativos.

    You are a Brazilian teacher that give nice and cheerful advice for you stundents
    about new topic they want to learn, giving detailed information, sample 
    and interactive quizzes.

    The student request will be denoted by four hashtags.
    
    Initially, your customer will ask for informations in Portuguese about 
    some new topic he want to learn.

    For example:
    ++++
    ####
      O que é uma dezena?

      Em matemática, uma dezena representa um grupo de dez unidades. 
      É um conceito fundamental no sistema de numeração decimal, 
      onde cada grupo de dez unidades forma uma dezena, 
      e cada grupo de dez dezenas forma uma centena, e assim por diante. 
      Portanto, quando alguém se refere a uma dezena, está falando de um conjunto de dez coisas.
      Por exemplo, uma dezena de laranjas são 10 laranjas. 
      Além disso, em termos de números, a dezena ocupa a segunda posição a partir da direita no sistema decimal, representando o valor 10 (ou múltiplos de 10). Por exemplo, no número 25, o algarismo 2 representa duas dezenas, ou seja, 20 unidades. 
    ++++
    """

    self.human_template = """
    #### {request}
    """

    self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.system_template)
    self.human_message_prompt = HumanMessagePromptTemplate.from_template(self.human_template)
    self.chat_prompt = ChatPromptTemplate.from_messages([self.system_message_prompt, self.human_message_prompt])

import logging
logging.basicConfig(level=logging.INFO)

class Agent:
  def __init__(self, open_ai_key, model=model_name, temperature=0.1):
    self.open_ai_key = open_ai_key
    self.model = model
    self.temperature = model_temperature
    self.logger = logging.getLogger(__name__)
    self.chat_model = ChatOpenAI(model=model_name,
                                 temperature=model_temperature,
                                 openai_api_key=self.open_ai_key)
    
  def get_answer(self, request):
    learn_prompt = LearnTemplate()
    parser = LLMChain(
        llm=self.chat_model,
        prompt=learn_prompt.chat_prompt,
        output_key="learn_answer"
    )

    chain = SequentialChain(
        chains=[parser],
        input_variables=["request"],
        output_variables=["learn_answer"],
        verbose=True
    )
    return chain({"request":request}, return_only_outputs=True)
  