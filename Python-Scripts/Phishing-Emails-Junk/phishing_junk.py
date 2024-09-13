import random
from faker import Faker
import os

fake = Faker()
current_dir = os.getcwd()
output_folder = os.path.join(current_dir, "Python-Scripts", "Phishing-Emails-Junk", "Generated-Emails")
os.makedirs(output_folder, exist_ok=True)

# Import the python files that contain all the random data
from random_generator_junk import (random_activities, random_features, random_social_features, team_names, company_update_title, company_update, social_title, social_news)
from email_templates_junk import (subject_lines, email_bodies, random_paragraphs)

# Generate a series of phishing emails and save each as a new file
def generate_email_html(index):
    subject = random.choice(subject_lines)
    body_template = random.choice(email_bodies)
    
    location = fake.city()
    community_member = fake.name()
    number_of_years = random.randint(2, 8)
    random_activity = random.choice(random_activities)
    random_feature = random.choice(random_features)
    random_social_feature = random.choice(random_social_features)
    random_paragraph = random.choice(random_paragraphs)
    team_name = random.choice(team_names)
    social_title_text = random.choice(social_title)
    social_news_text = random.choice(social_news)
    company_update_title_text = random.choice(company_update_title)
    company_update_text = random.choice(company_update)
    
    # Fill in the placeholders in the email body
    body = body_template.format(
        location=location, 
        community_member=community_member,
        number_of_years=number_of_years,
        team_name=team_name, 
        random_activity=random_activity,
        random_feature=random_feature,
        random_social_feature=random_social_feature,
        random_paragraph=random_paragraph,
        social_title=social_title_text,
        social_news=social_news_text,
        company_update_title=company_update_title_text,
        company_update=company_update_text
    )

    filename = os.path.join(output_folder, f"phishing_email_{index}.html")
    with open(filename, 'w') as f:
        f.write(body)

def display_title():
    print(r"""
 ██████╗ ███████╗████████╗    ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗   ██╗
██╔════╝ ██╔════╝╚══██╔══╝    ██╔══██╗██║  ██║██║██╔════╝██║  ██║╚██╗ ██╔╝
██║  ███╗█████╗     ██║       ██████╔╝███████║██║███████╗███████║ ╚████╔╝ 
██║   ██║██╔══╝     ██║       ██╔═══╝ ██╔══██║██║╚════██║██╔══██║  ╚██╔╝  
╚██████╔╝███████╗   ██║       ██║     ██║  ██║██║███████║██║  ██║   ██║   
 ╚═════╝ ╚══════╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   
""")

# Generate a series of phishing emails in HTML format and save each as a new file
def generate_emails_html(num_emails):
    display_title()
    print("-" * 75)
    print(f"Generating {num_emails} phishing emails...")
    for i in range(1, num_emails + 1):
        subject = generate_email_html(i)
    print(f"Phishing emails generated and saved in {output_folder}")
    print("-" * 75)
    print("I hope you're ready to send some emails!")

generate_emails_html(20)
