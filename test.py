import streamlit as st
import pandas as pd
import chromadb
import uuid
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate


# Load environment variables
load_dotenv()


# Initialize ChromaDB
def initialize_chromadb(file_path="final_cocktails.csv", db_path="vectorstore"):
    data = pd.read_csv(file_path)
    chroma_client = chromadb.PersistentClient(db_path)
    collection = chroma_client.get_or_create_collection(name="cocktails")

    # Load data into vector DB if not already present
    if not collection.count():
        for _, row in data.iterrows():
            collection.add(
                documents=[row["name"]],
                metadatas={
                    "alcoholic": row["alcoholic"],
                    "category": row["category"],
                    "glassType": row["glassType"],
                    "instructions": row["instructions"],
                    "drinkThumbnail": row["drinkThumbnail"],
                    "ingredients": row["ingredients"],
                    "ingredientMeasures": row["ingredientMeasures"],
                    "text": row["text"]
                },
                ids=[str(uuid.uuid4())]
            )
    return collection


# Search for cocktails based on query
def search_cocktails(query, collection=None, k=5):
    """Find similar cocktails based on ingredients or preferences."""
    if collection is None:
        collection = initialize_chromadb()

    results = collection.query(query_texts=query, n_results=k)
    cocktails = results.get('metadatas', [])
    prompt = PromptTemplate.from_template(
        """
        ### COCKTAIL DATABASE QUERY RESULT:
        {cocktails}

        ### INSTRUCTIONS FOR AI:
        You are a knowledgeable cocktail expert. Based on the user's ingredient preferences, suggest the best matching cocktails. If the user asks about specific ingredients, provide relevant insights. If they request non-alcoholic options, highlight suitable alternatives.
        Use the provided dataset to generate informed recommendations.

        ### FORMAT FOR RECOMMENDED COCKTAILS:
        Provide responses in a friendly and engaging manner. Include cocktail names, key ingredients, and a brief description. If applicable, suggest an ideal glass type and any unique preparation techniques.
        """
    )
    llm = ChatOpenAI(model_name="gpt-4o-mini")

    # Chain the LLM with the prompt
    chain = prompt | llm
    response = chain.invoke({"cocktails": cocktails})
    return response


# Streamlit App
st.title("Cocktail Advisor Chat")

st.sidebar.header("Cocktail Search")
st.sidebar.write("Enter your preferences to get cocktail recommendations.")

# Initialize ChromaDB
collection = initialize_chromadb()

# Input query
user_query = st.sidebar.text_input("Search for cocktails", "")

if user_query:
    st.sidebar.write("Searching for cocktails...")
    try:
        result = search_cocktails(query=user_query, collection=collection)
        st.write("### Recommended Cocktails")
        st.write(result.content)
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.sidebar.write("Enter a query to start.")

st.write("### About")
st.write(
    "This app helps you discover amazing cocktails based on your preferences using AI-powered recommendations. Enter a query in the sidebar to get started!")
