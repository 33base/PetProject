# PetProject
Pet Project for learning FastAPI and DevOps
## In this project we learn how to use Fastapi services 

## Getting Started

  

To run this application locally, follow these steps:

  

1. Clone this repository:

```
git clone <repository-url>
cd python-intern
```
2. Create an `.env` file based on the `.env.sample` file:
```
cp .env.sample .env
```
3. Open the `.env` file and adjust the environment variables as needed.

4. Set up and activate the virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
5. Install the required dependencies:
```
pip install -r requirements.txt
```
6. Run the FastAPI application using Uvicorn:
```
uvicorn app.main:app --reload
```
Note: The above command assumes that you have your FastAPI application instance named app in a file named main.py inside the app directory. Adjust the path accordingly if your setup is different.

7. Access the application at  http://127.0.0.1:8000 or the IP address of your VM in a web browser.

## Running the Application in Docker 

### Step 1: Building Docker image 
First, we need to build the Docker image of our application. To do this, navigate to the directory containing your Dockerfile and run:

```
docker build -t be_app .
```
### Step 2: Run the conteiner
After the image has been built, you can run a container based on this image:
```
docker run -p 8000:8000 be_app
```
Now, your application should be accessible at http://localhost:8000/ (or whichever port you specified).
