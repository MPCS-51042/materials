**1. A SHA is...**
- simple hash algo and it represents the snapshot of the codebase at the time of the commit. It's a UID and it's the exact state of the codebase at that time. 

**2. A branch is...**
- A branch is a name that we attach to a specific commit within our history. 

**3. A remote...**
- What we will use to submit homework in the class! however, what it means in general a remote is a place outside of the local machine where the repository is being stored, e.g., Git, Azure, GCP etc. 

**4. The commands would be..**
- first create and check out a new branch called 'with_documentation'. This is so that the changes they made are not lost. 
    git checkout -b with_documentation
- Then we want to have the local main branch match the remote main branch. 
    git checkout main | switches us to the main branch
    git reset --hard origin/main | now our local main branch will match the remote main branch but this removes the last four commits from the local main
- Now we want to push that newly created branch that has the 4 new commits to remote
    git push origin with_documentation
- Now create a PR that requests someone review with_documentation vs. main before merging. You can do that from the github website and click "open pull request" or "new pull request". You can tag the appropriate person there.

