import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
import numpy as np

pinecone.init(api_key="e5364597-8f21-4855-a69f-13068ff2d8c2", environment="gcp-starter")
embeddings = OpenAIEmbeddings(openai_api_key="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")
content = []
texts=["./resources/economia.txt",
        "./resources/ingenieria-civil.txt",
        "./resources/ingenieria-electrica.txt",
        "./resources/ingenieria-electronica.txt",
        "./resources/ingenieria-industrial.txt",
        "./resources/ingenieria-sistemas.txt"]
for txt in texts:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=15,
        length_function=len,
        add_start_index=True,
    )

    for aux in text_splitter.create_documents([open(txt, encoding="utf-8").read()]):
        content.append(aux.page_content)

data = Pinecone.from_texts(texts=content,
                           embedding=embeddings,
                           index_name="matrix1")
"""


"""