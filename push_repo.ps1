$git = "C:\Users\CRaje\AppData\Local\Microsoft\WinGet\Packages\Git.MinGit_Microsoft.Winget.Source_8wekyb3d8bbwe\cmd\git.exe"

# 1. Initialize repository
Write-Host "Initializing Git repository..."
& $git init

# 2. Rename branch to main
Write-Host "Setting default branch to main..."
& $git branch -M main

# 3. Configure local user details
Write-Host "Configuring git user name and email..."
& $git config user.name "RAJESH36-IN"
& $git config user.email "RAJESH36-IN@users.noreply.github.com"
& $git config credential.helper wincred

# 4. Stage and commit files
Write-Host "Staging files..."
& $git add .
Write-Host "Creating initial commit..."
& $git commit -m "Initial commit - debugged EduFlow LMS with all tests passing"

# 5. Configure remote and push
Write-Host "Configuring remote origin..."
# Check if remote already exists, if so, remove it first
$existingRemote = & $git remote
if ($existingRemote -contains "origin") {
    & $git remote remove origin
}
& $git remote add origin "https://github.com/RAJESH36-IN/HappyLearning_Ai.git"

Write-Host "Pushing to GitHub..."
& $git push -u origin main
