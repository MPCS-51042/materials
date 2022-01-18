**1. A SHA is a unique identifier that Git generates for each commit.**

**2. A branch is a development version of a code base that starts from an original (main) code base. Creating many branches from the main code base allows users to work on many versions of a code base at the same time without impacting each other and later still is able to merge back together after review.**

**3. A remote is a place outside of the local machine where a copy of a repository is kept**

**4. The commands would be as below.**
To restore the local main branch to the remote main branch: $git checkout 6f21591

To create a new branch: $git checkout -b restore-remote-main

Make 4 changes on this new branch
    After each change, add the change staged to commit: $git add . 
    and then to commit: $git commit -m "message"

To push the change on the restore-remote-main: $git push --set-upstream origin restore-remote-main

To get the link where we can create pull request: $git remove -v