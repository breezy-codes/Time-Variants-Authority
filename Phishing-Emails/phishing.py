import random
from faker import Faker
import os

# Initialize Faker
fake = Faker()

# Create a directory to store HTML files if it doesn't exist
os.makedirs("generated_emails", exist_ok=True)

# Expanded list of jet ski-related subject lines with more variety
subject_lines = [
    "Check Out This Exclusive Jet Ski App for Enthusiasts!",
    "Your Jet Ski Experience Just Got Better – Download Our New App",
    "Limited Offer! Try Our New Jet Ski Adventure App Now",
    "New Jet Ski Tracker App – Discover the Best Locations",
    "Explore New Waters with Our Latest Jet Ski App!",
    "Jet Ski Lovers, Don’t Miss This App – Download Today",
    "Get Ready for the Ultimate Jet Ski Adventure – Download Now",
    "Unlock Exclusive Jet Ski Features with This App",
    "Attention Jet Ski Fans! A New App Just for You",
    "Are You a Jet Ski Enthusiast? Check Out This New App",
    "Enhance Your Jet Ski Experience with Our Latest App",
]

# Randomized sections to increase variability
random_activities = [
    "plan your next water adventure", 
    "record your jet ski rides", 
    "track weather updates in real time", 
    "monitor wave conditions", 
    "save your favorite riding spots",
    "share your jet ski experiences",
    "connect with other riders",
    "compete in challenges",
]

random_features = [
    "weather forecasts", 
    "tide schedules", 
    "best riding times", 
    "top jet ski locations", 
    "other riders' reviews of spots",
    "leaderboards",
    "ride statistics",
]

random_social_features = [
    "join virtual jet ski races", 
    "compete in global leaderboards", 
    "connect with riders in your area", 
    "share your rides on social media", 
    "compare stats with friends",
    "earn badges and achievements",
    "participate in challenges",
    "chat with fellow jet ski enthusiasts",
]

# Generate random app names and URLs
app_names = [
    "Jet Ski Pro", "Jet Ski Explorer", "Wave Rider", 
    "Jet Ski Tracker", "Ride the Waves", "Waterway Navigator",
    "Aqua Adventure", "Ocean Explorer", "Wave Runner",
    "Sea Tracker", "Ride Guide", "Waterworld",
]

download_urls = [
    "http://jetskiproapp.com/download",
    "http://jetskiexplorerapp.com/download",
    "http://waveriderapp.com/download",
    "http://jetskitrackerapp.com/download",
    "http://ridethewavesapp.com/download",
    "http://waterwaynavigatorapp.com/download",
    "http://aquaadventureapp.com/download",
    "http://oceanexplorerapp.com/download",
]

# Predefined list of team names
team_names = [
    "Jet Ski Adventures", "Wave Riders", "Aqua Team",
    "Ocean Explorers", "Ride the Waves Team", "Waterway Navigators",
    "Jet Ski Pro Team", "Wave Runner Team", "Sea Tracker Team",
    "Ride Guide Team", "Waterworld Team", "Jet Ski Tracker Team",
]

# Placeholder for random paragraphs
random_paragraphs = [
    "<p>Discover the thrill of the open water with our latest tracking features. Whether you're a pro or just starting, this app will elevate your experience!</p>",
    "<p>Stay ahead of the competition with our leaderboards, where you can compare your stats with riders from all over the world.</p>",
    "<p>With real-time updates on weather and tides, you’ll always know the best time to hit the water. Don’t let the weather catch you by surprise!</p>",
    "<p>Join a community of jet ski enthusiasts. Share your rides, compare notes, and find new friends who love the water as much as you do!</p>",
]

# Expanded email body templates in HTML format with placeholders for random sections
email_bodies = [
    """
    <html>
    <body>
        <p>Hi Mobius .m Mobius,</p>
        <p>As someone who loves jet skiing in {location}, we’ve got something exciting for you! Our new app, <strong>{app_name}</strong>, helps you track {random_activity}, {random_feature}, and connect with other jet ski enthusiasts worldwide.</p>
        {random_paragraph}
        <p>Get started by clicking the link below:<br>
        <a href="{download_link}">Download {app_name} APK</a></p>
        <p>Don’t miss out on enhancing your jet ski adventures!</p>
        <p>Best regards,<br>{team_name}</p>
    </body>
    </html>
    """,
    """
    <html>
    <body>
        <p>Hey Mobius .m Mobius,</p>
        <p>We know you enjoy exploring waters at {location}, so we thought you’d love our brand-new app: <strong>{app_name}</strong>. With this app, you can {random_activity}, stay updated on {random_feature}, and even {random_social_feature}!</p>
        {random_paragraph}
        <p>Check it out now:<br>
        <a href="{download_link}">Download {app_name} APK</a></p>
        <p>See you on the water!</p>
        <p>Cheers,<br>{team_name}</p>
    </body>
    </html>
    """,
    """
    <html>
    <body>
        <p>Hello Mobius .m Mobius,</p>
        <p>Ready to upgrade your jet ski adventures? The <strong>{app_name}</strong> app is perfect for jet ski lovers in {location} and beyond. It lets you {random_activity} and discover {random_feature} across your favorite water destinations.</p>
        {random_paragraph}
        <p>Download today:<br>
        <a href="{download_link}">Download {app_name} APK</a></p>
        <p>See you soon,<br>{team_name}</p>
    </body>
    </html>
    """,
    """
    <html>
    <body>
        <p>Dear Mobius .m Mobius,</p>
        <p>We are excited to introduce <strong>{app_name}</strong>, the newest app for jet ski enthusiasts. Track your jet ski adventures, monitor {random_feature}, and {random_social_feature} with fellow jet skiers from {location}!</p>
        {random_paragraph}
        <p>Start your journey today by downloading here:<br>
        <a href="{download_link}">Download {app_name} APK</a></p>
        <p>Sincerely,<br>{team_name}</p>
    </body>
    </html>
    """,
    """
    <html>
    <body>
        <p>Hi Mobius .m Mobius,</p>
        <p>Your jet ski experience at {location} is about to get even better! With <strong>{app_name}</strong>, you can {random_activity}, log your rides, and get real-time updates on {random_feature}.</p>
        {random_paragraph}
        <p>Get the app now:<br>
        <a href="{download_link}">Download {app_name} APK</a></p>
        <p>Don’t miss out on this incredible opportunity!</p>
        <p>Best,<br>{team_name}</p>
    </body>
    </html>
    """,
]

# Function to generate a random phishing email
def generate_email_html(index):
    subject = random.choice(subject_lines)
    body_template = random.choice(email_bodies)
    
    # Use Faker to create random details (location is randomized)
    location = fake.city()
    
    # Randomly select app-related details
    app_name = random.choice(app_names)
    download_link = random.choice(download_urls)
    random_activity = random.choice(random_activities)
    random_feature = random.choice(random_features)
    random_social_feature = random.choice(random_social_features)
    random_paragraph = random.choice(random_paragraphs)  # Select random paragraph
    team_name = random.choice(team_names)  # Use your predefined team names
    
    # Fill in the placeholders in the email body
    body = body_template.format(
        location=location, 
        team_name=team_name, 
        app_name=app_name,
        random_activity=random_activity,
        random_feature=random_feature,
        random_social_feature=random_social_feature,
        download_link=download_link,
        random_paragraph=random_paragraph  # Insert random paragraph
    )
    
    # Save the email as an HTML file
    filename = f"generated_emails/phishing_email_{index}.html"
    with open(filename, 'w') as f:
        f.write(body)
    
    return f"Email {index}: {subject}"

# Generate a series of phishing emails in HTML format and save each as a new file
def generate_emails_html(num_emails):
    for i in range(1, num_emails + 1):
        subject = generate_email_html(i)
        print(subject)

# Example: Generate 10 phishing emails as HTML files
generate_emails_html(2)
