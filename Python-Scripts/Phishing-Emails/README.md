```bash
 ██████╗ ███████╗████████╗    ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗   ██╗
██╔════╝ ██╔════╝╚══██╔══╝    ██╔══██╗██║  ██║██║██╔════╝██║  ██║╚██╗ ██╔╝
██║  ███╗█████╗     ██║       ██████╔╝███████║██║███████╗███████║ ╚████╔╝ 
██║   ██║██╔══╝     ██║       ██╔═══╝ ██╔══██║██║╚════██║██╔══██║  ╚██╔╝  
╚██████╔╝███████╗   ██║       ██║     ██║  ██║██║███████║██║  ██║   ██║   
 ╚═════╝ ╚══════╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   
```

This project generates random phishing emails in HTML format, simulating various jet ski-themed emails. Each email includes randomly generated content, such as app names, locations, activities, and social features. The generated emails are saved as `.html` files in a specified folder within the current directory.

## Disclaimer

This project was created for educational purposes as part of a HD project, and it should only be used in simulated environments for educational or research purposes. The use of phishing emails for malicious intent is illegal and unethical.

## Purpose

The primary purpose of this project is to generate targeted phishing emails to a specific TVA employee as part of the HD hacking project. The target employee was found to love Jetskis, so 3 python files were created to generate a series of randomised but themed emails to entice the target to click on a link and install a "Jetski" app on their device. The emails are generated in HTML format and saved to a folder for later use.

## Folder Structure

The folder is split into multiple Python files for better organisation:

### 1. `random_generators.py`

This module is responsible for generating random content, such as locations, app names, download URLs, and random paragraphs. Functions in this file return randomly selected items from predefined lists or use the `Faker` library to create random cities.

### Functions in `random_generators.py`

- `get_random_location()`: Generates a random city using the `Faker` library.
- `get_random_app_name()`: Selects a random app name.
- `get_random_download_link()`: Selects a random download link.
- `get_random_activity()`: Selects a random activity.
- `get_random_feature()`: Selects a random feature.
- `get_random_social_feature()`: Selects a random social feature.
- `get_random_team_name()`: Selects a random team name.
- `get_random_social_title()`: Selects a random social title.
- `get_random_social_news()`: Selects a random social news section.
- `get_random_company_update_title()`: Selects a random company update title.
- `get_random_company_update()`: Selects a random company update.

### 2. `email_templates.py`

This module contains all the static content used in the phishing emails. This includes subject lines, body templates, app names, URLs, and various sections of the email such as company updates and social news.

### Lists

- `subject_lines`: Predefined subject lines for the emails.
- `email_bodies`: HTML templates for the email bodies.
- `random_paragraphs`: List of random paragraphs to add variability to emails.

### 3. `generate_emails.py`

This is the main module that ties everything together. It imports the random generation functions from `random_generators.py` and email content from `email_templates.py`. The `generate_email_html()` function is responsible for constructing the email content and saving it as an `.html` file in the `generated_emails` folder.

### Functions in `generate_emails.py`

- `generate_email_html(index)`: Generates a single phishing email using random data and saves it to an HTML file.
- `generate_emails_html(num_emails)`: Generates multiple phishing emails by calling `generate_email_html()` multiple times and saves them to the specified folder.

### Example of Generated Email

An example of what a generated phishing email might look like:

```html
<html>
<body>
    <p>Hi Mobius .m Mobius,</p>
    <p>As someone who loves jet skiing in Miami, we’ve got something exciting for you! Our new app, <strong>Jet Ski Pro</strong>, helps you track your next adventure, get real-time weather forecasts, and connect with other jet ski enthusiasts worldwide.</p>
    <p>Discover the thrill of the open water with our latest tracking features. Whether you're a pro or just starting, this app will elevate your experience!</p>
    <p>Get started by clicking the link below:<br>
    <a href="http://jetskiproapp.com/download">Download Jet Ski Pro APK</a></p>
    <p>Don’t miss out on enhancing your jet ski adventures!</p>
    <h2>Connect with Other Riders</h2>
    <p>Our app now features a social news feed where you can stay updated on the latest trends in the jet ski community. Don't miss out on the fun!</p>
    <h2>Stay Updated on the Latest Features</h2>
    <p>Our latest app update includes enhanced tracking features, improved weather forecasts, and a brand-new social news feed. Download now to experience the difference!</p>
    <p>Best regards,<br>Jet Ski Adventures</p>
</body>
</html>
```

### Requirements

- `Faker` library for generating random city names:

```bash
pip install faker
```

> For All Time Always. 🕰️🌐
