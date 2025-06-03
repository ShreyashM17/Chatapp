# ChatApp

A real-time chat application built with Django, designed for local deployment. Users can join by simply entering a name and start chatting instantly. The application features a user-friendly interface and displays messages in real-time.

## Features

* **Real-Time Communication**: Engage in live conversations with instant message updates.
* **User-Friendly Interface**: Clean and intuitive UI for seamless user experience.
* **Easy Setup**: Run locally without complex configurations.

## Prerequisites

* Python 3.x
* pip (Python package installer)
* Virtual environment tool (optional but recommended)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ShreyashM17/Chatapp.git
   cd Chatapp
   ```



2. **Create and Activate Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```



3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```



4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```



5. **Run the Server**:

   ```bash
   python manage.py runserver
   ```



6. **Access the Application**:

   Open your browser and navigate to `http://127.0.0.1:8000/` to start chatting.

## Project Structure

```
Chatapp/
├── chat/             # Django app handling chat functionalities
├── website/          # Django project configurations
├── manage.py         # Django's command-line utility
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```



## Technologies Used

* **Backend**: Django (Python)
* **Frontend**: HTML, CSS, JavaScript
* **Real-Time Communication**: Django Channels (if implemented)([repos.ecosyste.ms][3])

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

---

Feel free to customize this `README.md` further to align with any additional features or specific instructions relevant to your project.
