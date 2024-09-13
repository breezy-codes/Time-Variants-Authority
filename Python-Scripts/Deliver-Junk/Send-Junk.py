import smtplib
import os
import random
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# Email configuration
FROM_EMAIL = "email"
TO_EMAIL = "email"
GMAIL_PASSWORD = "pass"

# Path to the folder with generated HTML email templates
HTML_FOLDER = "location"
HTML_FOLDER = os.path.expanduser(HTML_FOLDER)

def send_email():
    print(r"""
███████╗███████╗███╗   ██╗██████╗     ██╗████████╗██╗
██╔════╝██╔════╝████╗  ██║██╔══██╗    ██║╚══██╔══╝██║
███████╗█████╗  ██╔██╗ ██║██║  ██║    ██║   ██║   ██║
╚════██║██╔══╝  ██║╚██╗██║██║  ██║    ██║   ██║   ╚═╝
███████║███████╗██║ ╚████║██████╔╝    ██║   ██║   ██╗
╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝     ╚═╝   ╚═╝   ╚═╝

So you wanna send an email hey? I hope you're not up to no good...
------------------------------------------------------------------
    """)

    # Randomly select one of the team names as the sender name, and one of the subject lines
    team_names = ["Jet Ski Adventures", "Wave Riders", "Aqua Team", "Ocean Explorers", "Ride the Waves Team", 
                "Waterway Navigators", "Jet Ski Pro Team", "Wave Runner Team", "Sea Tracker Team", 
                "Ride Guide Team", "Waterworld Team", "Jet Ski Tracker Team"]
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
        "Discover the Thrill of Jet Skiing with Our App",
    ]

    # Get user input for subject or randomly generate from the specified list
    subject_input = input("Enter the subject of the email (or press Enter to generate one): ")
    if not subject_input:
        SUBJECT = random.choice(subject_lines)
        print(f"Random subject generated: {SUBJECT}")
    else:
        SUBJECT = subject_input
        print(f"Subject entered: {SUBJECT}")

    # Get user input for sender name or randomly generate from the specified list
    sender_input = input("Enter the sender name (or press Enter to generate one): ")
    if not sender_input:
        SENDER_NAME = random.choice(team_names)
        print(f"Random sender name generated: {SENDER_NAME}")
    else:
        SENDER_NAME = sender_input
        print(f"Sender name entered: {SENDER_NAME}")

    # Randomly select an HTML email template from the specified folder
    def get_random_html_body(html_folder):
        print(f"Selecting an email at random from '{html_folder}'...")
        html_files = [os.path.join(html_folder, f) for f in os.listdir(html_folder) if f.endswith('.html')]
        if not html_files:
            raise FileNotFoundError(f"No HTML files found in {html_folder}")
        
        selected_html = random.choice(html_files)
        with open(selected_html, 'r') as file:
            html_content = file.read()
        
        print(f"Using HTML file: {selected_html}")
        return html_content

    # Get the HTML body from the selected file
    html_body = get_random_html_body(HTML_FOLDER)

    # Ask the user if they want to embed a tracking pixel
    embed_pixel = input("Do you want to embed a tracking pixel? (y/n): ").strip().lower()

    if embed_pixel.lower() in ["yes", "y"]:
        tracking_pixel_url = input("Enter the URL for the tracking pixel: ").strip()
        if tracking_pixel_url:
            # Add the tracking pixel to the end of the email body
            tracking_pixel = f'<img src="{tracking_pixel_url}" width="1" height="1">'
            html_body += tracking_pixel
            print(f"Tracking pixel added with URL: {tracking_pixel_url}")
        else:
            print("No valid URL entered for tracking pixel. Skipping pixel embedding.")
    else:
        print("Tracking pixel not embedded.")

    # Create the MIMEMultipart object
    msg = MIMEMultipart()
    msg['From'] = f"{SENDER_NAME} <{FROM_EMAIL}>"
    msg['To'] = TO_EMAIL
    msg['Subject'] = SUBJECT

    # Attach the HTML body to the email
    msg.attach(MIMEText(html_body, 'html'))

    # Setup the SMTP server connection
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
    server.login(FROM_EMAIL, GMAIL_PASSWORD)
    server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())

    # Quit the server connection
    server.quit()
    
    print(r"""
------------------------------------------------------------------
███████╗███████╗███╗   ██╗████████╗         
██╔════╝██╔════╝████╗  ██║╚══██╔══╝         
███████╗█████╗  ██╔██╗ ██║   ██║            
╚════██║██╔══╝  ██║╚██╗██║   ██║            
███████║███████╗██║ ╚████║   ██║   ██╗██╗██╗
╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝╚═╝
------------------------------------------------------------------
    """)
    
while True:
    send_email()
    
    # Ask if the user wants to send another email or exit
    another_email = input("\nDo you want to send another email? (yes to continue, press Enter to exit): ").strip().lower()
    if another_email.lower() not in ["yes", "y"]:
        print("Exiting the program.")
        break