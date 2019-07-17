import webapp2
import os
import jinja2
import database_models

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/index.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render({
            'dogs': database_models.DatabaseDog.query().fetch()
        }))

    def post(self):
        dogName = self.request.get('dogName')
        dogAge = self.request.get('dogAge')
        dogColor = self.request.get('dogColor')
        dogBark = self.request.get('dogBark')
        dogReview = self.request.get('dogReview')
        stored_dog = database_models.DatabaseDog(
            age=int(dogAge),
            color=dogColor,
            bark_intensity=int(dogBark),
            name=dogName,
            review=dogReview
        )
        stored_dog.put()
        template = JINJA_ENVIRONMENT.get_template("templates/index.html")
        data = {
            'success_message': "Thanks " + dogName + " your review was received",
            'dogs': database_models.DatabaseDog.query().fetch()
        }
        self.response.write(template.render(data))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
