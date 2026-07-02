# Return Scope Questions:

# Question 1, Answer:
# 8
# 10

# Question 2, Answer:
# Spy
# 40
# Agent
# 2

# Question 3, Answer:
# 30
# 20

# Question 4, Answer:
# 70
# 35
# 100

# Question 5, Answer:
# ['map', 'key', 'torch', 'coin']
# ['map', 'key', 'torch', 'coin']

# Question 6, Answer:
# ['potion', 'shield']
# ['map', 'key']

# Question 7, Answer:
# 20
# 20

# Question 8, Answer:
# running
# ready
# waiting

# Question 9, Answer:
# 16
# 16
# 10

# Question 10, Answer:
# 25
# ['key', 'map', 'coin']
# 25
# ['key', 'map', 'coin']
# 1
# ['key', 'map', 'coin']

#python Return Practice
# question 1
def m_to_cm (distance):
    return distance*100

def message (cm):
    return f"Robot moved {cm} centimeters"

meters = 20
message (m_to_cm(meters))

# question 2
def add_ten (price):
    return price+10
def mulyiply_price (price):
    return price*2

price = 200
print (mulyiply_price(add_ten(price)))

# question 3
def full_name (fname, lname):
    return fname + " " + lname
def upper_case (name):
    return name.upper()

fn = "yaakov"
ln = "soibelman"
print (upper_case(full_name(fn,ln)))

# question 4
def to_fahrenheit (temp):
    return temp*1.8 +32
def result (temp):
    return f"the temp is {temp} degrees fahrenheit"
temp = 38
print (result(to_fahrenheit(temp)))

# question 5
def update_damaged_health (health, damage):
    return health - damage
def update_healed_health (dhealth,healing):
    return dhealth + healing
health = 100
damage = 50
healing = 30
print (update_healed_health( update_damaged_health(health, damage), healing))

# question 6
def total_price (a, b, c):
    return a+b+c
def discount (total_price):
    return total_price*0.8
def final_price (total_price):
    return f"the final price is {total_price}"
a=10
b=11
c=12
print (final_price(discount(total_price(a,b,c))))

# question 7
def clean_password (password):
    return password.strip()
def password_len (password):
    return len(password)
def has_8 (password_len):
    if password_len >= 8:
        return True
    else:
        return False
password = "123456789"
print (has_8(password_len(clean_password(password))))

# question 8
def bonus_5 (grade):
    return grade +5
def add_tenth (grade):
    return grade*1.1
def smaller_grade (grade):
    if grade < 100:
        return grade
    else:
        return 100
    
grade = 78
print (smaller_grade (add_tenth (bonus_5(grade))))

# question 9
def lower_sentence (sentence):
    return sentence.lower()
def count_a (sentence):
    return sentence.count("a")
def message (count_a):
    return f" the letter a appears {count_a} times"
sentence = "sdkj lkjsdf aasflk aasldkj asdlkj asicmad "
print (message(count_a(lower_sentence(sentence))))

# question 10
def total_value (price, amount):
    return price*amount
def lower_15(value):
    return value -15
def message (value):
    if value > 100:
        return True
    else:
        return False
    
price = 100
amount = 50
print (message(lower_15(total_value(price, amount))))
