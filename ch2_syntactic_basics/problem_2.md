**1. You shouldn't do three things below if you want to keep your committed work in git.**
a/ Check out an individual file
b/ Avoid running random commands found on the internet, especially those commands that contain '-f'. For example, the command <$git push -f> will erase the current version of the repo on GitHub and replace it with my version. This means if the current version includes changes from someone, we now lost these changes and have to redo that work.   
c/ Blow away the .git directory by typing <$rm -rf .git>

**2. I think...**
I think it can be difficult to undo a small piece of work that breaks the application. To avoid this difficulty, I should make small, incremental commits when things are working. If I break something, I can easily go back and check my last commit that is working and not so far behind my current working progress.