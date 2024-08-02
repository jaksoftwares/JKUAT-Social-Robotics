from django.shortcuts import render


def index(request):
    return render(request, "projects/index.html",
                  context={
                      "projects":[
                          {"title": "New", "description": "old"},
                          {"title": "New", "description": "old"},
                          {"title": "New", "description": "old"},
                          {"title": "New", "description": "old"},
                          {"title": "New", "description": "old"},
                      ]
                  }
                
                  
                  
                  
                  )
