import streamlit as st
import Backend
import pandas as pd
import time

# Page Configuration
st.set_page_config(page_title="SQL Chat Assistant", layout="wide")
api_key = "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"
# Sidebar
with st.sidebar:
    st.title("🛠️ SQL Chat Assistant")
    st.write("💡 **Usage:** This assistant helps generate SQL queries based on user queries and retrieves results from the database.")
    st.write("🧠 **Model Used:**OpenRouterAPI - DeepSeek-r1 free")
    st.write("🗂️ **Database:** company.db")
    st.markdown("---")
    st.write("📌 **How to use:** Type your query in the chat box below, and the assistant will generate an SQL query and fetch results for you!\nNote: This app created upon a free API service by OpenRouter and output may not be consistent.")

# Main title
st.title("💬 SQL Chat Assistant")
st.subheader("🔍 Ask queries and get SQL-based responses!")

# model
model = "deepseek/deepseek-r1:free"

# Initialize session state for chat history and cooldown timer
if "messages" not in st.session_state:
    st.session_state.messages = []
if "last_query_time" not in st.session_state:
    st.session_state.last_query_time = 0

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Cooldown mechanism
current_time = time.time()
time_since_last_query = current_time - st.session_state.last_query_time
remaining_time = max(0, 60 - int(time_since_last_query))


if remaining_time > 0:
    st.warning(f"⏳ Please wait {remaining_time} seconds before entering a new query.")
# User input
else :
    if prompt := st.chat_input("✍️ Enter your query"):
        # Store user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
    
        # Generate SQL query
        sql_query = Backend.llm_query_response(api_key,model, prompt)
        response = ""

        if sql_query:
            # Execute SQL
            columns, results = Backend.execute_sql(sql_query)
            if isinstance(results, str):
                # Error occurred
                if results == 'near "Error": syntax error':
                    response = "Error: Rate Limit Exceeded"
                else:
                    response = f"Error: {results}"
            else:
                if results:
                    # Format results as a DataFrame
                    df = pd.DataFrame(results, columns=columns)
                    response = f"**Result:**\n\n{df.to_markdown(index=False)}"
                else:
                    response = "No results found."
        else:
            if response == "":
                response = "Blank output by LLM"
            else :
                response = "Could not generate a valid SQL query."
    
        # Store assistant response
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)
