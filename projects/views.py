from django.shortcuts import render


def index(request):
    return render(request, "projects/index.html",
                  context={
                      "projects":[
                          {"title": "New", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque placerat nibh vitae mauris efficitur, vitae egestas lectus molestie. Duis dictum orci massa, sit amet pulvinar nisi porta vitae. Pellentesque aliquam sem metus, tincidunt mattis sapien tempor vitae. Nullam volutpat sit amet metus id scelerisque. Praesent felis tortor, fringilla ac condimentum a, ornare et sapien. Donec a turpis ultrices, fringilla eros vel, lobortis velit."},
                          {"title": "New", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque placerat nibh vitae mauris efficitur, vitae egestas lectus molestie. Duis dictum orci massa, sit amet pulvinar nisi porta vitae. Pellentesque aliquam sem metus, tincidunt mattis sapien tempor vitae. Nullam volutpat sit amet metus id scelerisque. Praesent felis tortor, fringilla ac condimentum a, ornare et sapien. Donec a turpis ultrices, fringilla eros vel, lobortis velit."},
                          {"title": "New", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque placerat nibh vitae mauris efficitur, vitae egestas lectus molestie. Duis dictum orci massa, sit amet pulvinar nisi porta vitae. Pellentesque aliquam sem metus, tincidunt mattis sapien tempor vitae. Nullam volutpat sit amet metus id scelerisque. Praesent felis tortor, fringilla ac condimentum a, ornare et sapien. Donec a turpis ultrices, fringilla eros vel, lobortis velit."},
                          {"title": "New", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque placerat nibh vitae mauris efficitur, vitae egestas lectus molestie. Duis dictum orci massa, sit amet pulvinar nisi porta vitae. Pellentesque aliquam sem metus, tincidunt mattis sapien tempor vitae. Nullam volutpat sit amet metus id scelerisque. Praesent felis tortor, fringilla ac condimentum a, ornare et sapien. Donec a turpis ultrices, fringilla eros vel, lobortis velit."},
                          {"title": "New", "description": " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque placerat nibh vitae mauris efficitur, vitae egestas lectus molestie. Duis dictum orci massa, sit amet pulvinar nisi porta vitae. Pellentesque aliquam sem metus, tincidunt mattis sapien tempor vitae. Nullam volutpat sit amet metus id scelerisque. Praesent felis tortor, fringilla ac condimentum a, ornare et sapien. Donec a turpis ultrices, fringilla eros vel, lobortis velit."},
                      ]
                  }
                
                  
                  
                  
                  )
