# Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available


customer_name = "sushant"
number_of_pass = 20
token_per_pass = 30
price_per_pass = 15
token_req_per_game = 1

total_tokens = number_of_pass * token_per_pass
total_cost = number_of_pass * price_per_pass
game_available = total_tokens // token_req_per_game


print("======Arcade Day Pass======")

print("Customer:" , customer_name)
print("passes:", number_of_pass)
print("Tokens:", total_tokens)
print("Total Cost: $" + str(total_cost))
print("Games Available: " + str(game_available))



