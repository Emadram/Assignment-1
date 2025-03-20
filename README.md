Here’s everything formatted in GitHub-flavored Markdown with copyable code blocks:

# 🚀 Git Basics & GitHub Token Setup  

## **1. Git Basic Commands for Beginners**  

### **🔹 One-Time Git Setup**  
```sh
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

🔹 Initialize a Repository

git init

🔹 Clone a Repository

git clone <repository_url>

🔹 Check Repository Status

git status

🔹 Add Files to Staging

git add <filename>  # Add a specific file
git add .           # Add all changes

🔹 Commit Changes

git commit -m "Your commit message"

🔹 Check Commit History

git log

🔹 Push Changes to Remote Repository

git push origin <branch_name>

🔹 Pull Latest Changes from Remote

git pull origin <branch_name>

🔹 Create a New Branch

git branch <branch_name>

🔹 Switch Branches

git checkout <branch_name>

🔹 Merge Branches

git checkout main  
git merge <branch_name>

🔹 Check Remote URLs

git remote -v

🔹 Set Up a Remote Repository

git remote add origin <repository_url>

🔹 Undo Changes

git reset HEAD <file>   # Unstage a file
git checkout -- <file>  # Discard changes in working directory



⸻

2. Git Environment Setup

🔹 Install Git
	•	Windows: Download Git and install.
	•	Mac:

brew install git


	•	Linux:

sudo apt install git  # Ubuntu/Debian
sudo dnf install git  # Fedora



🔹 Check Git Installation

git --version

🔹 Generate SSH Key (Optional for Authentication)

ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

	•	Add the generated key to GitHub/GitLab settings.

⸻

3. How to Create a GitHub Personal Access Token (PAT) Step by Step

🔹 Step 1: Log in to GitHub
	•	Go to GitHub and sign in.

🔹 Step 2: Open Developer Settings
	•	Click your profile picture (top-right corner).
	•	Select “Settings” → “Developer settings”.

🔹 Step 3: Navigate to Personal Access Tokens
	•	Click “Personal access tokens” → “Tokens (classic)”.

🔹 Step 4: Generate a New Token
	•	Click “Generate new token” → “Generate new token (classic)”.

🔹 Step 5: Set Token Details
	•	Name: Add a descriptive name (e.g., “GitHub CLI Token”).
	•	Expiration: Choose an expiration date (or “No expiration”).
	•	Scopes: Select necessary permissions:
	•	For repo access: ✅ repo
	•	For pushing to a repo: ✅ workflow, ✅ write:packages, ✅ read:packages
	•	For authentication over HTTPS: ✅ gist (if needed)

🔹 Step 6: Generate and Copy the Token
	•	Click “Generate token”.
	•	Copy and save it safely (You won’t see it again).

🔹 Step 7: Use the Token in Git

When prompted for a password in Git over HTTPS, enter this token instead.

Example usage in Git:

git clone https://github.com/your-username/your-repo.git

Username: your-username
Password: [Paste the token here]

✅ Done! You now have a GitHub token for authentication. 🎉
