import random
from faker import Faker
fake = Faker()

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
        {social_title}
        {social_news}
        {company_update_title}
        {company_update}
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
        {social_title}
        {social_news}        
        <p>Check it out now:<br>
        <a href="{download_link}">Download {app_name} APK</a></p>
        <p>See you on the water!</p>
        {company_update_title}
        {company_update}
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
        {social_title}
        {social_news}
        {company_update_title}
        {company_update}
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
        {social_title}
        {social_news}
    </body>
    </html>
    """,
]

random_paragraphs = [
    "<p>Discover the thrill of the open water with our latest tracking features. Whether you're a pro or just starting, this app will elevate your experience!</p>",
    "<p>Stay ahead of the competition with our leaderboards, where you can compare your stats with riders from all over the world.</p>",
    "<p>With real-time updates on weather and tides, you’ll always know the best time to hit the water. Don’t let the weather catch you by surprise!</p>",
    "<p>Join a community of jet ski enthusiasts. Share your rides, compare notes, and find new friends who love the water as much as you do!</p>",
]