import random
import wikipedia
from urllib.parse import quote_plus
import streamlit as st

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you get if you cross a cat with a dark horse? Kitty Perry.",
    "Why don't some couples go to the gym? Because some relationships don't workout.",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "Why was the math book sad? Because it had too many problems."
]

greetings = ["hello", "hi", "hey", "greetings", "what's up"]
farewells = ["bye", "goodbye", "exit", "quit", "see you later"]

def fetch_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=3)
        page = wikipedia.page(query)
        return summary, page.url
    except wikipedia.exceptions.DisambiguationError:
        return f"Multiple entries found for '{query}'. Please be more specific.", None
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find information on that topic.", None

def open_youtube_search(query):
    encoded_query = quote_plus(query)
    search_url = f"https://www.youtube.com/results?search_query={encoded_query}"
    return search_url

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    if any(greet in user_input for greet in greetings):
        return "Hello! How can I assist you today?"
    elif any(farewell in user_input for farewell in farewells):
        return "Goodbye! Have a great day!"
    elif 'joke' in user_input:
        return random.choice(jokes)
    elif 'how to' in user_input or 'make' in user_input or 'diy' in user_input:
        youtube_url = open_youtube_search(user_input)
        return f"Here is a YouTube search for your query: [Open YouTube]({youtube_url})"
    elif 'who is' in user_input or 'what is' in user_input or 'tell me about' in user_input or 'birthday' in user_input:
        query = user_input.replace('who is', '').replace('what is', '').replace('tell me about', '').replace('birthday', '').strip()
        summary, page_url = fetch_wikipedia_summary(query)
        if page_url:
            return f"{summary}\nRead more [here]({page_url})."
        else:
            return summary
    elif any(char.isdigit() for char in user_input) and any(op in user_input for op in ['+', '-', '*', '/']):
        try:
            result = eval(user_input)
            return f"The answer is {result}"
        except Exception:
            return "Sorry, I couldn't evaluate that expression."
    return "Sorry, I didn't understand that. Please try asking something else."

def main():
    st.write("Chatbot: Hi! I'm here to assist you. How can I help?")
    user_input = st.text_input("You: ")
    if user_input:
        response = chatbot_response(user_input)
        st.write(f"Chatbot: {response}")
        if "Goodbye! Have a great day!" in response:
            st.stop()

if __name__ == "__main__":
    main()
