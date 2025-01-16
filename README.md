# Cocktail Advisor Chat
# IMPORTANT!!!
https://www.loom.com/share/e16d8c6c1e5541f59ead7fa901d78577?sid=ce0121e9-7c4f-4b26-b8e6-fa0b1001e9b0

Welcome to **Cocktail Advisor Chat**, an AI-powered application that recommends cocktails based on your ingredient preferences! This app leverages advanced machine learning models to help you discover exciting cocktails, whether you're looking for something classic or new, alcoholic or non-alcoholic. 

## Features

- **Cocktail Recommendations**: Get personalized cocktail suggestions based on your ingredients or preferences.
- **AI-Powered Search**: Uses LangChain and OpenAI's GPT models to generate recommendations.
- **ChromaDB Integration**: Stores cocktail data in a vector database for efficient search and retrieval.
- **User-Friendly Interface**: Built with Streamlit for easy interaction and fast results.

## Requirements

Before running the application, make sure you have the following installed:

- Python 3.7 or higher
- `pip` (Python's package installer)

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/cocktail-advisor-chat.git
    cd cocktail-advisor-chat
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables:
    - Create a `.env` file in the root of the project and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your-openai-api-key-here
    ```

4. Download the cocktail data file `final_cocktails.csv` and place it in the project directory. This file should contain information such as cocktail names, ingredients, instructions, and more.

## Running the Application

To run the app locally:

1. Open a terminal or command prompt.
2. Navigate to the project directory and run the following command:
    ```bash
    streamlit run app.py
    ```

3. The app should open in your default web browser, where you can start searching for cocktails by entering your preferences in the sidebar.

## How It Works

1. **Initialize ChromaDB**: When the app starts, it loads cocktail data into a persistent ChromaDB collection if it's not already stored.
2. **Search Cocktails**: When a user enters a query, the app uses ChromaDB to find the most relevant cocktails based on their query. The results are processed using a LangChain-powered AI model (OpenAI's GPT-4) to generate a response with recommendations.
3. **Display Results**: The recommended cocktails are displayed on the main page, with detailed information about each cocktail.

## Technologies Used

- **Streamlit**: For building the user interface.
- **LangChain**: To manage the AI model prompts and response generation.
- **OpenAI GPT-4**: Used to generate cocktail recommendations.
- **ChromaDB**: A vector database for storing and retrieving cocktail data.
- **Pandas**: For handling and processing the cocktail dataset.

## Future Enhancements

- **User Memories**: In the future, the app can be extended to store user memories. This feature would allow users to save their favorite ingredients and cocktails, which could then be used to provide even more personalized recommendations over time. As users interact with the app and share their preferences, the system could remember and suggest cocktails based on their history, helping refine recommendations for future visits.

I'm still working on it!!!!
