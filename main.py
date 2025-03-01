import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
from default_answers import DEFAULT_ANSWERS

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_ai_response(question, role):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are an expert AI assistant specializing in APIs, focusing on the perspective of a {role}. Provide a comprehensive, detailed, and actionable response."},
                {"role": "user", "content": question}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {str(e)}"

def main():
    # Set page config to wide mode
    st.set_page_config(layout="wide")

    # Custom CSS for enhanced styling
    st.markdown("""
    <style>
    .main-title {
        font-size: 2.8em;
        color: #2C3E50;
        text-align: center;
        margin-bottom: 50px;
        padding: 30px;
        border-bottom: 2px solid #eee;
    }
    .section-heading {
        font-size: 1.8em;
        color: #2C3E50;
        margin: 40px 0 30px 0;
        padding-bottom: 15px;
        border-bottom: 1px solid #eee;
    }
    .answer-box {
        background-color: white;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 35px;
        margin: 35px 0;
        line-height: 1.8;
        font-size: 1.1em;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .answer-box p {
        margin-bottom: 1em;
    }
    .answer-box ul, .answer-box ol {
        margin: 1em 0;
        padding-left: 2em;
    }
    .answer-box li {
        margin: 0.5em 0;
    }
    .answer-box h1, .answer-box h2, .answer-box h3 {
        margin: 1.5em 0 1em 0;
        color: #2C3E50;
    }
    .answer-box code {
        background: #f8f9fa;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 0.9em;
        color: #e83e8c;
    }
    .answer-box pre {
        background: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        overflow-x: auto;
        margin: 1em 0;
    }
    .sidebar-title {
        color: #2C3E50;
        font-weight: bold;
        margin: 0 0 10px 0;
        padding: 10px;
        background: #f8f9fa;
        border-radius: 5px;
        font-size: 1.1em;
    }
    .sidebar-link {
        color: #3498DB;
        text-decoration: none;
        font-size: 1em;
        padding: 5px 10px;
        display: block;
        margin: 0;
    }
    .sidebar-link:hover {
        color: #2980B9;
        background: #f1f1f1;
    }
    .stTextArea textarea {
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        padding: 25px;
        font-size: 1.1em;
        min-height: 200px;
        margin: 20px 0;
    }
    .stTextArea textarea:focus {
        border-color: #3498DB;
        box-shadow: 0 0 0 1px #3498DB;
    }
    .stButton > button {
        background-color: #3498DB;
        color: white;
        border-radius: 6px;
        padding: 15px 35px;
        font-size: 1.1em;
        font-weight: 500;
        border: none;
        transition: all 0.3s ease;
        margin: 25px 0;
    }
    .stButton > button:hover {
        background-color: #2980B9;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    st.markdown('<h1 class="main-title">API Knowledge Hub 🚀</h1>', unsafe_allow_html=True)

    # Create two columns
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<h3 class="section-heading">Choose Your Role</h3>', unsafe_allow_html=True)
        selected_role = st.radio("", list(DEFAULT_ANSWERS.keys()))

        st.markdown('<h3 class="section-heading">Common Questions</h3>', unsafe_allow_html=True)
        selected_question = st.radio(" ", list(DEFAULT_ANSWERS[selected_role].keys()))

        if selected_question in DEFAULT_ANSWERS[selected_role]:
            default_answer = DEFAULT_ANSWERS[selected_role][selected_question]
            formatted_answer = default_answer.replace('\n', '<br>')
            st.markdown(f"""
            <div class="answer-box">
            {formatted_answer}
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown('<h2 class="section-heading">Ask Your Own Question</h2>', unsafe_allow_html=True)
        st.markdown(f"*Current Role: {selected_role}*")
        
        default_question = "Generate an OpenAPI Specification for managing customer data with full CRUD operations. Ensure compliance with GovTech's standards, covering authentication, security best practices, rate limiting, and versioning"
        custom_question = st.text_area("", value=default_question, height=200)
        
        if st.button("Get Insights", key="custom_question_button"):
            if custom_question:
                with st.spinner("Generating insights..."):
                    custom_response = generate_ai_response(custom_question, selected_role)
                    st.session_state.chat_history.append({
                        'question': custom_question,
                        'response': custom_response
                    })
                    st.write(f"""
                    <div class="answer-box">
                    {custom_response}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("Please enter a question")

        # Display chat history for custom questions
        if st.session_state.chat_history:
            st.markdown("")  # Add vertical space
            st.markdown('<h2 class="section-heading">Previous Questions</h2>', unsafe_allow_html=True)
            for chat in reversed(st.session_state.chat_history):
                st.markdown(f"**Q:** {chat['question']}")
                st.write(f"""
                <div class="answer-box">
                {chat['response']}
                </div>
                """, unsafe_allow_html=True)

    # Sidebar content
    st.sidebar.markdown('<div class="sidebar-title">🔍 API Resources</div>', unsafe_allow_html=True)
    
    st.sidebar.markdown("API Lifecycle")
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/api-governance-model/pages/8-lifecycle" class="sidebar-link">Lifecycle Stages</a>', unsafe_allow_html=True)
    
    st.sidebar.markdown("API Design Standards")
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/api-governance-model/pages/3-api-design" class="sidebar-link">Design Best Practices</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/api-governance-model/pages/6-versioning" class="sidebar-link">Versioning</a>', unsafe_allow_html=True)

    st.sidebar.markdown("API Development")
    st.sidebar.markdown('<a href="https://medium.com/@thirukkumaran/rapid-prototyping-of-design-first-apis-in-go-601d8833593a" class="sidebar-link">API Design-First Development</a>', unsafe_allow_html=True)

    st.sidebar.markdown("API Security")
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/api-governance-model/pages/4-security" class="sidebar-link">Security Best Practices</a>', unsafe_allow_html=True)

    st.sidebar.markdown("API Testing")
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/api-governance-model/pages/5-testing" class="sidebar-link">API Testing</a>', unsafe_allow_html=True)

    st.sidebar.markdown("API Tools")
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/data-provisioning-standards-dps-linter/" class="sidebar-link">API Linter</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()