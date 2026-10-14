import os
from datetime import datetime, timedelta
import random

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

days_back = 365 
start_date = datetime.now() - timedelta(days=days_back)

for i in range(days_back + 1):
    current_date = start_date + timedelta(days=i)
    formatted_date = current_date.strftime("%Y-%m-%dT12:00:00")
    
    commits_for_today = random.randint(0, 100)

    if commits_for_today > 0:
        for _ in range(commits_for_today):
            os.environ["GIT_COMMITTER_DATE"] = formatted_date
            os.environ["GIT_AUTHOR_DATE"] = formatted_date
            
            cmd = 'git commit --allow-empty -m "Fake commit" -q'
            os.system(cmd)
            
        print(f"{GREEN}✅ Commits made for: {formatted_date}. Total: {commits_for_today}{RESET}")
    else:
        print(f"No commits for: {formatted_date}")

print(f"{RED}💥 Operation complete! Your local history has been modified. Push to update the remote.{RESET}")