from folders import create_dir, remove_dir
from lists import list_choice
import os

create_dir()
print(os.listdir())
remove_dir()
print(list_choice([1, 2, 3, 4]))
