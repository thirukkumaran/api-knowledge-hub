import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="API Knowledge Hub",
    page_icon="🚀",
    layout="wide"
)

# Role-based  questions
ROLE_QUESTIONS = {
    "I'm an API Consumer": [
        "How can I quickly integrate a new API into my application?",
        "What are the best practices for API authentication?",
        "How do I handle API rate limits effectively?",
        "What tools can help me test and debug API integrations?",
        "How can I ensure my API integration is secure?"
    ],
    "I'm an API Developer": [
        "What are the latest API design standards?",
        "How can I create scalable and performant APIs?",
        "What are the best practices for API versioning?",
        "How do I implement proper error handling in APIs?",
        "What tools can help me develop APIs more efficiently?"
    ],
    "I'm an API Designer": [
        "How do I design RESTful APIs effectively?",
        "What are the key principles of API design?",
        "How can I create clear and consistent API documentation?",
        "What are the best practices for API naming conventions?",
        "How do I design APIs that are easy to understand and use?"
    ],
    "I'm a Tech Lead": [
        "How can I manage the entire API lifecycle?",
        "What strategies ensure API governance across teams?",
        "How do I balance innovation with API standardization?",
        "What metrics should I track for API performance?",
        "How can I implement an effective API strategy?"
    ],
    "I'm a Product Manager": [
        "How do APIs drive product innovation?",
        "What are the key considerations for API product development?",
        "How can APIs create new revenue streams?",
        "What makes a successful API product?",
        "How do I prioritize API features?"
    ],
    "I'm a Security Engineer": [
        "What are the top API security vulnerabilities?",
        "How can I implement robust API authentication?",
        "What are best practices for API security?",
        "How do I protect against common API attacks?",
        "What tools help in API security testing?"
    ],
    "I'm an API Tester": [
        "What are the best strategies for API testing?",
        "How can I automate API testing?",
        "What tools are essential for API testing?",
        "How do I create comprehensive API test cases?",
        "How can I simulate different API scenarios?"
    ]
}



# Load environment variables
load_dotenv()

# Get API key with error checking
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    st.error("OpenAI API key not found. Please check your .env file.")
    st.stop()

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_ai_response(question, role):
    """Generate AI response using OpenAI API"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f"You are an expert AI assistant specializing in APIs, focusing on the perspective of a {role}. Provide a comprehensive, detailed, and actionable response."},
                {"role": "user", "content": question}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating response: {str(e)}"

def main():
    # Custom CSS for enhanced styling
    st.markdown("""
    <style>
    .main-title {
        font-size: 2.5em;
        color: #2C3E50;
        text-align: center;
        margin-bottom: 20px;
    }
    .role-title {
        color: #3498DB;
        font-weight: bold;
    }
    .insights-box {
        background-color: #F4F6F7;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 80%;
        max-height: 300px;
        overflow-y: auto;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        z-index: 1000;
    }
    .sidebar-title {
        color: #2C3E50;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sidebar-link {
        color: #3498DB;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    .sidebar-link:hover {
        color: #2980B9;
        text-decoration: underline;
    }
    .stButton button {
        background-color: #3498DB;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #2980B9;
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar for API Lifecycle and Standards
    st.sidebar.markdown('<div class="sidebar-title">🔍 API Resources</div>', unsafe_allow_html=True)
    st.sidebar.markdown("### API Lifecycle")
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/api-governance-model/pages/8-lifecycle" class="sidebar-link" target="_blank">Lifecycle Stages</a>', unsafe_allow_html=True)
    
    st.sidebar.markdown("### API Design Standards")
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/api-governance-model/pages/3-api-design" class="sidebar-link" target="_blank">Design Best Practices</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/api-governance-model/pages/6-versioning" class="sidebar-link" target="_blank">Versioning</a>', unsafe_allow_html=True)

    st.sidebar.markdown("### API Security")
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/api-governance-model/pages/4-security" class="sidebar-link" target="_blank">Security Best Practices</a>', unsafe_allow_html=True)

    st.sidebar.markdown("### API Testing")
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/api-governance-model/pages/5-testing" class="sidebar-link" target="_blank">API Testing</a>', unsafe_allow_html=True)

    st.sidebar.markdown("### API Tools")
    st.sidebar.markdown('<a href="https://docs.developer.tech.gov.sg/docs/data-provisioning-standards-dps-linter/" class="sidebar-link" target="_blank">API Linter</a>', unsafe_allow_html=True)

    # Main title
    st.markdown('<h1 class="main-title">🚀 API Knowledge Hub</h1>', unsafe_allow_html=True)

    # Role Selection - Now at the top of the page
    st.markdown("## Select Your Role")
    selected_role = st.selectbox(
        "", 
        list(ROLE_QUESTIONS.keys())
    )

    # Questions Section
 #   st.markdown("## Questions")
    selected_question = st.radio(
        "Here are some questions we've chosen for you! :)", 
        ROLE_QUESTIONS[selected_role]
    )

    if st.button("Get Insights", key="predefined_insights_button"):
        with st.spinner("Generating insights..."):
            ai_response = generate_ai_response(selected_question, selected_role)
            st.session_state['last_response'] = {
                'question': selected_question,
                'response': ai_response,
                'type': 'predefined'
            }

    # Custom question input - Moved to the bottom
    st.markdown("## Ask Me Anything")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        custom_question = st.text_area("Specific API-related question", height=150)
    
    with col2:
        st.write("") # Spacer
        st.write("") # Spacer
        if st.button("Get Insights", key="custom_question_button"):
            if custom_question:
                with st.spinner("Generating insights..."):
                    custom_response = generate_ai_response(custom_question, selected_role)
                    st.session_state['last_response'] = {
                        'question': custom_question,
                        'response': custom_response,
                        'type': 'custom'
                    }
            else:
                st.warning("Please enter a question")

    # Fixed AI Insights at the bottom
    if 'last_response' in st.session_state:
        st.markdown('<div class="insights-box">', unsafe_allow_html=True)
        st.subheader("Insights")
        
        # Display the question
        st.markdown(f"**Question:** {st.session_state['last_response']['question']}")
        
        # Display the response
        st.write(st.session_state['last_response']['response'])
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()