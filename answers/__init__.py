from .api_designer_answers import API_DESIGNER_ANSWERS
from .api_developer_answers import API_DEVELOPER_ANSWERS
from .api_consumer_answers import API_CONSUMER_ANSWERS
from .tech_lead_answers import API_TECH_LEAD_ANSWERS
from .product_manager_answers import PRODUCT_MANAGER_ANSWERS
from .security_engineer_answers import API_SECURITY_ENGINEER_ANSWERS
from .api_tester_answers import API_TESTER_ANSWERS

# Combine all role answers into one dictionary
DEFAULT_ANSWERS = {
    "I'm an API Designer": API_DESIGNER_ANSWERS,
    "I'm an API Developer": API_DEVELOPER_ANSWERS,
    "I'm an API Consumer": API_CONSUMER_ANSWERS,
    "I'm a Tech Lead": API_TECH_LEAD_ANSWERS,
    "I'm a Product Manager": PRODUCT_MANAGER_ANSWERS,
    "I'm a Security Engineer": API_SECURITY_ENGINEER_ANSWERS,
    "I'm an API Tester": API_TESTER_ANSWERS
}
