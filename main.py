# This game is a cyberpunk business simulation. 

# The player starts with a certain amount of money. The player can buy businesses and shares in the stock market. Everyday, stocks go up or down. 
# The goal of the player is to make money.
# The player has to pay charges daily. If the player's money goes below 0, it's game over.

import time
import random

print ("\n------Cyber Business------\n")
    
# The character has a name, money, a number of businesses owned, income per day, charges to pay per day, action points per day
class Character:
    def __init__ (self, name, money, business, income, charges, action, action_day):
        self.name = name
        self.money = money
        self.business = business
        self.income = income
        self.charges = charges
        self.action = action
        self.action_day = action_day
        
    def showbalance(self): # function to show the current amount of money in the player's account
        print(f"You currently have {self.money} $ in your account.")
        
    def show_businesses(self): # function to show the amount of businesses own and the income per day
        print(f"You own {player.business} businesses, generating {player.income} $ per day.")
        
    def show_action_points(self):
        print(f"Maximum Action Points : {player.action}. | Today's Action Points : {player.action_day}.")
    
    def getmoney(self, x): # function to receive money in player's account, like a payment being received.
        self.money += int(x)
        print("Transfering funds to your personal account...")
    
    def paymoney(self, x): # function to pay money from the player's account
        self.money -= int(x)
        print("Paying...")
        
    def showcharges(self):
        print(f"Your charges are {self.charges} $ per day.")
        
    def newday(self):
        self.money += self.income
        self.money -= self.charges
        print(f"| Your account has been credited with : {self.income}$.")
        print(f"| You had to pay charges for : {self.charges}$.")
        
    def allocate_action(self): # Makes the action count for today the same as maximum action. Its used when the day is refreshed to reset the number of action points usable to Full
        self.action_day = self.action
        print(f"| Your action points have been restored. ({self.action_day})")
        
class Business:
    def __init__ (self, name, price, income, charges, availability): # Name of business, price, income generated per day, cost to pay per day for maintenances and charges, and availability
        self.name = name
        self.price = price
        self.income = income
        self.charges = charges
        self.availability = availability
        
    def buy_business(self):
        print("------ ------ ------")
        print("Purchasing...")
        
        player.money = player.money - self.price # substract the player's money by the price of the business. 
        player.business += 1 # Add 1 to the number of business the player owns.
        player.income += self.income # add the income of the business to the players income.
        player.charges += self.charges # add the charges of the business to the players income.
        self.availability = 'No' # changes the availability to No, which indicates that the business is not for sale anymore.
        
        time.sleep(1)
        print(f"\nYou successfuly purchased : {self.name} for {self.price} $!")
        
    def sell_business(self):
        print("------ ------ ------")
        if player.action_day > 0:
            print("Selling...")
            
            player.money = player.money + self.price
            player.business -= 1
            player.income -= self.income
            player.charges -= self.charges
            self.availability = 'Yes'
            
            time.sleep(1)
            print(f"\nYou successfuly sold : {self.name} for {self.price} $!")
        else:
            print("You cannot sell your business without action points. Transaction cancelled.")
        
    def grow_business(self): # add value to the income per day and the price of the business by a certain %, also remove 1 action point of the day
        print("------ ------ ------")
        if player.action_day > 0:
            answer = input(f"Do you want to work at improving this business? This will consume 1 action point. [Y/n] or '0' to go back to main menu: ").lower()
    
            if answer == 'y':
                print("\nConnecting to the business interface and improving the business...")
                self.price = int(self.price * 1.03)
                self.income = int(self.income * 1.03)
                
                player.action_day -= 1
                time.sleep(1)
                print(f"\nOperation successful! The business has been improved. {self.name} will now generate {self.income} $ per day and is valued at {self.price} $.")
        else:
            print("\nYou don't have enough action points!")
                
    def devalue_business(self): # Devalue a business by a certain %
        self.price = int(self.price * 0.99)
        self.income = int(self.income * 0.99)  
        
    def actualize_income(self):
        if self.availability == 'No':                   
            player.income += self.income 

class Stock:
    def __init__ (self, name, price, shares, total, ogshares):
        self.name = name
        self.price = price
        self.shares = shares
        self.total = total # total of the money of all the shares combined
        self.ogshares = ogshares # original share price
        
    def totaling(self): # calculates price x shares
        return  self.price * self.shares
    
    def change_percent(self): # Calculates the change in percent between the current share price and the original share price (ogshares)
        return round(((self.price - self.ogshares) / self.ogshares) * 100, 2)
    
    def buy_stocks(self):
        print("------ ------ ------")
        shares_tobuy = int(input("Enter the number of shares to buy: "))
        print("------ ------ ------")
        sure = input(f"Purchasing {shares_tobuy} shares of {self.name} for {shares_tobuy * self.price} $. Are you sure? [Y/n]: ").lower()
        if sure == 'y':
            print("------ ------ ------")
            if player.money < shares_tobuy * self.price:
                unsuficient_funds()
            else:    
                print(f"Purchasing {shares_tobuy} shares of {self.name} for {shares_tobuy * self.price} $...") # purchasing number of shares from the company for the total amount of money.
                
                player.money -= shares_tobuy * self.price # substracting the number of shares x the share price from the player's money
                self.shares += shares_tobuy # adding the shares that were just bought to the company's account on behalf of the player
                
                time.sleep(1) # to simulate a transaction
                print("\nPurchase successful!")
        else:
            print("\nCanceling order... Going back to main menu.")
            
    def sell_stocks(self):
        print("------ ------ ------")
        shares_tosell = int(input("Enter the number of shares to sell: "))
        print("------ ------ ------")
        sure = input(f"Selling {shares_tosell} shares of {self.name} for {shares_tosell * self.price} $. Are you sure? [Y/n]: ").lower()
        if sure == 'y':
            print("------ ------ ------")
            if self.shares < shares_tosell:
                print("\nYou don't own that many shares!")
            else:    
                print(f"Selling {shares_tosell} shares of {self.name} for {shares_tosell * self.price} $...") # selling number of shares for the total amount of money.

                player.money += shares_tosell * self.price # adding the number of share x share price to the player's money
                self.shares -= shares_tosell # removing the shares that were just sold from the company's account on behalf of the player
                
                time.sleep(1)
                print("\nSale successful!")
        else:
            print("\nCanceling sale... Going back to main menu.")
  
    def fluctuations(self): # fluctuation every day of the stock market 
        stock_fluctuations = random.uniform(0.95, 1.05)
        self.price = int(self.price * stock_fluctuations)
        if self.price < 0:
            self.price = int(0)
        
    def big_fluctuations(self): # uncertain and big fluctuations
        stock_fluctuations = random.uniform(0.70, 1.30)
        self.price = int(self.price * stock_fluctuations)
        if self.price < 0:
            self.price = int(0)
        
    def slow_steady_fluctuations(self): # Reliable and more likely to grow
        stock_fluctuations = random.uniform(0.99, 1.03)
        self.price = int(self.price * stock_fluctuations)
        if self.price < 0:
            self.price = int(0)
        
    def medium_fluctuations(self):
        stock_fluctuations = random.uniform(0.85, 1.15)
        self.price = int(self.price * stock_fluctuations)
        if self.price < 0:
            self.price = int(0)
   
class Item:
    def __init__ (self, name, price, action, availability):
        self.name = name
        self.price = price
        self.action = action
        self.availability = availability
        
    def buy_item(self):
        print("------ ------ ------")
        print("Purchasing...")
        player.money = player.money - self.price
        player.action += 1
        self.availability = 'No'
        
        time.sleep(1)
        print(f"\nYou successfuly purchased : {self.name} for {self.price} $! You also gained {self.action} Action Point.")
        
# Items 
laptop = Item("Kruger Business Laptop", 20000, 1, "Yes") # Name, price, action points, availability
cyberdeck = Item("Biocos MK.2 Cyberdeck", 150000, 1, "Yes")
car = Item("Farfetch Malibu Luxury Car", 299000, 1, "Yes")
              
# Businesses        
hardware_store = Business("Germanium", 6900, 350, 300, "Yes") # defining the business caracteristics. Name, price, income, charges, availability
night_club = Business("Paradise", 59000, 1943, 1450, "Yes")
cyber_cafe = Business("Matrix Cyber Cafe", 17500, 871, 600, "Yes")
schneider = Business("Schneider Corp.", 195000, 6700, 4500, "Yes")
radioactiv = Business("RadioActiv", 11000, 682, 450, "Yes")

# Stocks
kruger = Stock("Kruger", 3000, 0, 0, 3000) # Name, share price, number of shares, total $ owned, original share price
mizotich = Stock("Mizotich", 678, 0, 0, 678)
deluxo = Stock("Deluxo", 247, 0, 0, 247)
biocorp = Stock("Biocorp", 56, 0, 0, 56)
zirton = Stock("Zirton", 153, 0, 0, 153)

# Player
player = Character("Name", 10000, 0, 0, 0, 1, 1) # Creating an account with the name, money, business, income, charges, action points max, action points usable today
       
print("Welcome to Cyber Business!")
print("Buy businesses, make them grow and invest in the stock market! If your money goes below 0, it's game over!")
print("Each day, you have an action point to make one business grow. Use it wisely! Businesses will also lose value over time.\n")
input("Press Enter and create a new account.")
print("Creating a new account...\n")

time.sleep(1) # Simulating the creation of a new account
input("Press Enter to start...")

def unsuficient_funds():
    print("\nYou don't have the money!")
 
def press_enter():
    input("\nPress Enter to go back to the main menu...")

def devaluation(): # Will check for which business needs to lose in value today, depending on if they're owned or not.
    if hardware_store.availability == 'No':
        hardware_store.devalue_business()
    if night_club.availability == 'No':
        night_club.devalue_business()
    if cyber_cafe.availability == 'No':
        cyber_cafe.devalue_business()
    if schneider.availability == 'No':
        schneider.devalue_business()
    if radioactiv.availability == 'No':
        radioactiv.devalue_business()

def reset_income(): # remove the total income of the player
    player.income = 0

def actualize_income_business():
    hardware_store.actualize_income()
    night_club.actualize_income()
    cyber_cafe.actualize_income()
    schneider.actualize_income()
    radioactiv.actualize_income()
    
# Marketplace menu
def marketplace_menu():
    print("------ ------ ------")
    print("Here's a list of items for sale:")
    print("------ ------ ------")
    if laptop.availability == 'Yes':
            print(f"| 1 | Name: {laptop.name}     | Price: {laptop.price} $   | Action Point: {laptop.action} | For sale : {laptop.availability} |")
    if cyberdeck.availability == 'Yes':
            print(f"| 2 | Name: {cyberdeck.name}      | Price: {cyberdeck.price} $  | Action Point: {cyberdeck.action} | For sale : {cyberdeck.availability} |")
    if car.availability == 'Yes':
            print(f"| 3 | Name: {car.name}| Price: {car.price} $  | Action Point: {car.action} | For sale : {car.availability} |")

    item_choice = int(input("\nEnter the number of the item you'd like to buy, or '0' to go back to the main menu: "))
    
    if item_choice == 0:
        ...
            
    elif item_choice == 1:
        if laptop.availability != 'Yes':
                print("\nThis item is not for sale!")
                press_enter()
                
        elif player.money < laptop.price:
                unsuficient_funds()
                press_enter()
                
        else:
            ask_purchase_item = input(f"\nPurchase the item {laptop.name} for {laptop.price} $ ? [Y/n]: ").lower()
            
            if ask_purchase_item == 'y':
                laptop.buy_item()
                press_enter()
                    
    elif item_choice == 2:
        if cyberdeck.availability != 'Yes':
                print("\nThis item is not for sale!")
                press_enter()
                
        elif player.money < cyberdeck.price:
                unsuficient_funds()
                press_enter()
                
        else:
            ask_purchase_item = input(f"\nPurchase the item {cyberdeck.name} for {cyberdeck.price} $ ? [Y/n]: ").lower()
            
            if ask_purchase_item == 'y':
                cyberdeck.buy_item()
                press_enter()
                
    elif item_choice == 3:
        if car.availability != 'Yes':
                print("\nThis item is not for sale!")
                press_enter()
                
        elif player.money < car.price:
                unsuficient_funds()
                press_enter()
                
        else:
            ask_purchase_item = input(f"\nPurchase the item {car.name} for {car.price} $ ? [Y/n]: ").lower()
            
            if ask_purchase_item == 'y':
                car.buy_item()
                press_enter()    
        
 
# Investments menu
def investments_menu():
    print("------ ------ ------")
    print("Here's a list of every stocks on sale:")
    print("------ ------ ------")
    print(f"| 1 | Name: {kruger.name}     | Price: {kruger.price} $    | Shares Owned: {kruger.shares} | Total Owned: {kruger.totaling()} $ | Change: {kruger.change_percent()} % |")
    print(f"| 2 | Name: {mizotich.name}    | Price: {mizotich.price} $     | Shares Owned: {mizotich.shares} | Total Owned: {mizotich.totaling()} $ | Change: {mizotich.change_percent()} % |")
    print(f"| 3 | Name: {deluxo.name}    | Price: {deluxo.price} $     | Shares Owned: {deluxo.shares} | Total Owned: {deluxo.totaling()} $ | Change: {deluxo.change_percent()} % |")
    print(f"| 4 | Name: {biocorp.name} | Price: {biocorp.price} $      | Shares Owned: {biocorp.shares} | Total Owned: {biocorp.totaling()} $ | Change: {biocorp.change_percent()} % |")
    print(f"| 5 | Name: {zirton.name}    | Price: {zirton.price} $     | Shares Owned: {zirton.shares} | Total Owned: {zirton.totaling()} $ | Change: {zirton.change_percent()} % |")
    
    stock_select = int(input("\nSelect a stock [1-5] or '0' to go back to the main menu: "))
    
    if stock_select == 0:
        ...  
    elif stock_select == 1:
        kruger_select()
         
    elif stock_select == 2:
        mizotich_select()
              
    elif stock_select == 3:
        deluxo_select()
        
    elif stock_select == 4:
        biocorp_select()
        
    elif stock_select == 5:
        zirton_select()

# Business menu
def business_menu():
    print("------ ------ ------")
    player.show_businesses()
    print("\n1. Browse businesses")
    print("2. Manage businesses")
    print("3. Go back to main menu")
    business_menu_choice = int(input("Choose an option [1-3]: "))
    
    if business_menu_choice == 1:      # Browse businesses
        print("------ ------ ------")
        print("Here's a list of every businesses for sale:")
        print("------ ------ ------")
        if hardware_store.availability == 'Yes':
            print(f"| 1 | Name: {hardware_store.name}       | Price: {hardware_store.price} $   | Income: {hardware_store.income} $   | Charges: {hardware_store.charges} $   | For sale : {hardware_store.availability} |")
        if night_club.availability == 'Yes':
            print(f"| 2 | Name: {night_club.name}         | Price: {night_club.price} $  | Income: {night_club.income} $  | Charges: {night_club.charges} $  | For sale : {night_club.availability} |")
        if cyber_cafe.availability == 'Yes':
            print(f"| 3 | Name: {cyber_cafe.name}| Price: {cyber_cafe.price} $  | Income: {cyber_cafe.income} $  | Charges {cyber_cafe.charges} $    | For sale : {cyber_cafe.availability} |")
        if schneider.availability == 'Yes':    
            print(f"| 4 | Name: {schneider.name}  | Price: {schneider.price} $ | Income: {schneider.income} $ | Charges: {schneider.charges} $ | For sale : {schneider.availability} |")
        if radioactiv.availability == 'Yes':
            print(f"| 5 | Name: {radioactiv.name}       | Price: {radioactiv.price} $  | Income: {radioactiv.income} $   | Charges: {radioactiv.charges} $   | For sale : {radioactiv.availability} |")
    
        businessfs_choice = int(input("\nEnter the number of the business you'd like to check, or '0' to go back to the main menu: ")) #business for sale choice
        if businessfs_choice == 0: # Pressing 0 to quit
            ...
        
        elif businessfs_choice == 1: # Selecting first business
            
            if hardware_store.availability != 'Yes':
                print("\nThis business is not for sale!")
                press_enter()
                
            elif player.money < hardware_store.price:
                unsuficient_funds()
                press_enter()
                
            else:
                hardware_store_summ()
                ask_purchase_business = input("\nDo you want to purchase the business? [Y/n]: ").lower()
                
                if ask_purchase_business == 'y':
                    hardware_store.buy_business()
                    press_enter()
                
        elif businessfs_choice == 2:
            
            if night_club.availability != 'Yes':
                print("\nThis business is not for sale!")
                press_enter()
                
            elif player.money < night_club.price:
                unsuficient_funds()
                press_enter()
                
            else:
                nightclub_summ()
                ask_purchase_business = input("\nDo you want to purchase the business? [Y/n]: ").lower()
                
                if ask_purchase_business == 'y':
                    night_club.buy_business()
                    press_enter()
                    
        elif businessfs_choice == 3:
            
            if cyber_cafe.availability != 'Yes':
                print("\nThis business is not for sale!")
                press_enter()
                
            elif player.money < cyber_cafe.price:
                unsuficient_funds()
                press_enter()
                
            else:
                cyber_cafe_summ()
                ask_purchase_business = input("\nDo you want to purchase the business? [Y/n]: ").lower()
                
                if ask_purchase_business == 'y':
                    cyber_cafe.buy_business()
                    press_enter()
                    
        elif businessfs_choice == 4:
            
            if schneider.availability != 'Yes':
                print("\nThis business is not for sale!")
                press_enter()
                
            elif player.money < schneider.price:
                unsuficient_funds()
                press_enter()
                
            else:
                schneider_summ()
                ask_purchase_business = input("\nDo you want to purchase the business? [Y/n]: ").lower()
                
                if ask_purchase_business == 'y':
                    schneider.buy_business()
                    press_enter()
                    
        elif businessfs_choice == 5:
            
            if radioactiv.availability != 'Yes':
                print("\nThis business is not for sale!")
                press_enter()
                
            elif player.money < radioactiv.price:
                unsuficient_funds()
                press_enter()
                
            else:
                radioactiv_summ()
                ask_purchase_business = input("\nDo you want to purchase the business? [Y/n]: ").lower()
                
                if ask_purchase_business == 'y':
                    radioactiv.buy_business()
                    press_enter()
            
                                        
    elif business_menu_choice == 2: # 2. Manage business
            print("------ ------ ------")
            reset_income()                    # Reset the income of the player to 0
            actualize_income_business()       # Adds the total income of owned businesses to the player's income
            player.show_businesses()
            print("Owned businesses:")
            print("------ ------ ------")
            if hardware_store.availability == 'No':
                print(f"| 1 | Name: {hardware_store.name}       | Price: {hardware_store.price} $   | Income: {hardware_store.income} $   | Charges: {hardware_store.charges} $   |")
            if night_club.availability == 'No':
                print(f"| 2 | Name: {night_club.name}         | Price: {night_club.price} $  | Income: {night_club.income} $  | Charges: {night_club.charges} $  |")
            if cyber_cafe.availability == 'No':
                print(f"| 3 | Name: {cyber_cafe.name}| Price: {cyber_cafe.price} $  | Income: {cyber_cafe.income} $  | Charges {cyber_cafe.charges} $    |")
            if schneider.availability == 'No':    
                print(f"| 4 | Name: {schneider.name}  | Price: {schneider.price} $ | Income: {schneider.income} $ | Charges: {schneider.charges} $ |")
            if radioactiv.availability == 'No':
                print(f"| 5 | Name: {radioactiv.name}       | Price: {radioactiv.price} $  | Income: {radioactiv.income} $   | Charges: {radioactiv.charges} $   |")
            
            business_owned_choice = int(input("\nEnter the number of the business you'd like to check, or '0' to go back to the main menu: "))
            
            if business_owned_choice == 0: # Pressing 0 to quit
                ...
            
            elif business_owned_choice == 1 and hardware_store.availability == 'No':
                print("\n1. Grow the business")
                print("2. Sell the business")
                print("3. Go back to main menu")
                ask_business_owned_choice = int(input("\nChoose an option [1-3]: "))
                
                if ask_business_owned_choice == 1:
                    hardware_store.grow_business()
                elif ask_business_owned_choice == 2:
                    ask_b_sell = input("\nDo you want to sell the business? [Y/n]: ").lower()
                    if ask_b_sell == 'y':
                        hardware_store.sell_business()
           
            elif business_owned_choice == 1 and hardware_store.availability == 'Yes':
                print("\nYou don't own this business!")
                
            
            elif business_owned_choice == 2 and night_club.availability == 'No':
                print("\n1. Grow the business")
                print("2. Sell the business")
                print("3. Go back to main menu")
                ask_business_owned_choice = int(input("\nChoose an option [1-3]: "))
                
                if ask_business_owned_choice == 1:
                    night_club.grow_business()
                elif ask_business_owned_choice == 2:
                    ask_b_sell = input("\nDo you want to sell the business? [Y/n]: ").lower()
                    if ask_b_sell == 'y':
                        night_club.sell_business()
                          
            elif business_owned_choice == 2 and night_club.availability == 'Yes':
                print("\nYou don't own this business!")    
                         
            elif business_owned_choice == 3 and cyber_cafe.availability == 'No':
                print("\n1. Grow the business")
                print("2. Sell the business")
                print("3. Go back to main menu")
                ask_business_owned_choice = int(input("\nChoose an option [1-3]: "))
                
                if ask_business_owned_choice == 1:
                    cyber_cafe.grow_business()
                elif ask_business_owned_choice == 2:
                    ask_b_sell = input("\nDo you want to sell the business? [Y/n]: ").lower()
                    if ask_b_sell == 'y':
                        cyber_cafe.sell_business()
                          
            elif business_owned_choice == 3 and cyber_cafe.availability == 'Yes':
                print("\nYou don't own this business!")       
             
            elif business_owned_choice == 4 and schneider.availability == 'No':
                print("\n1. Grow the business")
                print("2. Sell the business")
                print("3. Go back to main menu")
                ask_business_owned_choice = int(input("\nChoose an option [1-3]: "))
                
                if ask_business_owned_choice == 1:
                    schneider.grow_business()
                elif ask_business_owned_choice == 2:
                    ask_b_sell = input("\nDo you want to sell the business? [Y/n]: ").lower()
                    if ask_b_sell == 'y':
                        schneider.sell_business()
                          
            elif business_owned_choice == 4 and schneider.availability == 'Yes':
                print("\nYou don't own this business!")     
             
            elif business_owned_choice == 5 and radioactiv.availability == 'No':
                print("\n1. Grow the business")
                print("2. Sell the business")
                print("3. Go back to main menu")
                ask_business_owned_choice = int(input("\nChoose an option [1-3]: "))
                
                if ask_business_owned_choice == 1:
                    radioactiv.grow_business()
                elif ask_business_owned_choice == 2:
                    ask_b_sell = input("\nDo you want to sell the business? [Y/n]: ").lower()
                    if ask_b_sell == 'y':
                        radioactiv.sell_business()
                          
            elif business_owned_choice == 5 and radioactiv.availability == 'Yes':
                print("\nYou don't own this business!")     
                
            press_enter()
            

def hardware_store_summ(): # summary of the business
    print("\n------ ------ ------")
    print(f"The {hardware_store.name} is a russian electronic store specialized in old hardware.")
    print(f"This business can be yours for {hardware_store.price} $.")
    print(f"This business generates {hardware_store.income} $ per day. The rent, maintenance cost and other charges ammount to {hardware_store.charges} $ per day.")
    
def nightclub_summ():
    print("\n------ ------ ------")
    print(f"The {night_club.name} is a successful night club known all around the city.")
    print(f"Home to the most diverse clientele, this legendary business will cost you {night_club.price} $.")
    print(f"This business generates {night_club.income} $ per day. The rent, maintenance cost and other charges ammount to {night_club.charges} $ per day.")
    
def cyber_cafe_summ():
    print("\n------ ------ ------")
    print(f"Looking for a place to chill and disconnect... or reconnect? The {cyber_cafe.name} is the place to go.")
    print(f"Welcoming a wide variety of people, from netrunners to BD enthusiast, this hub is listed at {cyber_cafe.price} $.")
    print(f"This business generates {cyber_cafe.income} $ per day. The rent, maintenance cost and other charges ammount to {cyber_cafe.charges} $ per day.")
    
def schneider_summ():
    print("\n------ ------ ------")
    print(f"The {schneider.name} has been the center of attention in the business world with their ever-growing net worth and power.")
    print(f"49 years of excellence, more than 500 employees, the {schneider.name} is on sale for {schneider.price} $.")
    print(f"This business generates {schneider.income} $ per day. The rent, maintenance cost and other charges ammount to {schneider.charges} $ per day.")

def radioactiv_summ():
    print("\n------ ------ ------")
    print(f"The acid techno radio studio, {radioactiv.name}, is looking for a new owner!")
    print(f'"If you got the money, we got the... honey?! I mean... BUY IT NOW, FOR {radioactiv.price} $!!!"')
    print(f"This business generates {radioactiv.income} $ per day. The rent, maintenance cost and other charges ammount to {radioactiv.charges} $ per day.")
       
def kruger_select():
    print("------ ------ ------")
    print(f"| 1 | Name: {kruger.name}     | Price: {kruger.price} $    | Shares Owned: {kruger.shares} | Total Owned: {kruger.totaling()} $ | Change: {kruger.change_percent()} |")
    print("\n1. To buy shares.")
    print("2. To sell shares.")
    answer = int(input("Choose an option [1-2] or '0' to go back to the main menu:  "))
    if answer == 0:
        ...
    elif answer == 1:
        kruger.buy_stocks()
        press_enter()     
    elif answer == 2:
        kruger.sell_stocks()
        press_enter()
        
def mizotich_select():
    print("------ ------ ------")
    print(f"| 2 | Name: {mizotich.name}    | Price: {mizotich.price} $     | Shares Owned: {mizotich.shares} | Total Owned: {mizotich.totaling()} $ | Change: {mizotich.change_percent()} |")
    print("\n1. To buy shares.")
    print("2. To sell shares.")
    answer = int(input("Choose an option [1-2] or '0' to go back to the main menu:  "))
    if answer == 0:
        ...
    elif answer == 1:
        mizotich.buy_stocks()
        press_enter()
    elif answer == 2:
        mizotich.sell_stocks()
        press_enter()
        
def deluxo_select():
    print("------ ------ ------")
    print(f"| 3 | Name: {deluxo.name}    | Price: {deluxo.price} $     | Shares Owned: {deluxo.shares} | Total Owned: {deluxo.totaling()} $ | Change: {deluxo.change_percent()} |")
    print("\n1. To buy shares.")
    print("2. To sell shares.")
    answer = int(input("Choose an option [1-2] or '0' to go back to the main menu:  "))
    if answer == 0:
        ...
    elif answer == 1:
        deluxo.buy_stocks()
        press_enter()
    elif answer == 2:
        deluxo.sell_stocks()
        press_enter()
        
def biocorp_select():
    print("------ ------ ------")
    print(f"| 4 | Name: {biocorp.name} | Price: {biocorp.price} $      | Shares Owned: {biocorp.shares} | Total Owned: {biocorp.totaling()} $ | Change: {biocorp.change_percent()} |")
    print("\n1. To buy shares.")
    print("2. To sell shares.")
    answer = int(input("Choose an option [1-2] or '0' to go back to the main menu:  "))
    if answer == 0:
        ...
    elif answer == 1:
        biocorp.buy_stocks()
        press_enter()
    elif answer == 2:
        biocorp.sell_stocks()
        press_enter()
        
def zirton_select():
    print("------ ------ ------")
    print(f"| 5 | Name: {zirton.name}    | Price: {zirton.price} $     | Shares Owned: {zirton.shares} | Total Owned: {zirton.totaling()} $ | Change: {zirton.change_percent()} |")
    print("\n1. To buy shares.")
    print("2. To sell shares.")
    answer = int(input("Choose an option [1-2] or '0' to go back to the main menu:  "))
    if answer == 0:
        ...
    elif answer == 1:
        zirton.buy_stocks()
        press_enter()
    elif answer == 2:
        zirton.sell_stocks()
        press_enter()
# Main menu
def main_menu():
    
    day = 1 # Numbers of day since beginning of game. Starts at Day 1.    

    while True:
        try:
            print("\n------Main Menu------\n")
            print("1. Check account and date")
            print("2. Businesses")
            print("3. Investments")
            print("4. Marketplace")
            print("5. Advance to the next day")
            print("6. Quit")
            
            if player.money < 0: # Check for game over if the player's money goes below 0
                print("\nGame Over, you're bankrupt!\n")
                input("Press Enter to quit the game.")
                break
                
            def show_day():
                print(f"Today is day {day}")
            
            main_menu_choice = int(input("Choose an option [1-6]: "))
            
            if main_menu_choice == 1:
                print("------ ------ ------")
                show_day()
                player.showbalance()
                player.show_action_points()
                player.show_businesses()
                player.showcharges()
                press_enter()
                        
            elif main_menu_choice == 2:
                business_menu()
                
            elif main_menu_choice == 3:
                investments_menu()    
            
            elif main_menu_choice == 4:
                marketplace_menu()
                
            elif main_menu_choice == 5:
                print("------ ------ ------")  
                print("Advancing to the next day...\n")
                day += 1                                # Add a day to the day counter. Meaning, start of a new day
                
                kruger.slow_steady_fluctuations() # Change the values of the stock markets, fluctuations 
                mizotich.fluctuations()
                deluxo.big_fluctuations()
                biocorp.medium_fluctuations()
                zirton.fluctuations()
                devaluation()                     # Makes player's owned business lose value 
                reset_income()                    # Reset the income of the player to 0
                actualize_income_business()       # Adds the income of every owned business to the player's income
                               
                time.sleep(2)                       # simulates the change of day
                
                print(f"---Today is day {day}---")
                player.allocate_action()                    # reset the action counter based on the maximum action the player has
                player.newday()
                press_enter()
                
            elif main_menu_choice == 6: # to quit the game
                quit_sure = input("Are you sure? [Y/n]: ").lower()
                if quit_sure == 'y':
                    print("Exiting...")
                    break
                else:
                    continue 
        except ValueError:
            print("\nInvalid input.")
            press_enter()
       
main_menu()