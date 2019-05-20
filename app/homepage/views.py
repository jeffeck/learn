from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
test_message = HttpResponse('<h1>Test Message sucessfully returned')

def home(request):
	return render(request, 'homepage/index.html')
	# return HttpResponse('<h1>Home page</h1>')


def instructions(request):
	# return HttpResponse(test_message)
	return render(request, 'homepage/instructions.html')

def links(request):
	# return test_message
	context = {
				'github': [
					{
						'links': [
							{
								'title': 'My Repository',
								'url': 'https://github.com/jeffeck?tab=repositories',
							},
							{
								'title': "Clone a Repository",
								'url': "https://github.com/jeffeck?tab=repositories"
							},
							{
								'title': 'Branching',
								'url': "https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches"
							},
							{
								'title': 'Committing Changes',
								'url': "https://help.github.com/en/desktop/contributing-to-projects/committing-and-reviewing-changes-to-your-project"
							},
							{
								'title': "Merging",
								'url': "https://help.github.com/en/articles/about-merge-methods-on-github"
							},
							{
								'title': "Rebasing",
								'url': "https://help.github.com/en/articles/about-git-rebase"
							},
						],
					},
				],
				'docker': [
					{
						'links': [
							{
								'title': 'test docker',
								'url': 'www.docker.com'
							}
						]
					}
				]
			}


	return render(request, 'homepage/links.html', context)
