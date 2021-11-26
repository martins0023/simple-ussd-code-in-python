#USSD CODE

default_airtime_balance = float
default_data_balance = int
ussd_code = int
ussd_daily = int
code_data_plan = 1
code = 131
usd_next_1 = 1
usd_next_2 = 2
usd_next_3 = 3
usd_next_4 = 4
usd_next_5 = 5
usd_next_6 = 6
usd_next_7 = 7
usd_next_8 = 8
usd_next_9 = 9
data_pl = int
our_range = 1
reply_cancel = 00

def bundles():
    print("1. Data Plans \n2. Social Bundles \n3. Balance Check \n4. Roaming/Int'l \n5. Borrow Credit/Recharge \n6. Gift Data \n7. Video Packs \n8. Hot Deals \n9. Chat Zigi \n00. opt out")

def social_bundles():
    social_dict = {
        '1' : 'Whatsapp',
        '2' : 'Facebook',
        '3' : 'Instagram',
        '4' : 'TikTok',
        '5' : 'Ayoba',
        '6' : 'All Social Bundle',
        '7' : 'Youtube, Instagram, and TikTok',
        '8' : 'Opera Mini & News',
        '9' : 'Social Mega BUndle',
        '10' : '2GO',
        '11' : 'WeChat',
        '12' : 'Eskimi',
        '0' : 'BACK',
        '00' : 'Opt Out'
        
    }
    whatsapp = {
        
    }
    facebook = {
        
    }
    instagram = {
        
    }
    tiktok = {
        
    }
    ayoba = {
        
    }
    all_social = {
        
    }
    ytb_insta_ttok = {
        
    }
    opera_mini_news = {
        
    }
    for gear in social_dict:
        print(gear,  social_dict[gear])
def balance_check():
    global default_data_balance
    global default_airtime_balance
    default_airtime_balance = 0
    default_data_balance = 0
    print(f"Your default \nairtime balance is: {default_airtime_balance} and your remaining \ndata bundle is {default_data_balance}")
    balance_dict = {
        
    }
def roaming():
    roaming_dict = {
        '1' : 'Roaming Data Bundles',
        '2' : 'Roaming Voice + Data Bundles',
        '3' : 'Free incoming roaming call',
        '4' : 'int\'l Calling Bundle',
        '5' : 'Roaming Balance Check'
        
    }
    for roam in roaming_dict:
        print(roam, roaming_dict[roam])

def borrow_credit():
    borrow_dict = {
        '1' : 'Borrow Airtime',
        '2' : 'Borrow Data',
        '3' : 'Recharge',
        '0' : 'Back'
    }
    for cred in borrow_dict:
        print(cred, borrow_dict[cred])
        
def gift_data():
    gift_data_dict = {
        '1' : 'Transfer from Data Balance',
        '2' : 'Buy for a friend',
        '3' : 'Request from a friend',
        '4' : 'View Pending Request',
        '0' : 'Back',
        '00' : 'MainMenu'
    }
    for gift in gift_data_dict:
        print(gift, gift_data_dict[gift])
        
def video_packs():
    video_pack_dict = {
        '1' : 'Youtube Video Packs',
        '2' : 'StarTimes Video Packs',
        '3' : '1GB (YouTube Only) + 500MB (Data access)',
        '4' : 'Showmax Mobile'
    }
    for pack in video_pack_dict:
        print(pack, video_pack_dict[pack])
        
def hot_deals():
    hot_deals_dict = {
        '1' : 'TopDeal4Me',
        '2' : 'Recharge4ME',
        '3' : 'Data4ME',
        '4' : 'VAS4ME'
    }
    for hot in hot_deals_dict:
        print(hot, hot_deals_dict[hot])
        
def chat_zigi():
    print("Y\'ello! Need Help? Chat Zigi on your preferred\nchannels; Whatsapp, FaceBook Messenger, Web and Telegram. Details via SMS.")
    print("____________________")
    print("____text_message____")
    print("____________________")
    chat_options_dict = {
        'zigi_whatsapp' : 'https://wa.me/2349033000001?text=Hi',
        'zigi_facebook' : 'https://m.me/MTNLoaded',
        'zigi_web' : 'https://www.mtnonline.com',
        'zigi_telegram' : 'https://t.me/MTNOnlineBot'
    }
    for zig in chat_options_dict:
        print(zig, chat_options_dict[zig])
       
def data_plans():
    global data_pln
    global ussd_daily
    daily_next = 1
    weekly_next = 2
    monthly_next = 3
    month2_3_next = 4
    always_on_next = 5
    data_pln = {
        '1' : 'Daily',
        '2' : 'Weekly',
        '3' : 'Monthly',
        '4' : '2-3Month',
        '5' : 'Always ON Plans',
        '6' : 'Mifi Plans',
        '7' : 'FREE Youtube',
        '8' : 'Hot Deals',
        '9' : 'Popular Plans',
        '10' : 'Manage Data',
        '99' : 'Next',
        '0' : 'Back'
        
    }
    daily = {
        '1' : 'N50 for 40MB',
        '2' : 'N100 for 100MB',
        '3' : 'N100 for 350MB (IG&TIKTOK ONLY)',
        '4' : 'N200 for 200MB (3 days)',
        '5' : 'N300 for 1GB',
        '6' : 'N500 for 2GB(2 days)',
        '7' : 'N25 for 250MB(Nightlife)',
        '99' : 'NEXT'
    }
    weekly = {
        
    }
    monthly = {
        
    }
    month2_3 = {
        
    }
    always_on = {
        
    }
    mifi = {
        
    }
    free_youtube = {
        
    }
    hot_deals = {
        
    }
    popular_plan = {
        
    }
    manage_data = {
        
    }
    for key in data_pln:
        print(key, '->', data_pln[key])
    ussd_daily = int(input("Buy Data Plans\n: "))
    if ussd_daily == daily_next:
        for door in daily:
            print(door, '->', daily[door])
        
         
    
def ussd_cd():
    global code
    global ussd_code
    global usd_next_1
    global usd_next_2
    global usd_next_3
    global usd_next_4
    global usd_next_5
    global usd_next_6
    global usd_next_7
    global usd_next_8
    global usd_next_9
    global data_pl
    global data_pln
    global our_range
    global reply_cancel
    ussd_code = int(input("Dial code :"))
    if ussd_code == code:
        bundles()
        for i in range (our_range):
            data_pl = int(input("Enter: "))
            if data_pl == usd_next_1:
                data_plans()
            elif data_pl == usd_next_2:
                social_bundles()
            elif data_pl == usd_next_3:
                balance_check()
            elif data_pl == usd_next_4:
                roaming()
            elif data_pl == usd_next_5:
                borrow_credit()
            elif data_pl == usd_next_6:
                gift_data()
            elif data_pl == usd_next_7:
                video_packs()
            elif  data_pl == usd_next_8:
                hot_deals()
            elif data_pl == usd_next_9:
                chat_zigi()
            elif data_pl == reply_cancel:
                print("You opted out")
    else:
        print("You dialed the wrong code..")
        
#data_plans()
ussd_cd()
#balance_check()