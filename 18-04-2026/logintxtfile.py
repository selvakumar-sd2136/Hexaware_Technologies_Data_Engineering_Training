with open("logins.txt", "r") as f:
    users = [line.strip() for line in f]

# 1. Print all names
print(users)

# 2. Total logins
print("Total logins:", len(users))

# 3. Count each user
count = {}
for user in users:
    count[user] = count.get(user, 0) + 1
print("Login count:", count)

# 4. Most frequent user
top_user = max(count, key=count.get)
print("Most active:", top_user)

# 5. Unique users
print("Unique users:", set(users))