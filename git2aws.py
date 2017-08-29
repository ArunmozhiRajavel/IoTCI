from datetime import datetime, timedelta
from github import Github

def getLastCommitURL():
	g = Github('ArunmozhiRajavel', 'Arun#moz3')
#	org = g.get_organization('ArunmozhiRajavelOrg')
	code = g.get_user().get_repo('IoTCI')
    	# limit to commits in past 24 hours
	since = datetime.now() - timedelta(days=1)
	commits = code.get_commits(since=since)
	last = commits[0]
	print(last.html_url)
	raw_input("Press Enter to terminate.")
	return last.html_url

getLastCommitURL()
