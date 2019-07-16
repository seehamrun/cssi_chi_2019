import webapp2
import os
import jinja2
import random

fortune_list=['Tomorrow, you will meet a life-changing new friend.',
              'Fame and Instagram followers are headed your way.',
              'On the Tuesday after next, an odd meeting will lead to a new opportunity.',
              'Despite dry skies, bring an umbrella tomorrow.',
              'A thrilling time is in your immediate future.',
              'Someone has Googled you recently.',
              'Stay alert. You will be part of a rescue mission.',
              'You will beat Watson in a game of Jeopardy. Start studying though']

def get_fortune():
    return(random.choice(fortune_list))


#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_directory.get_template("templates/fortune.html")
        values = {}

        if self.request.get('user_astrological_sign') != "":
            random_fortune = get_fortune()
            astro_sign = self.request.get('user_astrological_sign')
            values['the_fortune'] = random_fortune
            values['the_astro_sign'] = astro_sign

        if self.request.get('show_all') == "True":
            values['all_fortunes'] = fortune_list
        self.response.write(template.render(values))


app = webapp2.WSGIApplication([
    ('/', FortuneHandler)
], debug=True)
