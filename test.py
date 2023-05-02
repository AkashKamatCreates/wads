import webapp2
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello World!!\n"),
        self.response.write("My Name is Akash Kamat\n"),
        self.response.write("ASSIGNMENT 1 CLOUD COMPUTING\n\n"),
        self.response.write("Class teit1\n\n"),
        self.response.write("roll: 307A007\n\n")

app=webapp2.WSGIApplication([('/',MainPage)], debug=True)