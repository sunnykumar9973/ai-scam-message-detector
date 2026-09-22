"""
Dataset Download Script
Downloads the SMS Spam Collection dataset and saves it for training
"""

import requests
import os
import zipfile

# URL of the SMS Spam Collection dataset
DATASET_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip"
DATASET_PATH = os.path.dirname(__file__)
OUTPUT_FILE = os.path.join(DATASET_PATH, "spam.csv")
ZIP_FILE = os.path.join(DATASET_PATH, "smsspamcollection.zip")


def download_dataset():
    """Download the SMS Spam Collection dataset from UCI and convert it to CSV"""
    print(f"Downloading dataset from {DATASET_URL}...")
    
    try:
        response = requests.get(DATASET_URL, stream=True, timeout=30)
        response.raise_for_status()
        
        with open(ZIP_FILE, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        print(f"✓ Dataset archive downloaded to {ZIP_FILE}")
        
        with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
            zip_ref.extractall(DATASET_PATH)
        
        source_file = os.path.join(DATASET_PATH, "SMSSpamCollection")
        if not os.path.exists(source_file):
            raise FileNotFoundError("SMSSpamCollection file not found inside archive")
        
        with open(source_file, 'r', encoding='utf-8', errors='ignore') as raw_file, \
                open(OUTPUT_FILE, 'w', encoding='utf-8') as csv_file:
            csv_file.write("label,message\n")
            for line in raw_file:
                label, text = line.strip().split("\t", 1)
                text = text.replace(",", " ")
                csv_file.write(f"{label},{text}\n")
        
        print(f"✓ Dataset converted to CSV at {OUTPUT_FILE}")
        return True
    except Exception as e:
        print(f"✗ Error downloading dataset: {e}")
        print("Using fallback: Creating local dataset...")
        create_fallback_dataset()
        return False

def create_fallback_dataset():
    """Create a fallback dataset if download fails"""
    # Use a larger fallback dataset so the model has more spam/ham examples
    fallback_data = """label,message
ham,Go until jurong point crazy Available only in 4d sushi king lor
ham,Ok lar Joking wif u oni
ham,Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005 Text FA to 87121 to enter www FA org uk Laffaz
spam,FreeMsg Hey there darling it me once again and to see me again just txt me baby but to see me you know how i roll
ham,Even my brother is not like to speak with me They treat me like aids patient
ham,As per your request Melle Melle has been set as your callertune for all Callers Press to copy your friends Callertune
spam,WINNER As a valued network customer you have been selected to receive a prize reward To claim call 09061701461 Claim code KL341 Valid 12 hours only
ham,Had your mobile 11 months or more U R entitled to Update to the latest colour mobiles with half price line rental Call The Mobile Update co free on 0800 930 8271 Limited time offer
spam,SIX chances to win CASH All you need is a mobile number and email address Text GO to 71441
ham,I'm gonna be home soon and i don't want to talk about this stuff anymore tonight k I've gotta be helped on by 12 u can't be prepared for that
spam,For 5 Free to use the T-Mobile platform text YOUR NAME to 80062 then press play This is your chance to win 4 wk trip to Barcelona for just 35 incl hotel Text TM to 81010 for info T Cs apply
spam,Todays Voda number is 40411 FreeMsg Expect 1 per sms send and k4 varies by network T Cs see www vodafone co uk
ham,Ok so i was testing the catalog and i attached a practical error after the code of the intro page
spam,New Nokia 3310 mode available No1 rated vehicle leasing co Bg Rewards urn mvp spends Latest Motorola and Samerton phone All recommended Specs and Voting Kindly rents well
ham,Is it possible to make a significant profit trading forex on a very small deposit
ham,Sunshine Quiz Winning weight 100 in your Bank Account copy this link paste it in your browser to confirm you entry
ham,Once you have submitted the website use our links at the top of page to proceed with the claim
ham,Could i get a date wiv u baby
ham,Yeah but did you catch the bus BBC News SyncronGrade sets OFFICIAL Gerstner moulding Crop No H for Docs groups in verbals Forever
ham,Did you see the news today How you been
spam,Txt STOP to 80062 to opt out temporarily Txt START to resume
ham,Hey are you free this weekend
ham,Let's meet for coffee tomorrow at 3 PM
ham,Happy birthday Hope you have a great day
spam,Congratulations You won 1000000 Click here to claim
spam,FREE iPhone 15 Limited time offer
spam,URGENT Your account will be closed Verify here
spam,You have won a free ticket to Bahamas Text WIN to 70000
spam,Claim your free reward by replying YES to this message
spam,Your account has been selected to receive a cash prize Send OK now
spam,Exclusive offer Just text back to get your gift voucher today
spam,Reminder Your subscription will expire Pay now to continue service
spam,This is an urgent security alert Update your password immediately
spam,Congratulations you are the lucky winner of 15000 cash
spam,Dear user Click the link to verify your payment information now
spam,Win a brand new car Enter the code CAR44 to claim your prize
spam,Free membership upgrade available Reply YES to get it
spam,Verify your account now to avoid suspension of service
spam,Special promotion for you Text SAVE to 80082 to receive details
spam,You have been selected for a free membership upgrade
spam,Alert Your payment has failed Please update your billing info
spam,Free delivery on your next order Reply YES to confirm
spam,Congratulations You are preapproved for a new credit card
spam,Your parcel could not be delivered Provide details to reschedule
spam,Your loan application is approved Please send your bank details
spam,This is the last reminder to claim your urgent reward
spam,Act fast Limited seats available for our new investment plan
spam,Your service will be suspended unless you update your account
spam,Earn money from home with this quick simple program
spam,Free trial subscription confirmed Reply NOW to activate
spam,Your verification code expires soon Reply to verify
spam,Claim your cashback gift before midnight
spam,Your verification code expires soon Reply to verify
spam,Update shipping address to receive package delivery
spam,Cheap meds available text order now
spam,Your payment was declined Verify details to continue
spam,Dear customer You have won 2500 cash Prize
ham,Are you coming to the meeting later this afternoon
ham,Please send the notes after the class today
ham,Can you pick up some groceries on your way home
ham,I will be late to dinner because of traffic
ham,Thanks for the invitation I will join you tomorrow
ham,Please call me when you have time
ham,See you at the office at 9 am tomorrow
ham,Do you want to go to the movie tonight
ham,I finished the assignment and sent it to you
ham,Meet me at the cafe after work today
ham,Let me know when you reach home safely
ham,Act fast I am leaving now and will text you later
ham,The train is delayed by 10 minutes today
ham,Thanks for your help with the task this week
ham,I am on my way to the office now
ham,The weather is nice today Let us walk to lunch
ham,I will call you after the meeting ends
ham,I am going to the bank later this afternoon
ham,When is the next class scheduled for our group
ham,Do you want to watch a movie this weekend
ham,The event has been moved to Friday afternoon
ham,I need to buy groceries on the way home
ham,Please confirm your attendance for tomorrow
ham,I enjoyed the workshop yesterday a lot
ham,The team approved the budget for the project
ham,We should reschedule for Monday morning
ham,She sent the email yesterday with the details
ham,What time should I pick you up for dinner
ham,I forgot to bring the charger with me
ham,The appointment is at three pm today
ham,Our neighbors invited us for dinner tonight
ham,I will meet you at the cafe after work"""
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(fallback_data)
    
    print(f"✓ Fallback dataset created at {OUTPUT_FILE}")

if __name__ == "__main__":
    if not os.path.exists(OUTPUT_FILE):
        download_dataset()
    else:
        print(f"Dataset already exists at {OUTPUT_FILE}")
