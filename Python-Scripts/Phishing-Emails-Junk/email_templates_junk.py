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
        <h1>Hi Mobius M. Mobius,</h1>
        <p>We hope you're enjoying your adventures on the water! We have some exciting news – our annual Jet Ski Expo is coming up soon in {location}!</p>
        <p>This year’s event will feature live demonstrations, expert talks, and an exclusive preview of the latest jet ski models. Whether you're looking to upgrade your gear or simply connect with fellow enthusiasts, this is an event you won’t want to miss.</p>
        <p>Save the date and stay tuned for more information on how to register. We look forward to seeing you there!</p>
        {social_title}
        {social_news}
        {company_update_title}
        {company_update}
        
        <h3>Coming soon!</h3>
        {random_paragraph}
        
        <p>Best regards,<br>{team_name}</p>
    """,
    """
        <h1>Hey Mobius M. Mobius,</h1>
        <h3>Coming soon!</h3>
        {random_paragraph}
        <p>We know that jet skiing is all about fun and excitement, but safety is always a top priority! That’s why we’re sharing some essential jet ski safety tips to keep you safe on the water.</p>

        <ul>
        <li>Always wear a life jacket and ensure it's properly fitted.</li>
        <li>Familiarize yourself with local water regulations before you head out.</li>
        <li>Keep a safe distance from other watercraft and always be aware of your surroundings.</li>
        <li>Never operate your jet ski under the influence of alcohol or drugs.</li>
        <li>Check the weather conditions before your ride to avoid surprises.</li>
        </ul>

        <p>Stay safe and enjoy your rides! We’ll keep sending tips to help you get the most out of your jet skiing adventures.</p>

        {social_title}
        {social_news}
        <p>Check out what the community is saying and be part of this exciting journey!</p>
        
        {company_update_title}
        {company_update}
        
        <p>Cheers,<br>{team_name}</p>
    """,
    """
        <h1>Hello Mobius M. Mobius,</h1>
        <p>We love seeing what our community is up to, and this month, we’re shining the spotlight on {community_member} from {location}!</p>

        <p>{community_member} has been an active part of our community for the past {number_of_years} years, sharing incredible photos and stories from their jet skiing adventures. Whether it’s exploring new coastlines or pushing the limits in speed challenges, {community_member} continues to inspire us all.</p>

        <p>Want to be featured in our next newsletter? Share your stories and photos with us – we love celebrating our passionate community!</p>
       
        <h3>Coming soon!</h3>
        {random_paragraph}
        
        {company_update_title}
        {company_update}
        
        <p>See you soon,<br>{team_name}</p>
    """,
    """
        <h1>Dear Mobius M. Mobius,</h1>
        <p>Taking care of your jet ski is key to making sure it performs its best season after season. In this newsletter, we’re sharing our top maintenance tips to keep your machine in top shape.</p>

        <ul>
        <li>Rinse your jet ski with fresh water after every ride, especially in saltwater conditions.</li>
        <li>Regularly check the oil and coolant levels to prevent engine issues.</li>
        <li>Inspect the hull for any signs of damage or wear, and repair any cracks immediately.</li>
        <li>Store your jet ski in a dry, secure area when not in use to avoid sun and weather damage.</li>
        <li>Schedule regular professional servicing to ensure your jet ski stays in peak condition.</li>
        </ul>

        <p>By following these tips, you'll be ready to hit the water with confidence every time!</p>
        <h3>Coming soon!</h3>
        {random_paragraph}
        <p>Sincerely,<br>{team_name}</p>
    """,
    """
        <h1>Hi Mobius M. Mobius,</h1>
        <p>As the seasons change, so do the opportunities for incredible jet skiing experiences! We’ve put together a list of top seasonal ride ideas that will keep you on the water no matter the time of year.</p>

        <ul>
        <li>Spring: Explore quiet lakes and rivers as nature begins to bloom.</li>
        <li>Summer: Enjoy the thrill of open ocean rides or take part in local jet ski competitions.</li>
        <li>Fall: Cruise along the coastlines to take in stunning fall foliage from a unique perspective.</li>
        <li>Winter: For the adventurous, try a winter ride in warmer climates or on calm waters during off-peak seasons.</li>
        </ul>
        
        <h3>Coming soon!</h3>
        {random_paragraph}
        
        <p>Wherever the season takes you, we’ll be here with more tips and ideas to make your rides unforgettable.</p>
        
        <p>Best,<br>{team_name}</p>
        
        {social_title}
        {social_news}
    """,
    """
        <h1>Hi Mobius M. Mobius,</h1>
        <p>We’ve discovered some incredible new jet skiing spots in {location} that we know you'll love! These locations offer stunning views, smooth waters, and plenty of room to ride to your heart’s content.</p>

        <p>Mobius, as a valued member of our community for {number_of_years} years, we want you to be among the first to know about these hidden gems.</p>
        
        <h3>Coming soon!</h3>
        {random_paragraph}

        <p>Don't forget to share your experience with us after visiting one of these amazing spots!</p>
        {company_update_title}
        {company_update}
        <p>Best regards,<br>{team_name}</p>
    """,
    """
        <h1>Hi Mobius M. Mobius,</h1>
        <p>Exciting news – the biggest jet ski event of the year is happening soon in {location}!</p>
        <h3>Coming soon!</h3>
        {random_paragraph}
        <p>As a loyal member of our community for {number_of_years} years, we want to personally invite you to join us. There will be live demos, thrilling races, and a chance to connect with fellow riders.</p>
        {social_title}
        {social_news}
        <p>Mobius, we hope to see you at this can't-miss event and celebrate our shared passion for jet skiing.</p> 
        <p>Best regards,<br>{team_name}</p>
    """
]

random_paragraphs = [
    "<p>Get ready to discover the thrill of the open water with our upcoming tracking features. Soon, you'll be able to map your favorite routes, log your performance, and track your speed in real-time. Whether you’re a seasoned pro mastering tricky maneuvers or a beginner just enjoying the open waters, this app will elevate your jet ski experience to new heights. Stay tuned!</p>", 
    "<p>Coming soon: Compete with riders from around the world with our leaderboard feature! You'll soon be able to compare your stats, take on timed runs, distance challenges, and much more. Push yourself to beat your personal best and see how your skills measure up. Get ready to log your performance data with precision when our app launches.</p>",  
    "<p>Stay tuned for real-time updates on weather, tides, and water conditions with our app's live forecasting. You’ll always know the best time to hit the water and stay safe while riding. With our upcoming features, you’ll never get caught off guard by a sudden change in conditions, ensuring safety and adventure go hand-in-hand.</p>",   
    "<p>Join a community of jet ski enthusiasts soon with our upcoming app! You'll be able to share your rides, compare notes, and connect with other riders who love the water just as much as you do. Get ready to upload photos and videos, discuss gear, and organize group outings – coming soon!</p>",  
    "<p>Track your performance in detail with advanced telemetry, coming soon to the app! You’ll be able to log speed, distance, ride duration, and fuel usage to optimize each ride. These powerful analytics will help you improve your efficiency and perfect your technique. Prepare to ride smarter when the app arrives!</p>",   
    "<p>Explore new jet skiing locations and find hidden gems with our upcoming location discovery feature. You’ll soon have access to detailed maps of popular and off-the-beaten-path spots based on real rider reviews. Whether you’re searching for calm waters or adrenaline-pumping zones, the best locations will soon be just a tap away!</p>",   
    "<p>Stay informed on the latest jet ski trends and gear, all coming soon to our app. From the newest jet ski models to high-performance accessories, you’ll have everything you need to stay on the cutting edge of the personal watercraft world. Get ready to explore what's next in jet skiing when our app launches!</p>",
]
