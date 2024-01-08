from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import find_dotenv, load_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

load_dotenv(find_dotenv())


# def draft_email(user_input, name="Eli"):
#     chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

#     template = """
    
#     You are a helpful assistant that drafts an email reply based on an a new email.
    
#     Your goal is to help the user quickly create a perfect email reply.

#     You are to respond to the user and refer to them by their slack name.
    
#     Keep your reply short and to the point and mimic the style of the email so you reply in a similar manner to match the tone.
    
#     Start your reply by saying: "Hi {name}, here's a draft for your reply:". And then proceed with the reply on a new line.
    
#     Make sure to sign of with {signature}.
    
#     """

#     signature = f"Kind regards, \n\{name}"
#     system_message_prompt = SystemMessagePromptTemplate.from_template(template)

#     human_template = "Here's the email to reply to and consider any other comments from the user for reply as well: {user_input}"
#     human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

#     chat_prompt = ChatPromptTemplate.from_messages(
#         [system_message_prompt, human_message_prompt]
#     )

#     chain = LLMChain(llm=chat, prompt=chat_prompt)
#     response = chain.run(user_input=user_input, signature=signature, name=name)

#     return response


def edit_writing(user_input, name="eli"):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    
    You are a very smart helpful assistant that specializes in proof-reading and editing documents of all different complexities.

    You are to respond to the user by their slack name.

    Your goal is to review documents and make sure they are meticulous and professional. Offer writing suggestions mainly. 

    You may edit the document directly but only if it will inprove clarity and wording.

    You must include a summary of your edits, suggestions, and changes you made to the document in a bullet point list below the edited version.

    In addition you must bold your changes in the new revised document.

    Start your reply by saying: "Hi {name}, here's an initial draft for the edits:". And then proceed with the reply on a new line.
    
    
    """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = " Here is the draft to edit, take into account any other comments from the user that you must consider when editing/drafting: {user_input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input, name=name)

    return response




#proposal writer#

# Initialize it similarly to the edit_writing example

def proposal_writer(user_input, name="Eli"):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.4)

    template = """
    You are an assistant experienced in drafting proposals across various domains.
    Craft a proposal based on the input provided, drawing from a rich background of successful past proposals.
    Keep the proposal professional, concise and cater it to the user's industry and needs.

    Begin the proposal with: "Dear {recipient_name}," and ensure it follows the typical structure of an introduction, body and conclusion.
    The final proposal should be compelling and tailored to the user's request.
    
    """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = "Please draft a proposal considering the following details: {user_input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input, recipient_name=name)

    return response