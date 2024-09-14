from django.http import HttpResponse

def home(response):
    return HttpResponse('''<h1> This is a heading line </h1>
                        
                        <div> 
                        <a href="/first/about"> About </a>
                        <a href="/first/contact"> Contact </a>
                        <a href="/second/courses"> Courses </a>
                        <a href="/second/feedback"> Feedback </a>
                        </div>
                        
                        ''')