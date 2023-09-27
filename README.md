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

### Deploying a Docker Container to Google Cloud Run

Google Cloud Run allows you to easily deploy containerized applications in a serverless environment. Follow these steps to deploy your Docker container image to Google Cloud Run.

### Prerequisites

- A Google Cloud Platform (GCP) account.
- Docker installed on your local machine.
- Google Cloud SDK (`gcloud`) installed and configured.

### Steps

1. **Build Your Docker Image:**

   Build your Docker image using the following command, replacing `my-image` with your image name and tag:

   ```bash
   docker build -t my-image:latest .
   ```

2. **Tag Your Docker Image:**

   Tag your Docker image with the Google Container Registry path:

   ```bash
   docker tag my-image:latest gcr.io/your-project-id/my-image:latest
   ```

3. **Authenticate with Google Cloud:**

   Ensure you are authenticated to Google Cloud using the `gcloud auth` command. Use `gcloud auth login` if you are not already logged in.

4. **Configure Docker for GCR (Google Container Registry):**

   Configure Docker to use Google Container Registry as the container registry:

   ```bash
   gcloud auth configure-docker
   ```

5. **Push Docker Image to GCR:**

   Push your Docker image to Google Container Registry:

   ```bash
   docker push gcr.io/your-project-id/my-image:latest
   ```

6. **Deploy to Cloud Run:**

   Use the following `gcloud` command to deploy your container to Google Cloud Run:

   ```bash
   gcloud run deploy --image gcr.io/your-project-id/my-image:latest --platform managed --region your-region
   ```

   Replace `your-project-id` with your GCP project ID and `your-region` with your desired region.

7. **Configure Service Settings:**

   Follow the prompts to configure your service settings, including service name, permissions, and whether to allow unauthenticated invocations.

8. **Wait for Deployment:**

   Google Cloud Run will deploy your container image. Wait for the deployment to complete. You will receive a service URL when it's ready.

9. **Access Your Service:**

   You can now access your deployed service via the provided URL.

10. **Clean Up (Optional):**

    To delete the service, run the following command:

    ```bash
    gcloud run services delete service-name --platform managed --region your-region
    ```

    Replace `service-name` with your service name and `your-region` with your region.

Congratulations! Your Docker container image is now deployed and running on Google Cloud Run.

Replace the placeholders (`your-project-id`, `your-region`, `my-image`, etc.) with your specific project details and image names.



## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
