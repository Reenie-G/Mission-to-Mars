{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ad4cadcd",
   "metadata": {},
   "source": [
    "# 10.5.1 Use Flask to Create a Web App"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "db4379a3",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "# Using Flask and Mongo to beging creating Robin's web app\n",
    "\n",
    "from flask import Flask, render_template, redirect, url_for\n",
    "from flask_pymongo import PyMongo\n",
    "import scraping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "680f2c06",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set up flask\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f913a0e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use flask_pymongo to set up mongo connection\n",
    "\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "31fd4921",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define the route for HTML\n",
    "\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "   mars = mongo.db.mars.find_one()\n",
    "   return render_template(\"index.html\", mars=mars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb71a712",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [01/Aug/2022 19:47:37] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [01/Aug/2022 19:47:37] \"GET /static/images/error.png HTTP/1.1\" 404 -\n",
      "[2022-08-01 19:47:48,847] ERROR in app: Exception on /scrape [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\gonza\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\gonza\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\gonza\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"C:\\Users\\gonza\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"C:\\Users\\gonza\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\gonza\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"C:\\Users\\gonza\\AppData\\Local\\Temp\\ipykernel_57032\\3579977935.py\", line 4, in scrape\n",
      "    mars_data = scraping.scrape_all()\n",
      "AttributeError: module 'scraping' has no attribute 'scrape_all'\n",
      "127.0.0.1 - - [01/Aug/2022 19:47:48] \"GET /scrape HTTP/1.1\" 500 -\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "   mars = mongo.db.mars\n",
    "   mars_data = scraping.scrape_all()\n",
    "   mars.update_one({}, {\"$set\":mars_data}, upsert=True)\n",
    "   return redirect('/', code=302)\n",
    " \n",
    "if __name__ == \"__main__\":\n",
    "   app.run()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a2a2c50",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  },
  "vscode": {
   "interpreter": {
    "hash": "4a9361c6053ddebb4a3cbafa186ad24281b12153eb8dd7165b81196dc981e63a"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}