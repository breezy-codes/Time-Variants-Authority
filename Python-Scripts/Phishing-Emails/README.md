# Phishing Email Generator

This project generates random phishing emails in HTML format, simulating various jet ski-themed emails. Each email includes randomly generated content, such as app names, locations, activities, and social features. The generated emails are saved as `.html` files in a specified folder within the current directory.

## Purpose

The primary purpose of this project is to demonstrate how phishing emails can be constructed using random generators and template-based content. By leveraging libraries like `Faker` and custom random content, we can create a variety of unique phishing emails with minimal repetition.

## Project Structure

The project is split into multiple Python files for better organization:

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
- `get_random_paragraph()`: Selects a random paragraph.
- `get_random_social_title()`: Selects a random social title.
- `get_random_social_news()`: Selects a random social news section.
- `get_random_company_update_title()`: Selects a random company update title.
- `get_random_company_update()`: Selects a random company update.

### 2. `email_templates.py`

This module contains all the static content used in the phishing emails. This includes subject lines, body templates, app names, URLs, and various sections of the email such as company updates and social news.

### Lists

- `subject_lines`: Predefined subject lines for the emails.
- `email_bodies`: HTML templates for the email bodies.
- `app_names`: List of random app names.
- `download_urls`: List of random download URLs.
- `random_activities`: List of random activities.
- `random_features`: List of random features.
- `random_social_features`: List of random social features.
- `team_names`: List of random team names.
- `random_paragraphs`: List of random paragraphs to add variability to emails.
- `social_title`: List of random social section titles.
- `social_news`: List of random social news sections.
- `company_update_title`: List of random company update titles.
- `company_update`: List of random company updates.

### 3. `generate_emails.py`

This is the main module that ties everything together. It imports the random generation functions from `random_generators.py` and email content from `email_templates.py`. The `generate_email_html()` function is responsible for constructing the email content and saving it as an `.html` file in the `generated_emails` folder.

### Functions in `generate_emails.py`

- `generate_email_html(index)`: Generates a single phishing email using random data and saves it to an HTML file.
- `generate_emails_html(num_emails)`: Generates multiple phishing emails by calling `generate_email_html()` multiple times and saves them to the specified folder.

### Folder Structure

- `phishing_emails/`: This is the main directory containing the 3 Python files.
  - `generated_emails/`: This is where the generated phishing emails will be saved.

## Usage

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd phishing-emails
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script to generate phishing emails:

    ```bash
    python generate_emails.py
    ```

4. The generated emails will be saved in the `generated_emails` folder.

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

### Customization

You can modify the contents of the `email_templates.py` file to adjust the email templates, subject lines, or add additional random content.

### Requirements

- `Faker` library for generating random city names:

```bash
pip install faker
```
