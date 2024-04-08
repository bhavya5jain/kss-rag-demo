import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
import openai
from llama_index.core import Settings
from llama_index.embeddings.openai import OpenAIEmbedding


if __name__ == "__main__":
    os.environ['OPENAI_API_KEY'] = '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'
    openai.api_key = os.environ['OPENAI_API_KEY']
    llm = OpenAI(model="gpt-4")

    Settings.llm = llm
    Settings.embed_model = OpenAIEmbedding()

    documents = SimpleDirectoryReader(
        "data/ibm-principle-of-operations").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.set_index_id("ibm-poo")

    index.storage_context.persist("index-storage")
