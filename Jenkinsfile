pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    ./venv/bin/python -m uvicorn api:app \
                    --host 127.0.0.1 \
                    --port 8000 &

                    sleep 5

                    ./venv/bin/python -m pytest -v test/api_test.py
                '''
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t fastapi-app .'
            }
        }

        stage('Tag') {
            steps {
                sh 'docker tag fastapi-app fastapi-app:${BUILD_NUMBER}'
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    docker rm -f fastapi-test 2>/dev/null || true

                    docker run -d \
                    --name fastapi-test \
                    -p 8000:8000 \
                    fastapi-app:${BUILD_NUMBER}

                    sleep 5

                    curl -f http://localhost:8000/health
                '''
            }
        }
    }
}