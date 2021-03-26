#what if you want an Optiona charater.
#if the charecter is or if its not, you dont really care.

import re
#Syntax in use : (text_to_be_found)?

super_human = re.compile("Super(wo)?man")
fav_hero = super_human.search("My fav superhero is Superwoman")
print(f"We found out that you favorite superhero is {fav_hero.group(1)}")
