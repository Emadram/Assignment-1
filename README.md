# 🚀 Git Setup & Usage for Assignments

## **1. Git Environment Setup (Windows)**  

### **🔹 Install Git**  
- **Download Git for Windows**: [Git Website](https://git-scm.com/downloads)  
- Install it using default settings.

### **🔹 Check Git Installation

```
git --version
```

## **2. Create a GitHub Personal Access Token (PAT)**  

### **🔹 Step 1: Log in to GitHub**  
- Go to [GitHub](https://github.com/) and sign in.

### **🔹 Step 2: Open Developer Settings**  
- Click your profile picture (top-right corner).  
- Select **"Settings"** → **"Developer settings"**.  

### **🔹 Step 3: Navigate to Personal Access Tokens**  
- Click **"Personal access tokens"** → **"Tokens (classic)"**.  

### **🔹 Step 4: Generate a New Token**  
- Click **"Generate new token"** → **"Generate new token (classic)"**.  

### **🔹 Step 5: Set Token Details**  
- **Name**: Add a descriptive name (e.g., "GitHub Token").  
- **Expiration**: Choose an expiration date (or "No expiration").  
- **Scopes**: Check these permissions:
  - ✅ **repo** (Full access to repositories)
  - ✅ **workflow** (For CI/CD)
  - ✅ **write:packages** & ✅ **read:packages** (For pushing changes)

### **🔹 Step 6: Generate & Copy the Token**  
- Click **"Generate token"**.  
- **Copy and save it safely** (You won’t see it again).  

### **🔹 Step 7: Use the Token in Git**  
- When Git asks for a **password**, paste **this token** instead.

---

## **3. Git Basic Commands (For Assignment-1 Repo)**  

### **🔹 One-Time Git Setup**  
```
git config --global user.name "Your Name"
```
```
git config --global user.email "your.email@example.com"
```

### **🔹 Clone the Assignment Repository**  
```
git clone https://github.com/Emadram/Assignment-1.git
```
```
cd Assignment-1
```

### **🔹 Check Repository Status**  
```
git status
```

### **🔹 Pull Latest Changes from Remote**  
```
git pull origin main
```

### **🔹 Add Files to Staging**  
```
git add <filename>  # Add a specific file
```
```
git add .           # Add all changes
```

### **🔹 Commit Changes**  
```
git commit -m "Your commit message"
```

### **🔹 Push Changes to Remote Repository**  
```
git push origin main
```

---

✅ **Done!** You are now set up to pull and push to **[Assignment-1](https://github.com/Emadram/Assignment-1)**
