# ConvexHullApp

This is a small client/server application that I made to practice javascript/HTML/CSS and learn a little bit about Flask.

The application is a web page that requests the user to click some points on a HTML canvas element. 

When the user clicks the "Form Convex Hull" button, the clicked points are then posted to the Flask server for processing. The convex hull of the point set is then computed using a Python library I wrote called ComputationalGeometry (located in the lib folder). The computed set of points along the convex hull are returned to the client, and a perimeter is drawn on the HTML canvas element connecting the points on the hull.

# To Run Locally
Python 3 and Flask must be installed
- Learn about/install Python here:https://www.python.org/
- install Flask using "pip install Flask"

Instructions:
1. Pull repository from github to local computer
2. Open the command line and navigate to the ConvexHullApp directory
3. Run the command "python server.py" to launch the Flask Server
4. Open a web browser and type "localhost:5000" as the URL address
5. Click points on HTML canvas and press "Form Convex Hull" button
6. Click on HTML canvas again to clear points and start over
