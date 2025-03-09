import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
from answers import DEFAULT_ANSWERS
import base64

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Define default questions for each role
DEFAULT_QUESTIONS = {
    "I'm an API Designer": "How can I design a RESTful API that follows best practices for resource naming, HTTP methods, and response structures?",
    "I'm an API Developer": "Generate an OpenAPI Specification for managing customer data with full CRUD operations. Ensure compliance with GovTech's standards, covering authentication, security best practices, rate limiting, and versioning.",
    "I'm an API Consumer": "What are the best practices for securely integrating with third-party APIs, including authentication, error handling, and rate limit management?",
    "I'm a Tech Lead": "How can I establish an API governance framework that balances standardization with innovation across multiple development teams?",
    "I'm a Product Manager": "What metrics and KPIs should I track to measure the success and adoption of our API products?",
    "I'm a Security Engineer": "What security controls and testing methodologies should I implement to protect our APIs from common vulnerabilities like OWASP API Top 10?",
    "I'm an API Tester": "How can I create a comprehensive API testing strategy that covers functional, performance, security, and integration testing?"
}

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
    # Initialize session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

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
        box-sizing: border-box;
        overflow-wrap: break-word;
        word-wrap: break-word;
        word-break: break-word;
        white-space: normal;
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
    .answer-box a {
        color: #3498DB;
        text-decoration: none;
        border-bottom: 1px dotted #3498DB;
        transition: all 0.2s ease;
    }
    .answer-box a:hover {
        color: #2980B9;
        border-bottom: 1px solid #2980B9;
    }
    .answer-box strong {
        color: #2C3E50;
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
    .subtitle {
        font-size: 1.3rem;
        color: #666;
        margin-bottom: 2rem;
        line-height: 2;
    }
    .full-width-container {
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
    }
    .answer-container {
        background-color: white;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 35px 50px;
        margin: 35px 0;
        line-height: 1.8;
        font-size: 1.1em;
        width: 100%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-title">API Knowledge Hub 🚀</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">API Knowledge Hub aims to provide guidance, tools, support, and a platform for connecting all personas involved in the API space across the Whole-of-Government (WoG)</p>', unsafe_allow_html=True)

    # Create two columns
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<h3 class="section-heading">Persona</h3>', unsafe_allow_html=True)
        selected_role = st.radio("", list(DEFAULT_ANSWERS.keys()))

        st.markdown('<h3 class="section-heading">You may be interested in:</h3>', unsafe_allow_html=True)
        selected_question = st.radio(" ", list(DEFAULT_ANSWERS[selected_role].keys()))

    with col2:
        st.markdown('<h3 class="section-heading">Ask your question</h3>', unsafe_allow_html=True)
        
        # Include the role in the question box
        prefixed_question = f"{selected_role}\n\n{selected_question}"
        custom_question = st.text_area("", value=prefixed_question, height=200)
        
        if st.button("Get Insights"):
            if custom_question:
                with st.spinner("Generating insights..."):
                    # Don't prepend the role to the question
                    custom_response = generate_ai_response(custom_question, selected_role)
                    st.session_state.chat_history.append({
                        'question': custom_question,
                        'response': custom_response
                    })
                    
                    # Display the response with full width
                    st.markdown(custom_response, unsafe_allow_html=True)
            else:
                st.warning("Please enter a question")

        # Display chat history for custom questions
        if st.session_state.chat_history:
            st.markdown("")  # Add vertical space
            st.markdown('<h3 class="section-heading">Previous Questions</h3>', unsafe_allow_html=True)
            
            st.markdown('<div class="full-width-container">', unsafe_allow_html=True)
            for i, chat in enumerate(reversed(st.session_state.chat_history)):
                if i < 3:  # Show only the last 3 questions
                    with st.expander(f"Q: {chat['question'][:50]}{'...' if len(chat['question']) > 50 else ''}"):
                        st.write(chat['response'])
            st.markdown('</div>', unsafe_allow_html=True)

    # Sidebar content
    st.sidebar.markdown('<div class="sidebar-title"> API Resources</div>', unsafe_allow_html=True)
    
    st.sidebar.markdown("API Management")
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/api-governance-model/pages/8-lifecycle" class="sidebar-link">API Lifecycle</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a href="https://www.developer.tech.gov.sg/products/categories/data-and-apis/apex-cloud/overview" class="sidebar-link">APEX Cloud API Gateway</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a href="https://api.apex.gov.sg/" class="sidebar-link">Discover WOG APIs</a>', unsafe_allow_html=True)
    
    st.sidebar.markdown("API Design Standards")
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/api-governance-model/pages/3-api-design" class="sidebar-link">Design Best Practices</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/api-governance-model/pages/4-security" class="sidebar-link">Security Best Practices</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a href="https://github.com/tohyongcheng/template-backend-express" class="sidebar-link">OpenAPI Templates</a>', unsafe_allow_html=True) 

    st.sidebar.markdown("API Development")
    st.sidebar.markdown('<a href="https://medium.com/@thirukkumaran/rapid-prototyping-of-design-first-apis-in-go-601d8833593a" class="sidebar-link">API Design-First Development</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/data-provisioning-standards-dps-linter/" class="sidebar-link">API Linter</a>', unsafe_allow_html=True)   

    st.sidebar.markdown("API Testing")
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/api-governance-model/pages/5-testing" class="sidebar-link">API Testing</a>', unsafe_allow_html=True)    

    st.sidebar.markdown("API Tools & Support")
    
    # Add API checklist as a link that looks like the other sidebar links
    with open('API-checklist.docx', 'rb') as file:
        checklist_bytes = file.read()
        b64 = base64.b64encode(checklist_bytes).decode()
        href = f'data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{b64}'
        st.sidebar.markdown(f'<a href="{href}" class="sidebar-link" download="API-checklist.docx">API Checklist</a>', unsafe_allow_html=True)
    
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/api-governance-model/?id=contact-us" class="sidebar-link">Ask API Community</a>', unsafe_allow_html=True)


    # Add the footer
    st.markdown("""
    <footer style="position: fixed; bottom: 0; left: 0; right: 0; width: 100%; background-color: #333; color: white; z-index: 999; padding: 8px 0; text-align: center;">
      <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <p style="font-size: 14px; margin: 0;">Built as part of the GovTech {build} Hackathon</p>
          <div style="display: flex; gap: 20px;">
            <a href="https://www.tech.gov.sg/contact-us/" style="color: white; text-decoration: none; font-size: 12px;">Contact Us</a>
            <a href="https://www.tech.gov.sg/report-vulnerability/" style="color: white; text-decoration: none; font-size: 12px;">Report Vulnerability</a>
            <a href="https://www.tech.gov.sg/privacy/" style="color: white; text-decoration: none; font-size: 12px;">Privacy Statement</a>
            <a href="https://www.tech.gov.sg/terms-of-use/" style="color: white; text-decoration: none; font-size: 12px;">Terms of Use</a>
          </div>
          <p style="font-size: 12px; margin: 0;"> 2025 Government Technology Agency of Singapore | GovTech</p>
        </div>
      </div>
    </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()