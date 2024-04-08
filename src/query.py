import os
import json
from llama_index.llms.openai import OpenAI
import openai
from llama_index.core import Settings
from llama_index.core import load_index_from_storage
from llama_index.core.storage import StorageContext
import re
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = os.environ['OPENAI_API_KEY']


def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def load_index():
    global index

    storage_context = StorageContext.from_defaults(
        persist_dir="index-storage")
    index = load_index_from_storage(storage_context, index_id="ibm-poo")


def define_llm():
    global llm

    response_template = str(load_json("response-template/response.json"))

    llm = OpenAI(
        model="gpt-3.5-turbo",
        temperature=0.5,
        system_prompt=f"""You are an IBM assembler expert.
            Your job is to explain the IBM assembler instruction that will be provided.
            Assume that all the following questions are related to IBM assembler operations.
            Relevant operation's documentation will be provided.
            Give response strictly in json format in the template: {response_template}"""
    )


@app.route('/')
def health_check():
    return 'OK'


@app.route('/assembler_description')
def assembler_instruction_description():
    instruction = request.args.get('instruction')

    user_prompt = f"""
        Given the relevant IBM assembler documentation provided, 
        explain the instruction: "{instruction}"."""

    Settings.llm = llm

    query_engine = index.as_query_engine()
    response = query_engine.query(user_prompt)

    res = json.loads(str(response).replace("'", '"'))

    if hasattr(response, 'metadata'):
        document_info = str(response.metadata)
        find = re.findall(
            r"'page_label': '[^']*', 'file_name': '[^']*'", document_info)

        res["contextInformation"] = str(find)

    return res


if __name__ == "__main__":
    load_index()
    define_llm()
    app.run(host="0.0.0.0", port=5000)
