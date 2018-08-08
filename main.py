# -*- coding: utf-8 -*-
# ^^ that's for emojis -- type 'u' before quoted text to insert emojis

import os
import webapp2
import jinja2
from artist_service import artist_info
# This says go to the artist service module and bring in the artist info,
# as artist info is used later on in this specific section

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# this initilizes the jinja library, and is immune from injection attacks (autoescape)
# it tells appengine where to find things i guess

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_current_directory.get_template(
            "templates/welcome.html")
        self.response.write(welcome_template.render())

class ArtistsHandler(webapp2.RequestHandler):
    def get(self):
        artists_template = jinja_current_directory.get_template(
            "templates/artists.html")
        self.response.write(artists_template.render())

class ArtistHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("name")
        artist_template = jinja_current_directory.get_template(
            "templates/artist.html")
        self.response.write(artist_template.render({
                "name": name,
                "image": artist_info[name]["image"],
                "artist": artist_info[name],
                "spotify_link": artist_info[name]["spotify_link"]
                }))

class SongsHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("name")
        songs_template = jinja_current_directory.get_template(
            "templates/songs.html")
        self.response.write(songs_template.render({"name": name}))

class AlbumsHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("name")
        albums_template = jinja_current_directory.get_template(
            "templates/albums.html")
        self.response.write(albums_template.render({"name": name}))


app = webapp2.WSGIApplication([
# WISGApplication comes from the webapp2
    ('/', WelcomeHandler),
    # has two applicaiotns - this is a tuple, maps all the things you can do the very first thing it does is go to WelcomeHandler
    ('/artists', ArtistsHandler),
    ('/artist', ArtistHandler),
    ('/songs', SongsHandler),
    ('/albums', AlbumsHandler)
], debug=True)
# debug mode means that the webapp spits out a ton of info to look at - in order to debug it :)
