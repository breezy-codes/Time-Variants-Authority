import random
from faker import Faker
fake = Faker()

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

team_names = [
    "Jet Ski Adventures", "Wave Riders", "Aqua Team",
    "Ocean Explorers", "Ride the Waves Team", "Waterway Navigators",
    "Jet Ski Pro Team", "Wave Runner Team", "Sea Tracker Team",
    "Ride Guide Team", "Waterworld Team", "Jet Ski Tracker Team",
]

company_update_title = [
    "<h2>Stay Updated on the Latest Features</h2>",
    "<h2>Discover What's New</h2>",
    "<h2>Get the Inside Scoop</h2>",
    "<h2>Don't Miss Out</h2>",
    "<h2>Exciting News Just In</h2>",
    "<h2>Be the First to Know</h2>",
]

company_update = [
    "<p>Our latest app update includes enhanced tracking features, improved weather forecasts, and a brand-new social news feed. Download now to experience the difference!</p>",
    "<p>Discover the newest additions to our app, including real-time wave conditions, personalized ride statistics, and a global leaderboard. Get ahead of the game!</p>",
    "<p>Get the inside scoop on our app's latest features from tracking your rides to connecting with other riders. Don't miss out on the fun – update now!</p>",
    "<p>Don't miss the latest updates on our app, from improved weather tracking to social challenges. Stay ahead of the curve and download the update today!</p>",
    "<p>Exciting news just in! Our app now features a social news feed, virtual challenges, and enhanced ride tracking. Experience the thrill – update now!</p>",
]

social_title = [
    "<h2>Connect with Other Riders</h2>",
    "<h2>Compete in Challenges</h2>",
    "<h2>Share Your Rides</h2>",
    "<h2>Join the Community</h2>",
    "<h2>Get Social</h2>",
    "<h2>Make Waves Together</h2>",
]

social_news = [
    "<p>Our latest app update is packed with new features designed to enhance your jet ski experience. We’ve added even more advanced tracking capabilities, refined weather forecasts with hyper-local precision, and introduced a brand-new social news feed. Now, you can stay connected with your fellow riders, track your performance in real time, and share your experiences like never before. Download the latest version and experience the difference firsthand!</p>",
    "<p>Discover the newest and most exciting additions to our app! The latest update includes real-time wave conditions, giving you up-to-the-minute data on water turbulence and surf quality. You’ll also have access to personalized ride statistics, helping you analyze every aspect of your performance, and a global leaderboard where you can compete with riders from around the world. It’s time to step up your game and push the limits. Update now to get ahead of the competition!</p>",
    "<p>We've just rolled out a major update with features you’re going to love! From detailed ride tracking to enhanced social connectivity, this update transforms your jet ski adventures. Track your routes, compare your stats, and share your journeys with the global jet ski community. Stay connected with other riders, discover new locations, and challenge yourself with the latest virtual events. Don’t miss out – update now and take your jet ski experience to the next level!</p>",
    "<p>Exciting things are happening with our app’s latest update! With improved weather tracking, you can now receive real-time updates on conditions specific to your location, ensuring you’re always prepared for the best (or worst) on the water. We’ve also introduced social challenges that let you compete with friends or other riders around the world. Stay ahead of the curve and download the update today to unlock these exciting new features!</p>",
    "<p>We’ve just released a thrilling new update that’s guaranteed to make your jet ski experience even more dynamic! You can now access a fully integrated social news feed where riders post updates, challenges, and tips. We’ve also added virtual challenges, so you can compete with riders from across the globe without ever leaving your favorite spot. Enhanced ride tracking and weather data round out this powerful update. Ready to level up? Update now and feel the difference on your next ride!</p>",
]