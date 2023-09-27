# FastAPI Email Generation API

This is a FastAPI project for generating personalized email content using OpenAI's GPT-3.5 Turbo model. It provides an HTTP API endpoint that takes input data and generates email text based on the provided information.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your computer.
- An OpenAI API key. You can obtain one by signing up at [OpenAI](https://beta.openai.com/signup/).

## Installation

1. **Clone the repository** to your local machine:

   ```shell
   git clone https://github.com/ganmol123/email-generator-be-service.git
   ```

2. **Navigate to the project directory**:

   ```shell
   cd fastapi-email-generation
   ```

3. **Create a virtual environment**:

   ```shell
   python -m venv venv
   ```

4. **Activate the virtual environment**:

   - On Windows:

     ```shell
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```shell
     source venv/bin/activate
     ```

5. **Install the project dependencies**:

   ```shell
   pip install -r requirements.txt
   ```

6. **Create a `.env` file** in the project directory and add your OpenAI API key:

   ```shell
   SECRET_KEY=your_openai_api_key_here
   ```

## Usage

1. **Start the FastAPI server**:

   ```shell
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

   This will start the server on `http://localhost:8000`.

2. Use an API client, such as Postman or `curl`, to make POST requests to the `/generate_email/` endpoint with the required input data. Here's an example request body:

   ```json
   {
     "recipient_name": "John Doe",
     "recipient_email": "johndoe@example.com",
     "subject": "Regarding Our Upcoming Event",
     "keywords": ["event", "invitation", "details"],
     "length": 100
   }
   ```

   This will generate an email based on the provided information and return the email content in the response.

3. You can integrate this API into your application for generating personalized email content.

## Deployment

To deploy this project to a production environment, consider using a cloud platform such as AWS, Azure, or Heroku. You can containerize the application using Docker and use container orchestration tools like Kubernetes for scaling.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
