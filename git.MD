# Git & GitHub Guide for Students

## Introduction

**Git** is a popular version control system widely used by developers to collaborate on projects. It allows multiple people to work on the same codebase simultaneously while keeping track of changes and preventing conflicts.

**GitHub** is a cloud-based hosting service that lets you manage Git repositories, making it easy to share code and collaborate with others.

### Why Use Git?

- Track changes to your code over time
- Collaborate with team members without overwriting each other's work
- Maintain a complete history of your project
- Revert to previous versions if something breaks
- Work on new features independently using branches

## Learning Resources

- [W3Schools Git Tutorial](https://www.w3schools.com/git/git_intro.asp)
- [GeeksforGeeks Git Commands](https://www.geeksforgeeks.org/git/useful-github-commands/)

---

## Essential Git Commands

### Getting Started

#### Clone a Repository
Create a local copy of a remote repository on your computer:
```bash
git clone <URL>
```

**Example:**
```bash
git clone https://github.com/username/repository-name.git
```

#### Check Repository Status
See which files have been modified, added, or deleted:
```bash
git status
```

#### Get Latest Changes
Pull the most recent changes from the remote repository:
```bash
git pull
```

### Working with Branches

Branches allow you to work on new features or fixes without affecting the main codebase.

#### Create a New Branch
Create and switch to a new branch based on the current branch:
```bash
git checkout -b <branch-name>
```

**Example:**
```bash
git checkout -b username_ex1
```

**Naming Convention:** Use descriptive names like `username_feature-name` or `username_bugfix-description`

#### Switch Between Branches
```bash
git checkout <branch-name>
```

**Examples:**
```bash
git checkout main          # Switch to main branch
git checkout username_ex1  # Switch to your feature branch
```

#### List All Branches
```bash
git branch
```

---

## Standard Workflow: Making and Pushing Changes

Follow these steps to save your work and share it with your team:

### 1. Create a Branch
```bash
git checkout -b username_feature-name
```

### 2. Make Your Changes
Edit, create, or delete files as needed using your code editor.

### 3. Check What Changed
```bash
git status
```

### 4. Stage Your Changes
Add all modified files to the staging area:
```bash
git add .
```

Or add specific files:
```bash
git add filename.txt
git add folder/another-file.py
```

### 5. Commit Your Changes
Record a snapshot with a descriptive message:
```bash
git commit -m "Add login form validation"
```

**Good commit message examples:**
- `"Fix navbar alignment issue"`
- `"Add user authentication feature"`
- `"Update README with installation instructions"`

**Avoid vague messages like:**
- `"Fixed stuff"`
- `"Changes"`
- `"Update"`

### 6. Push to Remote Repository

**First time pushing a new branch:**
```bash
git push --set-upstream origin <branch-name>
```

**After the first push:**
```bash
git push
```

---

## Best Practices

### Commit Frequently
Push your changes in small, logical increments. This approach:
- Prevents losing progress if files are accidentally deleted
- Makes it easier to identify when bugs were introduced
- Keeps your commit history clean and understandable
- Allows team members to see your progress

### Write Clear Commit Messages
- Start with a verb (Add, Fix, Update, Remove)
- Keep it concise but descriptive
- Explain what changed and why (if not obvious)

### Pull Before You Push
Always pull the latest changes before pushing your work to avoid conflicts:
```bash
git pull
git push
```

### Keep Your Branch Updated
Regularly merge changes from the main branch into your feature branch:
```bash
git checkout main
git pull
git checkout your-branch
git merge main
```

---

## Additional Useful Commands

### View Commit History
```bash
git log
```

Press `q` to exit the log view.

### See What Changed
View differences in modified files:
```bash
git diff
```

### Discard Local Changes
If you want to undo changes to a file:
```bash
git checkout -- <filename>
```

### Remove Files from Staging
If you accidentally added files:
```bash
git reset HEAD <filename>
```

### Delete a Branch
After merging your work, delete the old branch:
```bash
git branch -d <branch-name>
```

---

## Common Scenarios

### Scenario 1: I Made a Mistake in My Last Commit
If you haven't pushed yet:
```bash
git commit --amend -m "Corrected commit message"
```

### Scenario 2: I Need to Switch Branches but Have Uncommitted Changes
Save your work temporarily:
```bash
git stash
git checkout other-branch
# Do your work
git checkout original-branch
git stash pop
```

### Scenario 3: Merge Conflicts
If Git can't automatically merge changes:
1. Git will mark the conflicting files
2. Open the files and look for conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
3. Edit the file to resolve conflicts
4. Stage and commit the resolved files:
```bash
git add .
git commit -m "Resolve merge conflicts"
```

---

## Getting Help

If you're stuck, Git has built-in help:
```bash
git help <command>
```

**Example:**
```bash
git help commit
```

---