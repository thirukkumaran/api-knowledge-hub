import streamlit as st

# Set page configuration
st.set_page_config(page_title="API Knowledge Hub", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    /* Center the main title */
    .centered-title {
        text-align: center;
        color: #2E86C1;
    }

    /* Style the sidebar */
    .sidebar .sidebar-content {
        background-color: #F4F6F6;
        padding: 20px;
    }

    /* Style for buttons */
    .stButton button {
        background-color: #2E86C1;
        color: white;
        padding: 10px 20px;
        margin: 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #1A5276;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar navigation
menu_options = [
    ("[API Chatbot](https://api-specs-validator.streamlit.app/aibot)", "AI-powered assistant to help you understand and ask questions related to API Strategy, Life Cycle and Development"),
    ("[API Linter](https://dps-linter-beta.app.airbase.sg/)", "Automated tool to validate and enforce API design standards and best practices"),
    ("[OpenAPI Templates](https://docs.developer.tech.gov.sg/docs/data-provisioning-standards-dps-linter/)", "Pre-configured OpenAPI specification templates to jumpstart your API design"),
    ("[Feedback](https://docs.developer.tech.gov.sg/docs/data-provisioning-standards-dps-linter/)", "Share your feedback and help us improve")
]

# Render sidebar menu with tooltips
for link, tooltip in menu_options:
    st.sidebar.markdown(link, help=tooltip, unsafe_allow_html=True)


# Main content based on sidebar selection
st.markdown("<h1 class='left-title'>API Knowledge Hub</h1>", unsafe_allow_html=True)

# User roles and descriptions
roles = {
    "I'm an API Consumer": "I want to integrate my application with existing APIs and accelerate the integration process.",
    "I'm an API Developer": "New to API development and want to understand the tools available to speed up development.",
    "I'm an API Designer": "Would like to learn about API standards to include in my designs and the tools available.",
    "I'm a Tech Lead": "Want to understand the API lifecycle from development to deployment, along with the tools that support it.",
    "I'm a Product Manager": "Want to understand API strategy and how to apply it in product development.",
    "I'm a Security Engineer": "Want to understand API security best practices and tools to ensure compliance and protection.",
    "I'm an API Tester": "Would like to explore API testing tools and automation techniques.",
}

# Display user roles as clickable buttons
for role, description in roles.items():
    if st.button(role):
        st.write(f"**Role:** {description}")
        
        # Provide relevant links based on the selected role
        if role == "I'm an API Developer":
            st.markdown("<a href='https://docs.developer.tech.gov.sg/docs/data-provisioning-standards-dps-linter/'>Generate Server Stub from OpenAPI Spec</a>", unsafe_allow_html=True)
            st.markdown("<a href='https://example.com/api-design-tools'>API Testing Tools</a>", unsafe_allow_html=True)
        elif role == "I'm an API Designer":
            st.markdown("<a href='https://example.com/api-design-standards'>API Design Standards</a>", unsafe_allow_html=True)
            st.markdown("<a href='https://example.com/api-design-tools'>API Design Tools</a>", unsafe_allow_html=True)
        elif role == "I'm a Tech Lead":
            st.markdown("<a href='https://example.com/api-lifecycle'>API Life Cycle</a>", unsafe_allow_html=True)
            st.markdown("<a href='https://example.com/api-management-tools'>API Deployment and Management Tools</a>", unsafe_allow_html=True)
        elif role == "I'm a Product Manager":
            st.markdown("<a href='https://example.com/api-strategy'>API Strategy</a>", unsafe_allow_html=True)
            st.markdown("<a href='https://example.com/api-product-development'>API Product Development</a>", unsafe_allow_html=True)
        elif role == "I'm an API Tester":
            st.markdown("<a href='https://example.com/api-testing-tools'>API Testing Tools</a>", unsafe_allow_html=True)
            st.markdown("<a href='https://example.com/api-automation'>API Automation</a>", unsafe_allow_html=True)
        elif role == "I'm a Security Engineer":
            st.markdown("<a href='https://example.com/api-security'>API Security Best Practices</a>", unsafe_allow_html=True)
            st.markdown("<a href='https://example.com/api-compliance'>API Compliance Tools</a>", unsafe_allow_html=True)
        elif role == "I'm an API Consumer":     
            st.markdown("<a href='https://example.com/api-testing'>Quickly Testing APIs with Postman and Curl</a>", unsafe_allow_html=True)
            st.markdown("<a href='https://example.com/api-sdk'>Using SDKs and API Clients for Faster Integration</a>", unsafe_allow_html=True)
            
