#!/usr/bin/env python
# coding: utf-8

# # 1. Multi-Tier Tax Calculation for International Trade

# In[2]:


item_category = input("Enter the item_category (Electronics): ")
value_of_item = int(input("Enter Value of the item: "))
country_of_import = input("Enter the country economic status (Developing): ")
Eco_friendly = input("Is the Item Eco-friendly // True or False: ")

tax_charged = 0
value_after_tax = 0
tax_discount = 0
value_after_tax_discount = 0
custom_duty = 0
value_after_custom_duty = 0

if item_category == "Electronics" and value_of_item > 50000:
    tax_charged = value_of_item*25/100
    value_after_tax = value_of_item - tax_charged
    print("Tax on Electronic and value exceeding 50,000 is: ",tax_charged)
    print("Value after tax: ",value_after_tax)
    
    if Eco_friendly == "True":
        tax_discount = value_after_tax*5/100
        value_after_tax_discount = value_after_tax + tax_discount
        print("discount on Tax: ",tax_discount)
        print("Value after discount on tax: ",value_after_tax_discount)
    
elif country_of_import == "Developing" and 10000 < value_of_item < 50000:
    custom_duty = value_of_item*15/100
    value_after_custom_duty = value_of_item - custom_duty
    print("Custom Duty on Developing and value between 10000 and 50000: ",custom_duty)
    print("Value after Custom Duty: ",value_after_custom_duty)
    
    if Eco_friendly == "True":
        tax_discount = value_after_custom_duty*5/100
        value_after_tax_discount = value_after_custom_duty + tax_discount
        print("discount Tax: ",tax_discount)
        print("Value after discount on tax: ",value_after_tax_discount)

elif Eco_friendly == "True":
    tax_discount = value_of_item*5/100
    value_after_tax_discount = value_of_item + tax_discount
    print("discount Tax: ",tax_discount)
    print("Value after discount on tax: ",value_after_tax_discount)
    
else:
    print("No tax charged , No custom-duty charged and no discount on tax")


# # 2. Dynamic Risk Assessment for Financial Loans

# In[4]:


credit_score = int(input("Enter Credir Score:\n"))
loan = int(input("Enter loan: \n"))
income = int(input("Etner income: \n"))
co_signer = input("Do applicant has a co-signer:\n")

if credit_score<600 and loan>100000:
    print("High Risk")
    if co_signer=="Yes":
        print("Risk is reduced to Moderate risk")

elif 600<=credit_score<=750 and income<50000:
    print("Moderate risk")
    if co_signer=="Yes":
        print("Risk is reduced to low risk")

elif credit_score>750 and income>100000:
    print("Low risk")
    
else:
    print("applicant do not meet any requirements")


# # 3. Multi-Criteria Stock Replenishment Decision

# In[10]:


stock_level = int(input("Enter stock level:\n"))
avg_monthly_sales = int(input("Enter monthly sales:\n"))
expiry_date = int(input("Enter expiry date in days:\n"))

if 0<stock_level<10 and avg_monthly_sales>50:
    print("Urgent Replenishment")

elif 10<=stock_level<=50 and 20<=avg_monthly_sales<=50:
    print("Moderate Replenishment")

elif expiry_date<=30:
    print("Do not replenish")

else:
    print("Normal Stock")


# # 4. Personalized Insurance Premium Adjustment

# In[15]:


age = int(input("Enter your age:\n"))
accidents = int(input("Enter accidents:\n"))
accidents_5_years = int(input("Enter number of accidents in 5 years:\n"))
vehicle_type = input("Enter vehicle type(electric or hybrid):\n")
high_crime_area = input("does applicant lives in high-crime area(Yes/No):\n")
surcharge = 25
discount = 15
eco_discount = 10
high_crime_premium = 20
final_premium = 0
extra_premium = 0

if age<25 and accidents>2:
    print("surcharge on premium is: ",surcharge,"%")
    final_premium = final_premium + surcharge
    
    if high_crime_area=="Yes":
        print("Premium charged is :",high_crime_premium,"%")
        final_premium = final_premium + high_crime_premium
    
    if vehicle_type== "electric" or "hybrid":
        print("Eco-Discount: ",eco_discount,"%")
        final_premium = final_premium - eco_discount
        
    if final_premium>30:
        print("Premium cannot exceed 30")
        extra_premium = final_premium - 30
        final_premium = final_premium - extra_premium
        
    
elif age>50 and accidents_5_years==0:
    print("Discount received: ",discount,"%")
    final_premium = final_premium - discount
    
    if high_crime_area=="Yes":
        print("Premium charged is :",high_crime_premium,"%")
        final_premium = final_premium + high_crime_premium
        
    if vehicle_type== "electric" or "hybrid":
        print("Eco-Discount: ",eco_discount,"%")
        final_premium = final_premium - eco_discount
    
elif vehicle_type == "electric" or vehicle_type == "hybrid":
    print("Eco-Discount: ",eco_discount,"%")
    final_premium = final_premium - eco_discount
    
    if high_crime_area=="Yes":
        print("Premium charged is :",high_crime_premium,"%")
        final_premium = final_premium + high_crime_premium
    
elif high_crime_area=="Yes":
    print("Premium charged is :",high_crime_premium,"%")
    final_premium = final_premium + high_crime_premium

print("Final premium charged:",final_premium)


# # 5. Complex Employee Compensation Adjustment

# In[2]:


exp = int(input("Enter experience:\n"))
cur_salary = int(input("Enter current salary:\n"))
department = input("Is employee in research & development(Yes/No):\n")
last_quarter_profit = int(input("Enter last quarter profit:\n"))
performance = input("Did the employess get 2 consecutive excellent(Yes/No):\n")
avg_salary = 50000
max_increment = 25

salary_inc = 0
bonus= 0
salary_inc_2 = 0

if exp>10 and cur_salary < avg_salary:
    salary_inc = cur_salary * 0.15
    cur_salary = cur_salary + salary_inc
    print("Current Salary after 15% salary increase:\n",cur_salary)
    
    if department == "Yes" and last_quarter_profit>20:
        bonus = cur_salary * 0.10
        cur_salary = cur_salary + bonus
        print("Current salary after 10% bonus:\n",cur_salary)
    if performance == "Yes":
        salary_inc_2 = cur_salary * 0.05
        cur_salary = cur_salary + salary_inc_2
        print("Current salary after 5% salary increase:\n",cur_salary)

elif department == "Yes" and last_quarter_profit>20:
    bonus = cur_salary * 0.10
    cur_salary = cur_salary + bonus
    print("Current salary after 10% bonus:\n",cur_salary)
    
    if performance == "Yes":
        salary_inc_2 = cur_salary * 0.05
        cur_salary = cur_salary + salary_inc_2
        print("Current salary after 5% salary increase:\n",cur_salary)
        
elif performance == "Yes":
    salary_inc_2 = cur_salary * 0.05
    cur_salary = cur_salary + salary_inc_2
    print("Current salary after 5% salary increase:\n",cur_salary)
    
print("Final salary:\n",cur_salary)


# # 6. Advanced Real Estate Pricing Model

# In[3]:


luxury = input("Is the market marked as luxury segment(Yes/No):\n")
property_price = int(input("Enter property price:\n"))
location = input("Enter property location(city center):\n")
area = int(input("Enter the area of property:\n"))
property_age = int(input("Etner the age of property:\n"))
certification = input("Is the property certified green(Yes/No):\n")
new_market_trend = int(input("Enter new market trend:\n"))

market_trend = 20
premium = 0
eco_premium = 0
discount = 0
fixed_premium = 50000

if luxury == "No":
    if location == "city center" and area>3000:
        premium = property_price*0.25
        property_price = property_price+premium
        print("Property price after premium is: ",property_price)

        if property_age<5 and certification == "Yes":
            eco_premium = property_price*0.15
            property_price = property_price + eco_premium
            print("Property price after eco premium is: ",property_price)

        if new_market_trend - market_trend <= market_trend*0.10 and property_age>15:
            discount = property_price*0.10
            property_price = property_price - discount
            print("New price after discount allowed is: ",property_price)

    elif property_age<5 and certification == "Yes":
        eco_premium = property_price*0.15
        property_price = property_price + eco_premium
        print("Property price after eco premium is: ",property_price)

    elif new_market_trend-market_trend <= market_trend*0.10 and property_age>15:
        discount = property_price*0.10
        property_price = property_price - discount
        print("New price after discount allowed is: ",property_price)

elif luxury == "Yes":
    property_price = property_price + fixed_premium
    
print("Final property price is: ",property_price)


# # 7. Advanced Healthcare Prioritization System

# In[1]:


age = int(input("Enter your age:\n"))
condition = input("Critical or Non-Critical:\n")
illness = input("Enter Illness(chronic/communicable):\n")

if age>70 and illness == "chronic":
    print("Top Priority")

elif condition == "critical"  and illess == "chronic":
    print("High Priority")
    
elif condition == "non-critical" and illness == "communicable":
    print("Moderate Priority")
    
else:
    print("Low Priority")


# # 8. Advanced Marketing Campaign Segmentation

# In[1]:


# For a marketing campaign:
# If the customer has spent over $5,000 in the last year and their engagement score exceeds 80, target them with a "Premium Rewards Campaign."
# If the customer has spent between $1,000 and $5,000 and their engagement score is between 50 and 80, target them with a "Loyalty Program."
# If the customer has spent less than $1,000, but their engagement score exceeds 90, target them with a "Re-engagement Campaign."
# Otherwise, exclude the customer from the campaign.

spent = int(input("Enter money spent:\n"))
engagement_score = int(input("Enter your engagement score(1-100):\n"))

if spent > 5000 and engagement_score >80:
    print("Premium Reward")

elif 1000<spent<5000 and 50<engagement_score<80:
    print("Loyalty Program")

elif spent<1000 and engagement_score > 90:
    print("Re-engagement Campaign")

else:
    print("Exclude the cumtomer")


# # Dict

# # Q1

# In[2]:


a = {
    "d":"no"
}

a.get("discount","Not Available")


# # Q2

# In[14]:


b = {
    "price":1,
    "cost":2
}

if b.get("price") > b.get("cost"):
    print("Price is higher than cost")
    
elif b.get("price") < b.get("cost"):
    print("Price is lower than cost")

elif b.get("price") == b.get("cost"):
    print("price is equal to cost")
    

# Another method

b = {
    "price":1,
    "cost":2
}

if b["price"] > b["cost"]:
    print("Price is higher than cost")
    
elif b["price"] < b["cost"]:
    print("Price is lower than cost")

elif b["price"] == b["cost"]:
    print("price is equal to cost")
    


# # Q3

# In[10]:


c = {
    "employee":{"salary":10000,
               "age":21},
    "designation":"Monkey"
}

c["employee"]["salary"]


# # Q4

# In[25]:


d = {
    "income":[600000,300000,100000]
}

tax = 0
n = 0

for i in d["income"]:
    if d["income"][n] > 500000:
        tax = d["income"][n]*0.2
        print(tax,"on salary > 500000")
        n += 1

    elif 250000 <= d["income"][n] <= 500000:
        tax = d["income"][n]*0.1
        print(tax,"on salary between 250000 and 500000")
        n += 1

    elif d["income"][n] < 250000:
        tax = d["income"][n]*0.05
        print(tax,"on salary < 2500000")
        n += 1


# # Q5

# In[45]:


e = {
    "age":[12,23,54,61]
}

n = 0

for i in e["age"]:
    if 0 < e["age"][n] <= 12:
        print("child")
        n += 1

    elif 13 <= e["age"][n] <= 19:
        print("teen")
        n += 1

    elif 20 <= e["age"][n] <= 59:
        print("adult")
        n += 1

    elif e["age"][n] > 60:
        print("senior")
        n += 1        


# # Q6

# In[1]:


f = {
    "name":"admin"
}

if f.get("name") == "admin":
    print("Yes")


# # Q7

# In[23]:


g = {"mode": "upper",
        "message": "Hello World"
       }

if g["mode"] == "lower":
    print(g["message"].lower())
    
elif g["mode"] == "upper":
    print(g["message"].upper())
    
else:
    print("Invalid mode")


# # Q8

# In[37]:


h = {
    "username":"monkey_100"
}

y = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_"

if h["username"].isalpha() and h["username"].isdigit():
    print("valid")
    
else:
    print("not valid")


# # Q9 Incorrect

# In[25]:


dict = {
    "password":"India@"
}

a = dict["password"]
b = "!@#$%^&*"

if b in a:
    print("strong")  
elif a.isdigit():
    print("weak")  
else:
    print("medium")


# # Q10

# In[2]:


a = input("filename: ")

if a.endswith(".txt"):
    print("Text File")
elif a.endswith(".jpg") or a.endswith(".png"):
    print("Image File")


# # Q11

# In[4]:


dict = {
    "number":(1,2,3)
}
b = dict["number"]

for i in b:
    if i%2==0:
        print("even")
    else:
        print("odd")


# # Q12

# In[7]:


password = "123"

for i in range(3):
    password_input = input("Enter password: ")
    if password_input=="123":
        print("correct")
        break
    else:
        print("incorrect")


# # Q13

# In[9]:


temp = int(input("enter temp: "))

if temp>40:
    print("heatwave warning")
elif 30<temp<40:
    print("hot")
else:
    print("normal")


# # Q14

# In[10]:


purchase_amount = int(input("enter temp: "))

if purchase_amount>5000:
    discount = purchase_amount*0.20
    purchase_amount = purchase_amount - discount
    print(purchase_amount)
elif 2000<purchase_amount<5000:
    discount = purchase_amount*0.10
    purchase_amount = purchase_amount - discount
    print(purchase_amount)
else:
    print("no discount")


# # Q15

# In[3]:


account_type = input("enter account type: ")
balance = int(input("enter balance: "))

if account_type.lower() == "gold" and balance > 10000:
    print("Premium")
else:
    print("standard access")


# # Q16

# In[8]:


dict = {
    "name":"a",
    "email":"b",
    "phone":12
}

if "name" in dict and "email" in dict and "phone" in dict:
    print("complete")
    
else:
    print("incomplete")


# # Q17

# In[10]:


age = int(input("enter age: "))
vision = input("enter vision status: ")

if age>=18 and vision.lower() == "clear":
    print("eligible")
else:
    print("not eligible")


# # Q18

# In[13]:


smoker = input("are you a smoker: ")
age = int(input("enter age: "))

if smoker.lower()=="true" and age>50:
    print("insurance premium is increased by 25%")


# # Q19

# In[14]:


os = input("Enter Os: ")
ram = int(input("enter ram: "))

if os.lower() == "windows" and ram>8:
    print("software compatibility")
else:
    print("upgrade required")


# # Q20

# In[17]:


username = input("enter username: ")
password = input("enter password: ")

if username == "anu" and password != "123":
    print("wrong password")
elif username != "anu" and password != "123":
    print("invalid credentials")
elif username == "anu" and password == "123":
    print("login successful")


# # Lists:

# In[1]:


# 1 Write a program to find the sum of all elements in a list.
a = [1,2,3,4,5]
b = 0

for i in a:
    b = b + i
b


# In[6]:


# 2 Create a list of numbers and find the maximum value using a for loop.
a = [1,2,3,4,5]
b = 0
for i in a:
    if i>b:
        b = i
b


# In[5]:


# 3 Given a list of words, count the number of words that start with the letter 'A'.
a = ["aapple","mango","attribute"]
b = 0
for i in a:
    if i[0]=="a":
        b+=1
b


# In[29]:


# 4 Write a program to find the average of all the elements in a list.
a = [1,2,3,4,5]
b = 0
c = 0
for i in a:
    b += i
    c += 1
print(b/c)


# In[30]:


# 5 Create a list of numbers and calculate the product of all the elements.
a = [1,2,3,4,5]
b = 1

for i in a:
    b *= i
b


# In[61]:


# 6 Given a list of names, print each name in reverse order.
a = ["python","new"]

for i in a:
    print(i[::-1])


# In[73]:


# 7 Write a program to reverse a list.
a = ["python","new"]
b = ""
for i in a:
    for j in i:
        b = j+b
print(b)

c = [1,2,3,4,5]
d = []
for i in c:
    d.insert(0,i)
print(d)


# In[80]:


# 8 Create a list of even numbers and find their average.
a = [1,2,3,4,5,6,7,8]
d = []
b = 0
c = 0

for i in a:
    if i%2==0:
        d.append(i)

for i in d:
    b += i
    c += 1
print(d)
b/c


# In[84]:


# 9 Given a list of words, count the number of words that end with the letter 's'.
a = ["appels","mangos","planes"]
b = 0

for i in a:
    if i[-1]=="s":
        b += 1
b


# In[89]:


# 10 Check if a list is a palindrome (reads the same forwards and backwards).
a = ["civic","level", "apple","refer","mango"]

for i in a:
        if i == i[::-1]:
            print("palindrome")
        else:
            print("not palindrome")


# In[93]:


# 11 Remove all duplicate elements from a list.
a = ["apple","mango","apple"]
b = []  

for i in a:  
    if i not in b:  
        b.append(i)  

print(b)

a = [1, 2, 3, 2, 4, 1, 5]  
b = []  

for i in a:  
    if i not in b:  
        b.append(i)  

print(b)


# # Strings:
# 
# 9. Count the number of words with a specific length in a sentence.
# 10. Find the first non-repeated character in a string.
# 11. Reverse the order of words in a sentence.

# In[2]:


# 1 Write a program to count the number of vowels in a given string.
a = 'apple'
b = 0
c = "aeiou"
for i in a:
    if i in c:
        b = b+1
b


# In[3]:


# 2 Given a string, reverse it using a for loop.
a = "apple"
b =""
for i in a:
    b = i+b
b


# In[4]:


# 3 Create a string and check if it is a palindrome (reads the same forwards and backwards).
a = "refer"
if a==a[::-1]:
    print("palindrome")
else:
    print("not palindrome")


# In[1]:


# 4 Write a program to remove all spaces from a string using a for loop.
a = "apple is a fruit"
b = "abcdefghijklmnopqrstuvwxyz"
c = ""

for i in a:
    if i in b:
        c = c+i
c


# In[6]:


# 5 Count the number of occurrences of a specific character in a string.
a = "apple is a fruit"
spe_alp = input("Enter specific alphabet: ")
b = 0

for i in a:
    if i==spe_alp:
        b = b+1
b


# In[8]:


# 6 Remove all special characters and punctuation from a string.
a = "apple, is a fruit !@#$ "
b = "abcdefghijklmnopqrstuvwxyz "
c = ""

for i in a:
    if i in b:
        c = c+i
c


# In[18]:


# 7 Count the number of times a specific substring appears in a larger string.
a = "apple apple is a fruit"
b = 0
c = "abcdefghijklmnopqrstuvwxyz "
d = ""

for i in a:
    if i.endswith(c):
        d = d+i
d


# # Doubt

# In[1]:


# 7 Count the number of times a specific substring appears in a larger string.
a = "apple apple is a fruit"
b = 0
c = a.split()
t = input()
for i in c:
    if i == t:
        b = b+1
b


# In[7]:


# 8 Given a string, print every third character.
a = "apoapos"

print(a[::2])


# # Doubt

# In[6]:


# 9 Count the number of words with a specific length in a sentence.
a = "apple is a fruit"
b = 0
c = a.split()
r=5
for i in c:
    if len(i)==r:
        b+=1
b


# In[ ]:


# 10 Find the first non-repeated character in a string.
a = "apple apple is a fruit"

for i in a:
    if i 


# # Tuples:

# In[2]:


# 1 Create a tuple of numbers and find the sum of all the elements.
a = (1,2,3,4,5)
b = 0
for i in a:
    b = b+i
b


# In[31]:


# 2 Given a tuple of words, find the word with the longest length.
a = ("apple","alphabet","mang")
b = 0
for i in a:
    if len(i)>b:
        b = len(i)

for j in a:
    if b == len(j):
        print(j)


# In[33]:


# 3 Write a program to check if a specific element exists in a tuple.
a = (1,"apple")
b = int(input("Enter Number: "))
c = input("Enter Word: ")

for i in a:
    if i==b:
        print(b,"exists in tuple")
    if i==c:
        print(c,"exists in tuple")


# In[47]:


# 4 Find the index of a particular element in a tuple.
a = ("apple","mango","banana")
b = input("Enter Word: ")
c = -1

for i in a:
    c = c+1
    if i==b:
        print(a[c])
        break
a[c]


# In[49]:


# 5 Given a tuple of numbers, count the number of odd numbers.
a = (1,2,3,4,5,6,7)
b = 0

for i in a:
    if i%2 != 0:
        b += 1
b


# In[57]:


# 6 Find and print all the unique elements in a tuple.
a = ("apple","mango","apple","mango")
b = []
for i in a:
    if i not in b:
        b.append(i)
b 


# In[78]:


# 7 Check if all elements in a tuple are equal.
a = (1,1,1,1,1,2)
b = a[0]
c = True
for i in a:
    if i!=b:
        c = False
        break
if c:
    print("same")
else:
    print("no")


# In[80]:


# 8 Create a tuple of mixed data types and separate elements into different lists based on their data type.
a = ("apple",1,"mango",2)
b = []
c = []

for i in a:
    if type(i)==str:
        b.append(i)
    else:
        c.append(i)
print(b)
print(c)


# In[86]:


# 9 Find the average of all elements in a tuple of floats.
a = (1.1,2.1,3.1,4.1,5.1)
b = 0
c = 0

for i in a:
    b = b+i
    c = c+1
b/c


# # Sets:

# In[2]:


# 1 Create two sets of numbers and find the intersection of the two sets using a for loop.
a = {1,2,3,4,5}
b = {3,4,5,6,7}

for i in a:
    if i in b:
        print(i)


# In[6]:


# 2 Given a set of words, print all the unique vowels present in the words.
a = {"apple","mango","banana","pine"}
b = ("aeiou")
c = []
for i in a:
    for j in i:
        if j in b:
            if j not in c:
                c.append(j) 
c


# In[7]:


# 3 Write a program to remove duplicates from a set using a for loop.
a = {1,1,2,3}
b = []
for i in a:
    if i not in b:
        b.append(i)
b


# In[11]:


# 4 Calculate the union of two sets of numbers.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = []
d = 0
for i in a:
    c.append(i)
for i in b:
    if i not in c:
        c.append(i)

for i in c:
    d = d+i
d


# In[4]:


# 5 Check if one set is a subset of another set.
a = {1, 2, 3, 4}
b = {3,4,5}
c = []
d = []
for i in b:
    if i in a:
        c.append(i)
    else:
        d.append(i)
print(c)
d


# In[2]:


# 6 Find the symmetric difference between two sets.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = []

for i in a:
    if i not in b:
        c.append(i)

for i in b:
    if i not in a:
        c.append(i)
c


# In[12]:


# 7 Given a set of numbers, find the largest and smallest values.
a = {1,2,3,4,5,6}
b = 0
for i in a:
    if i>b:
        b=i
c=b
for j in a:
    if j<c:
        c=j
print(b,"is the largest number")
print(c,"is the smallest number")


# In[18]:


# 8. Create a set of colors and print all the colors that contain the letter 'e'.
a = {"red","black","blue"}
for i in a:
    for j in i:
        if j=="e":
            print(i)


# In[46]:


# 9. Count the number of prime numbers in a set of integers.
a = {2,3,4,5,6,7,8,37}
for i in a:
    for j in range(2,i):
        if i%j==0:
            print("np")
            break
    else:
        print(i)
        


# In[52]:


# Q10 check if 2 sets are disjoint
a = {1,2,3}
b = {4,5,6}
for i in a:
    if i in b:
        print(i,"is common element in both sets")
        break
else:
    print("disjoint")


# In[69]:


# 11. Write a program to remove all elements from a set that are divisible by 3.
a = {1, 2, 3, 4, 5}
for i in list(a):  # Convert set to a list to avoid modification issues
    if i % 3 == 0:
        a.remove(i)
print(a)


# # List

# In[1]:


# Q1 
a = [76,77,78,50,51,52,49,48,47]
im = 1
tm = 0

for i in range(1,len(a)):
    if a[i] > a[i-1]:
        im+=1
        if im>tm:
            
    else:
        im=0


# In[6]:


# Q2
marks = [71,72,73,74,7,76,79,78]
im = 0
tim = 0
dm = 0
tdm = 0
im_70 = 0
tim_70 = 0

for i in range(1,len(marks)):
    if marks[i] > marks[i-1] and marks[i]<70 and marks[i-1]<70:
        im+=1
        if tim<im:
            tim=im
    else:
        im = 0
        
for i in range(1,len(marks)):
    if marks[i] < marks[i-1]:
        dm+=1
        if tdm<dm:
            tdm=dm
    else:
        dm=0
    
for i in range(1,len(marks)):
    if marks[i] > marks[i-1] and marks[i]>70 and marks[i-1]>70:
        im_70 +=1
        if tim_70<im_70:
            tim_70=im_70
    else:
        im_70 = 0
        
print(im)
print(tim)

print(dm)
print(tdm)

print(im_70)
print(tim_70)


# In[1]:


# Q3
traffic = [1050,980,1120,875,1300,1500,1250]
c = 0
c_d = 0
d1 = 0
tt = []
d2 = 0

for i in range(1,len(traffic)):
    if traffic[i]>traffic[i-1]:
        c+=1
        if c_d<c:
            c_d=c
    else:
        c=0
print(c_d)
for i in range(1,len(traffic)):
    if traffic[i]<traffic[i-1]:
        d1 = traffic[i-1] - traffic[i]
        tt.append(d1)
        
for i in range(1,len(tt)):
    if tt[i]>tt[i-1]:
        d2 = tt[i]
    else:
        d2 = tt[i-1]
        
print(tt)        
print(d2)


# In[6]:


# Q4
salaries = [45000, 52000, 38000, 60000, 120000]

for i in salaries:
    if i < 40000:
        bl4 = i*0.15 + i
        print(bl4)
    elif 40000<=i<=70000:
        be47 = i*0.10 + i
        print(be47)
    elif 70000<i<=100000:
        be710 = i*0.05 + i
        print(be710)
    else:
        a10 = i*0.03 + i
        print(a10)


# In[25]:


# Q5
# 1.	Identify items that remained out of stock for 3 consecutive days or more.
# 2.	Determine the product with the most frequent stock-outs.
# 3.	Identify items that required urgent restocking (quantity below 5 for more than 5 days).

stocks = [[15, 0, 8, 23, 9, 0, 45, 1, 2, 3, 4], [0, 0, 0, 5, 12, 3, 8]]
more_3_0 = 0
tmore_3_0 = 0
stock_out = 0
stock_out_1 = 0
stock_5_0 = 0
stock_5_1 = 0

for j in range(0,len(stocks)):
    for i in range(0,len(stocks[j])):
        if stocks[j][i]==0:
            more_3_0+=1
            if more_3_0==3:
                tmore_3_0=more_3_0
                print(stocks[j],"is the product, that remained out of stock for 3 consecutive days")
        else:
            more_3_0 = 0

            
for i in range(0,len(stocks[0])):
    if stocks[0][i]==0:
        stock_out+=1
for i in range(0,len(stocks[1])):
    if stocks[1][i]==0:
        stock_out_1+=1
if stock_out>stock_out_1:
    print(stocks[0],"has more frequent stock outs")
else:
    print(stocks[1],"has more frequent stock outs")


for i in range(0,len(stocks[0])):
    if stocks[0][i]<5:
        stock_5_0+=1
for i in range(0,len(stocks[1])):
    if stocks[1][i]<5:
        stock_5_1+=1
if stock_5_0>5:
    print(stocks[0],"urgent restocking")
if stock_5_1>5:
    print(stocks[1],"urgent restocking")


# In[23]:


# Q6
orders = [{
    "amount": 1200,
    "status": "paid",
    "delivery": 2,
    "attempts": 4
},{
    "amount": 4500,
    "status": "failed",
    "attempts": 4
},{
    "amount": 4500,
    "status": "pending",
    "delivery": 7,
    "attempts": 4
}]

a = 0
for i in orders:
    if orders[a]["status"]=="paid" and orders[a]["delivery"]<=3:
        print("Low Risk",a)
    elif orders[a]["status"]=="pending" and orders[a]["delivery"]>5:
        print("Medium Risk",a)
    elif orders[a]["status"]=="failed" and orders[a]["attempts"]>3:
        print("High Risk",a)
    a+=1


# # DOUBT

# In[14]:


# Q7
t = [12, 9, 8, 7, 10, 15, 17, 20, 19, 18, 18, 16, 14]
drop = 0
spike = 0
b_spike = 0
b_drop = 0

for i in range(1,len(t)):
    if t[i]>t[i-1]:
        spike = t[i]-t[i-1]
        if b_spike<spike:
            b_spike=spike
    else:
        drop = t[i-1]-t[i]
        if b_drop<drop:
            b_drop=drop

print(b_drop)
print(b_spike)

d_stable = 0
s_stable = 0

for i in range(1,len(t)):
    if t[i]>t[i-1]:
        spike = t[i]-t[i-1]
        if spike<=2:
            s_stable+=1
    else:
        drop = t[i-1]-t[i]
        if drop<=2:
            d_stable+=1
            
print(d_stable)
print(s_stable)


# In[6]:


t = [12, 9, 8, 7, 10, 15, 17, 20, 19, 18, 18, 16, 14 ,1,2,3,4]
cold = 0
b = 0
for i in t:
    if i<10:
        cold+=1
        b = max(b,cold)
    else:
        cold = 0
print(b)


# In[ ]:


i = 12
i = 9 ,if 9<10 ,c=+1, l = max(0,1)==1, l=1
i = 8 ,


# In[51]:


# Q8
tran = [{
    "account": "A123",
    "amount": 45000,
    "status": "failed"
},{
   "account": "A123",
    "amount": 50000,
    "status": "failed"
},{
   "account": "A123",
    "amount": 50000,
    "status": "passed" 
},{
    "account": "A123",
    "amount": 50000,
    "status": "failed"
},{
    "account": "A123",
    "amount": 50000,
    "status": "failed"
},{
    "account": "A123",
    "amount": 50000,
    "status": "failed"
}]

a = 0
failed = 0
t_failed = 0

for i in tran:
    if a>=len(tran)-1:
        a-=1
    if i["status"]=="failed" and tran[a+1]["status"]=="failed":
        failed+=1
        if t_failed<failed:
            t_failed=failed
    else:
        failed = 0
    a+=1
print(failed)
print(t_failed)


# In[9]:


x = 456
b = 0
while x!=0:
    a = x%10
    b = b+a
    x //= 10
b


# In[ ]:


x = int(input("Enter Number: "))
b = 0
while x!=0:
    a = x%10
    


# # new

# In[16]:


# 2. Reverse Digits Without String Conversion:
# Take an integer as input and reverse its digits without converting it into a string.

a = int(input("Enter a number: "))
b = 0

while a > 0:
    b = b * 10 + a % 10
    a //= 10

print("Reversed:", b)


# In[14]:


# 3. Repeated Digit Extraction:
# Write a while loop program that extracts and prints the repeated digits in a given integer.

a = int(input("Enter number: "))
c = set()
d = set()
while a>0:
    b = a%10
    a //= 10
    if b not in c:
        c.add(b)
    else:
        d.add(b)
d


# In[31]:


# 4 Find the Smallest and Largest Digits in a Number:
# Given an integer, find the smallest and largest digits using a while loop.

a = int(input("Enter Number: "))
s = 9
b = 0

while a>0:
    z = a%10
    if z>b:
        b=z
    if z<s:
        s=z
    a //= 10
print(s)
print(b)


# In[21]:


# 5. Custom Collatz Sequence:
# Modify the standard Collatz sequence: if the number is even, divide it by 2; if odd,
# multiply by 3 and add 1. However, if a number is divisible by 5, subtract 1 instead of multiplying.

a = int(input())
b = 1

while b>0:
    if a%2==0 and a%5!=0:
        print("Even")
        print(a//2)
    elif a%2!=0:
        print("Odd")
        print((a*3)+1)
    elif a%5==0:
        print("5")
        print(a-1)
    b-=1


# In[114]:


# Bank account system,
# if 1 show details, 
# if 2 show balance,
# if 3 add money, 
# if 4 withdraw ,if withdraw is more than acc balance show insufficient balance
# if 5 exit


# In[17]:


bank_detail = {
    "Name":"Max",
    "Acc ID":312341241,
    "Balance":2000
}


# In[18]:


class Bank:
    
    def __init__(self):
        self.a = int(input("""Enter number
        1 (Bank details)
        2 (Bank Balance)
        3 (Deposit)
        4 (Withdraw)
        5 (Exit): """))
        
    def bank(self):
        
        if self.a==1:
            print(bank_detail)
        
        elif self.a==2:
            print(bank_detail["Balance"])
    
        elif self.a==3:
            deposit = int(input("Enter amount you want to deposit: "))
            bank_detail["Balance"] += deposit
            print(bank_detail["Balance"])
        
        elif self.a==4:
            withdraw = int(input("Enter amount you want to withdraw: "))
            bank_detail["Balance"] -= withdraw
            print(bank_detail["Balance"])
            
        elif self.a==5:
            print("Exiting the protocol")
            
        else:
            print(f"{self.a} is not specified , re-enter the number")


# In[19]:


x = Bank()
x.bank()


# In[ ]:





# In[ ]:





# In[ ]:




