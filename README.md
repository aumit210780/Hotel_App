# Hotel Search and Booking System

This project is a Django-based web application that allows users to search for hotels by city, price range, and star rating. The system scrapes hotel data from Booking.com and Agoda, compares prices, and displays the best matches to the user. Users can also bookmark their favorite hotels for future reference.

## 1. Installation Guide

### 1.1. Prerequisites
- **Python 3.8+**: Download from [Python's official site](https://www.python.org/downloads/).
- **PostgreSQL**: Download from [PostgreSQL official site](https://www.postgresql.org/download/).
- **Git**: Download from [Git official site](https://git-scm.com/).

### 1.2. Clone the Repository
bash:
<pre>
git clone https://github.com/your-username/hotel_project.git
cd hotel_project
</pre>

### 1.3. Set Up a Virtual Environment
<pre>
For Windows:
bash:
python -m venv venv
venv\Scripts\activate

For macOS/Linux:
bash:
python -m venv venv
source venv/bin/activate
</pre>

### 1.4. Install Dependencies
bash:
<pre>
pip install -r requirements.txt
</pre>

## 2. Configuration
### 2.1. Set Up Environment Variables
#### Create a .env file in the root of the project.

#### Add the following variables to the .env file:
<pre>
SECRET_KEY=your_django_secret_key
DB_NAME=hotel_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
</pre>

### 2.2. Configure PostgreSQL
#### Open pgAdmin or any PostgreSQL client.
#### Create a new database named hotel_db.

## 3. How to Run
### 3.1. Run Migrations
bash:
<pre>
python manage.py makemigrations
python manage.py migrate
</pre>


### 3.2. Start the Django Server
bash:
<pre>
python manage.py runserver
</pre>

#### Visit http://127.0.0.1:8000/ in your browser to access the application.

### 3.3. Run Scrapy Spiders
#### To scrape hotel data, run the following commands:
bash:
<pre>
cd hotel_scraper
scrapy crawl booking
scrapy crawl agoda
</pre>


## Project Structure
<pre>
hotel_project/
├── hotel_project/          # Django project settings
├── hotel_app/              # Django app (main functionality)
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   ├── forms.py            # Django forms
│   ├── models.py           # Database models
│   ├── views.py            # Django views
│   ├── urls.py             # App-level URLs
│   └── scraping.py         # Scrapy integration
├── hotel_scraper/          # Scrapy project
│   ├── hotel_scraper/
│   │   ├── spiders/        # Scrapy spiders
│   │   └── settings.py     # Scrapy settings
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
</pre>



#### How to Use
#### Sign Up:
##### Go to http://127.0.0.1:8000/signup/ and create a new account.

#### Log In:
##### Go to http://127.0.0.1:8000/login/ and log in with your credentials.

#### Search for Hotels:
##### Use the search form to find hotels by city, price range, and star rating.

#### Bookmark Hotels:
##### Click the Bookmark button on a hotel to save it to your bookmarks.

#### View Bookmarks:
##### Go to http://127.0.0.1:8000/bookmarks/ to view your bookmarked hotels.

#### Contributing
##### Contributions are welcome! If you'd like to contribute, please follow these steps:
<pre>
Fork the repository.
Create a new branch (git checkout -b feature/YourFeatureName).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeatureName).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.
</pre>

#### Contact
##### For any questions or inquiries, feel free to reach out:

Email: aumit115@gmail.com
GitHub: aumit210780

