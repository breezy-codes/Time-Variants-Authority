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

The primary purpose of this is to generate **targeted newsletter emails** as part of the initial phase of the HD hacking project. The target TVA employee, who has been identified as a jet ski enthusiast, will begin receiving a series of randomised, jet ski-themed newsletters. These emails are designed to get the target comfortable with receiving emails from the sender, building trust before introducing malicious content in later stages. The emails are generated in HTML format and saved to a folder for future use in the project. Each email also mentions about a future app launch, which will be used to deliver the malicious payload.

## Folder Structure

The folder is split into multiple Python files for better organisation:

### 1. `random_generators.py`

This module is responsible for generating random content, such as locations, app names, download URLs, and random paragraphs. Functions in this file return randomly selected items from predefined lists or use the `Faker` library to create random cities.

### Functions in `random_generators.py`

- `get_random_location()`: Generates a random city using the `Faker` library.
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
<h1>Hey Mobius M. Mobius,</h1>
<h3>Coming soon!</h3>
<p>Coming soon: Compete with riders from around the world with our leaderboard feature! You'll soon be able to compare your stats, take on timed runs, distance challenges, and much more. Push yourself to beat your personal best and see how your skills measure up. Get ready to log your performance data with precision when our app launches.</p>
<p>We know that jet skiing is all about fun and excitement, but safety is always a top priority! That’s why we’re sharing some essential jet ski safety tips to keep you safe on the water.</p>

<ul>
    <li>Always wear a life jacket and ensure it's properly fitted.</li>
    <li>Familiarize yourself with local water regulations before you head out.</li>
    <li>Keep a safe distance from other watercraft and always be aware of your surroundings.</li>
    <li>Never operate your jet ski under the influence of alcohol or drugs.</li>
    <li>Check the weather conditions before your ride to avoid surprises.</li>
</ul>

<p>Stay safe and enjoy your rides! We’ll keep sending tips to help you get the most out of your jet skiing adventures.</p>

<h2>Make Waves Together</h2>
<p>We’ve just released a thrilling new update that’s guaranteed to make your jet ski experience even more dynamic! You can now access a fully integrated social news feed where riders post updates, challenges, and tips. We’ve also added virtual challenges, so you can compete with riders from across the globe without ever leaving your favorite spot. Enhanced ride tracking and weather data round out this powerful update. Ready to level up? Update now and feel the difference on your next ride!</p>
<p>Check out what the community is saying and be part of this exciting journey!</p>
        
<h2>Get the Inside Scoop</h2>
<p>Discover the newest additions to our app, including real-time wave conditions, personalized ride statistics, and a global leaderboard. Get ahead of the game!</p>
        
<p>Cheers,<br>Waterway Navigators</p>
```

### Requirements

- `Faker` library for generating random city names:

```bash
pip install faker
```

---

> For All Time Always. 🕰️🌐

```shell
██████╗ ██████╗ ███████╗███████╗███████╗██╗   ██╗   
██╔══██╗██╔══██╗██╔════╝██╔════╝╚══███╔╝╚██╗ ██╔╝   
██████╔╝██████╔╝█████╗  █████╗    ███╔╝  ╚████╔╝    
██╔══██╗██╔══██╗██╔══╝  ██╔══╝   ███╔╝    ╚██╔╝     
██████╔╝██║  ██║███████╗███████╗███████╗   ██║   ██╗
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝
```
