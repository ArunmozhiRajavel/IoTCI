from datetime import datetime, timedelta

def getLastCommitURL():
    encrypted = Arun#moz3
    g = Github('ArunmozhiRajavel', Arun#moz3)
    org = g.get_organization('Self')
    code = org.get_repo('IoTCI')
    # limit to commits in past 24 hours
    since = datetime.now() - timedelta(days=1)
    commits = code.get_commits(since=since)
    last = commits[0]
    return last.html_url
