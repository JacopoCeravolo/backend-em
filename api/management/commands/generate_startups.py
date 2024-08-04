

import json
data = {
    "name": "CyberSafe",
    "code": "CS113",
    "location": "Austin, TX",
    "industry": "Water Management",
    "founding_date": "2023-01-01",
    "legal_form": "Corporation",
    "type_of_business": "B2B",
    "website": "https://cybersafe.com",
    "facebook": "https://facebook.com/cybersafe",
    "linkedin": "https://linkedin.com/company/cybersafe",
    "twitter": "https://twitter.com/cybersafe",
    "description": "Pioneering firewall solutions.",
    "mission": "To Safeguard digital assets.",
    "product_description": "Firewall solutions.",
    "customer_problem": "Lack of affordable firewall options.",
    "usp": "Sustainable food production",
    "capital": 1700000,
    "stage": "Series B",
    "target_investor_n": 3,
    "use_of_funds": {
        "R&D": 40,
        "Marketing": 30,
        "Operations": 30
    },
    "financial_tables": "Financial data here.",
    "already_invested_n": 0,
    "impact_value": 2.0,
    "team_values": [
        "Integrity",
        "Innovation"
    ],
    "team_motives": [
        "Resource Management"
    ],
    "funding_experience": "Yes",
    "team_languages": [
        "English"
    ],
    "investor_expertise": [
        "Water Treatment Technology",
        "Sustainability"
    ],
    "investor_expectations": [
        "Resource conservation",
        "Infrastructure development"
    ],
    "exit_strategy": "Acquisition",
    "type_of_investment": "Equity",
    "market": "Global water management market.",
    "sdg": {
        "SDG 7": "Affordable and Clean Energy",
        "SDG 13": "Climate Action",
        "SDG 6": "Clean Water and Sanitation"
    }
}
with open('/home/rumoza/Desktop/test_matching/company_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
