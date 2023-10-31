import requests
import getpass

# Replace with your GitHub username and token
username = input("Please Enter your Github Username : ")
token = input("Please Enter your Personal Access Token : ")

# Prompt for the repository name
repo_name = input("Enter the name of the new repository: ")

# Prompt for the description (optional)
repo_description = input("Enter a description for the repository (press Enter to skip): ")

# Create a new repository
url = f"https://api.github.com/user/repos"
headers = {
    "Authorization": f"token {token}"
}
data = {
    "name": repo_name,
    "description": repo_description
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 201:
    print("Repository created successfully.")
else:
    print(f"Failed to create the repository. Status code: {response.status_code}")
    print(response.json())
    exit()

# Provide instructions on how to upload files via the command line
print(f"Repository URL: https://github.com/{username}/{repo_name}.git")
print("To upload files to this repository, follow these steps:")
print(f"1. Open your terminal/command prompt.")
print(f"2. Navigate to the directory containing your project or files you want to upload.")
print(f"3. Run the following commands:")
print(f"   a. Initialize a Git repository if you haven't already: `git init`")
print(f"   b. Add your files to the staging area: `git add .`")
print(f"   c. Commit your changes: `git commit -m 'Initial commit'`")
print(f"   d. Set the remote repository as the origin: `git remote add origin https://github.com/{username}/{repo_name}.git`")
print(f"   e. Push your files to the repository: `git push -u origin master`")

print("Your files should now be uploaded to your new GitHub repository.")
