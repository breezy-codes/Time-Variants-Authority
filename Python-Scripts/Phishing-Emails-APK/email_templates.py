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
    "Discover the Thrill of Jet Skiing with Our App",
]

email_bodies = [
    """
        <p>Hi Mobius .m Mobius,</p>
        <p>As someone who loves jet skiing in {location}, we’re thrilled to introduce you to something that will take your adventures to the next level! Our brand-new app, <strong>{app_name}</strong>, is designed specifically for jet ski enthusiasts like you. Whether you’re looking to track your {random_activity}, discover {random_feature}, or connect with fellow riders from around the world, this app has it all.</p>
        
        {random_paragraph}
        
        <p>But that's not all – the app also lets you customize your rides, track your performance in real-time, and unlock exclusive features only available to our community members. Imagine having access to detailed weather forecasts, water conditions, and tide schedules for your favorite spots, all in one place.</p>
        
        <p>Ready to enhance your jet ski experience? Install the app attached today!</p>
        
        
        <p>Don’t miss out on this exciting opportunity to join the ultimate community of jet ski lovers. Your next adventure is just a click away!</p>
        
        {social_title}
        {social_news}
        {company_update_title}
        {company_update}
        
        <p>Best regards,<br>{team_name}</p>
    """,
    """
        <p>Hey Mobius .m Mobius,</p>
        <p>If exploring the waters at {location} is your thing, then you’re going to love what we have in store for you! Introducing <strong>{app_name}</strong> – the ultimate app for jet ski enthusiasts. Whether you’re out for a thrilling ride or just cruising, this app gives you the tools to {random_activity}, stay up-to-date on {random_feature}, and even {random_social_feature}.</p>
        
        {random_paragraph}
        
        <p>Imagine this: You’re out on the water, and with just a tap, you can monitor real-time conditions, track your speed, and even compete with other jet skiers from across the globe! With {app_name}, you'll never miss a beat.</p>
        
        <p>But that’s not all – we’ve also packed the app with a social platform where you can share your experiences, post ride highlights, and find other enthusiasts in {location} and beyond. It's a one-stop shop for all things jet skiing.</p>
        
        <p>Don’t wait – install the app attached below to get started today!</p>
        
        {social_title}
        {social_news}
        <p>Check out what the community is saying and be part of this exciting journey!</p>
        
        {company_update_title}
        {company_update}
        
        <p>Cheers,<br>{team_name}</p>
    """,
    """
        <p>Hello Mobius .m Mobius,</p>
        <p>If you're looking to take your jet skiing adventures to the next level, then <strong>{app_name}</strong> is exactly what you need! Designed for jet ski enthusiasts like yourself, this app helps you track every detail of your ride, whether you're enjoying the waters in {location} or planning your next destination.</p>
        
        <p>With {app_name}, you can easily {random_activity}, get the latest updates on {random_feature}, and explore new features that will completely transform the way you ride.</p>
        
        {random_paragraph}
        
        <p>What sets this app apart? You’ll have access to live data on weather conditions, tidal shifts, and even other riders’ reviews of the best spots. And if that wasn't enough, {app_name} lets you log your journeys, track your performance, and compete with riders from all over the world.</p>
        
        <p>Install the app today and start your adventure!</p>
        
        <p>Join the growing community of jet ski lovers and take your passion to the next level!</p>
        
        {social_title}
        {social_news}
        {company_update_title}
        {company_update}
        
        <p>See you soon,<br>{team_name}</p>
    """,
    """
        <p>Dear Mobius .m Mobius,</p>
        <p>We're beyond excited to introduce you to <strong>{app_name}</strong> – the latest app that’s going to revolutionize your jet ski experiences! Whether you're a seasoned rider or just getting into jet skiing, this app is designed with you in mind.</p>
        
        <p>With {app_name}, you’ll be able to track your jet ski adventures like never before, monitor {random_feature}, and {random_social_feature} with fellow jet skiers from {location} and around the world.</p>
        
        {random_paragraph}
        
        <p>What makes {app_name} special? It offers cutting-edge features like real-time weather updates, GPS tracking, and rider-to-rider communication, making sure that every ride is smooth, safe, and memorable. You’ll also be able to share your favorite routes, compare your performance stats, and explore new destinations with ease.</p>
        
        <p>Don’t wait – install the app today and start your journey towards endless water adventures.</p>

        <p>Sincerely,<br>{team_name}</p>
    """,
    """
        <p>Hi Mobius .m Mobius,</p>
        <p>Your jet ski experience in {location} is about to be transformed! Say hello to <strong>{app_name}</strong> – the app built for those who live for the thrill of the water. Whether you’re looking to {random_activity}, log your rides, or stay updated on {random_feature}, this app has got you covered.</p>
        
        {random_paragraph}
        
        <p>With features like ride tracking, performance metrics, and real-time water conditions, {app_name} ensures you’re always prepared for your next adventure. But there’s more – connect with other jet ski enthusiasts, share your journeys, and explore new spots around {location} and beyond!</p>
        
        <p>Why wait? Get the app now and make every ride even more unforgettable!</p>
        
        <p>Let’s hit the water and explore what’s out there!</p>
        
        <p>Best,<br>{team_name}</p>
        
        {social_title}
        {social_news}
    """,
]

random_paragraphs = [
    "<p>Discover the thrill of the open water with our latest tracking features. Whether you're cutting through waves at top speed or cruising along the shoreline, our app is here to enhance every moment on the water. You can now map your favorite routes, log your performance, and track your speed in real-time. Whether you’re a seasoned pro mastering tricky maneuvers or a beginner just enjoying the open waters, this app will elevate your jet ski experience to new heights!</p>",
    "<p>Stay ahead of the competition with our leaderboards, where you can compare your stats with riders from all over the world. Compete in timed runs, distance challenges, or just see how your skills measure up against others in the community. Push yourself to beat your personal best or take on jet ski enthusiasts from across the globe, all while logging your performance data with precision.</p>",
    "<p>With real-time updates on weather, tides, and water conditions, you’ll always know the best time to hit the water. The app offers live forecasts and waterway alerts, ensuring you never get caught off guard by a sudden change in conditions. Know when the tides are just right or when it’s time to seek shelter from a brewing storm. Safety and adventure go hand-in-hand with these cutting-edge features, making every ride safer and more thrilling.</p>",
    "<p>Join a community of jet ski enthusiasts. Share your rides, compare notes, and find new friends who love the water as much as you do! Our social features allow you to upload photos and videos of your latest adventures, discuss gear and techniques, and organize group outings with other riders. Whether you're looking to learn from seasoned professionals or just share in the passion for the sport, the app’s community has something for everyone.</p>",
    "<p>Track your performance in detail with advanced telemetry features. Log your speed, distance, ride duration, and even your fuel usage to optimize each ride. By analyzing your data, you can learn how to increase efficiency, maximize speed, and even identify the best times and locations for future trips. With these powerful analytics, you can transform every ride into an opportunity to improve and perfect your technique.</p>",
    "<p>Explore new locations and find hidden gems with our location discovery feature. The app provides detailed maps of popular jet ski destinations, as well as off-the-beaten-path spots that only locals know about. Whether you're looking for calm waters to relax or high-adrenaline zones for wave jumping, you can find the best spots based on real rider reviews and recommendations.</p>",
    "<p>Stay informed about the latest jet ski trends and gear. Our app keeps you up to date with news on the latest jet ski models, accessories, and performance upgrades. Whether you’re interested in eco-friendly jet skis, fuel-efficient designs, or high-powered racing machines, we’ll help you stay on the cutting edge of technology and innovation in the world of personal watercraft.</p>",
]