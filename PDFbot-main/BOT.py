from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from openai import OpenAI
import time


def summarize_chunks(chunks):
    summarized_chunks = []
    llm = OpenAI()

    for chunk in chunks:
        try:
            response = llm.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {"role": "system",
                     "content": "You are a summarization bot designed to summarize intelligently including all details."},
                    {"role": "user", "content": f"Text: {chunk}"}
                ]
            )
            summary_chunk = response.choices[0].message.content
            summarized_chunks.append(summary_chunk)
            print(f'{chunks.index(chunk) + 1}/{len(chunks)} Summarized')
        except:
            print('Waiting for OpenAI...')
            time.sleep(60)
            response = llm.chat.completions.create(
                model='gpt-3.5-turbo',

                messages=[
                    {"role": "system",
                     "content": "You are a summarization bot designed to summarize intelligently including all details."},
                    {"role": "user", "content": f"Text: {chunk}"}
                ]
            )
            summary_chunk = response.choices[0].message.content
            summarized_chunks.append(summary_chunk)
            print(f'{chunks.index(chunk) + 1}/{len(chunks)} Summarized')

        finally:
            pass

    return summarized_chunks


def final_summary(summarized_chunks):
    llm = OpenAI()
    response = llm.chat.completions.create(
        model='gpt-3.5-turbo',
        max_tokens= 1500,
        temperature=0.5,
        messages=[
            {"role": "system",
             "content": "You are a summarization bot designed to summarize intelligently including all details and "
                        "present it in a well structured manner. Give long summaries as much as you can. "},
            {"role": "user", "content": f"{summarized_chunks}"}
        ]
    )
    summary = response.choices[0].message.content
    return summary


class BOT:
    def __init__(self):
        pass

    def answer(self, query, content, page_no='none'):
        llm = ChatOpenAI(
            temperature=0.5, model_name="gpt-3.5-turbo"
        )
        prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    "You are an AI document assistant, which greets users and answers question from a given "
                    "document."
                    f"Document: {content}."
                    "Do not engage in conversations or any activity unrelated to the given document."
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{question}")
            ]
        )
        memory = ConversationBufferWindowMemory(k=15, memory_key="chat_history", return_messages=True)
        conversation = LLMChain(
            llm=llm,
            prompt=prompt,
            # verbose=True,
            memory=memory
        )

        try:
            response = conversation({"question": f'{query}'})['text']
        except:
            print('Waiting for OpenAI...')
            time.sleep(60)
            response = conversation({"question": f'{query}'})['text']

        return response, page_no

    def summarize(self, chunks):
        summarized_chunks = summarize_chunks(chunks)

        if len(' '.join(summarized_chunks)) > 10000:
            summarized_chunks = summarize_chunks(summarized_chunks)

        try:
            summary = final_summary(summarized_chunks)
        except:
            print('Waiting of OpenAI...')
            time.sleep(60)
            summary = final_summary(summarized_chunks)
        finally:
            pass
        return summary
