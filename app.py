# Import necessary libraries
import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]

if not api_key:
    st.error("API key not found! Set it in Streamlit secrets.")
    
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit App layout
st.title("AI-Powered Code Assistant")
st.markdown("Get AI-powered assistance for various programming languages!")

# Sidebar - Feature Selection
st.sidebar.header("Select Feature")
feature = st.sidebar.selectbox(
    "Choose what you need help with:",
    ["Code Suggestions", "Code Debugging", "Reusable Code Snippets", "General Code Query"]
)

# Sidebar - Language Selection
st.sidebar.header("Select Programming Language")
language = st.sidebar.selectbox(
    "Select the programming language:",
    ["Python", "JavaScript", "Java", "C++", "C#", "Go", "Ruby", "Swift", "PHP", "TypeScript", "Rust", "Kotlin", "SQL", "Other"]
)

# Input box for user to type code or query
user_input = st.text_area("Enter your code or query here:")

# Button to trigger the AI response
if st.button("Get AI Suggestions"):

    # Generate response based on selected feature
    if feature == "Code Suggestions":
        prompt = f"Suggest code completion for the following {language} code:\n{user_input}"
    elif feature == "Code Debugging":
        prompt = f"Find and fix the bugs in the following {language} code:\n{user_input}"
    elif feature == "Reusable Code Snippets":
        prompt = f"Provide reusable {language} code snippets related to: {user_input}"
    else:
        prompt = f"Provide an explanation or advice on this {language} code/query:\n{user_input}"

    # Get response from Gemini AI model
    response = model.generate_content(prompt)

    # Display AI's response in the app
    st.subheader("AI's Response:")
    st.code(response.text, language=language.lower())  # Syntax highlighting based on selected language

# Footer
st.markdown("---")
st.markdown("Powered by **Streamlit** and **Google Gemini AI**")
