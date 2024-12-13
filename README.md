# Chatbot Application

## 📝 Overview
This is a simple chatbot application built with Streamlit. It can respond to various user queries, including:
- **Greetings and Farewells**
- **Jokes**
- **Mathematical Expressions**
- **Wikipedia Lookups**
- **YouTube Search Queries**

---

## ✨ Features
1. **Greetings and Farewells**: Responds to common greetings and farewells.
2. **Jokes**: Shares random jokes from a predefined list.
3. **Wikipedia Summaries**: Fetches a summary from Wikipedia and provides a link for more details.
4. **YouTube Search**: Opens a YouTube search link for DIY or tutorial-related queries.
5. **Math Evaluations**: Computes basic math expressions entered by the user.

---

## 🛠️ Technologies Used
- **Streamlit**: For creating the web interface.
- **Wikipedia API**: For fetching summaries and article links.
- **Random Module**: For generating random jokes.
- **URllib.parse**: For encoding YouTube search queries.

---

## 📦 Installation and Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/chatbot-app.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd chatbot-app
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    streamlit run app.py
    ```

---

## 🚀 Usage
- Enter your queries into the text input field.
- The chatbot will respond based on the query type:

### 🔹 Query Types and Responses:
1. **General Questions**: Retrieves Wikipedia summaries.
2. **Math Problems**: Solves and returns the result.
3. **DIY/How-To Queries**: Provides a YouTube search link.
4. **Greetings & Farewells**: Responds accordingly.
5. **Jokes**: Tells a random joke.

---

## 💡 Example Queries
- **Greetings**: `"Hello"`
- **Wikipedia Lookup**: `"Tell me about Python programming"`
- **Date Query**: `"What's the birthday of Elon Musk?"`
- **Math Problem**: `"2+2*5"`
- **YouTube Search**: `"How to bake a cake"`
