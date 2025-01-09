pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'devamsdock/firstrepo'
    }
    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from SCM...'
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                        echo 'Building the Docker image...'
                        # Build the Docker image
                        docker build -t $DOCKER_IMAGE:${BUILD_NUMBER} .

                    '''
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    echo 'Pushing Docker image to Docker Hub...'
                    sh '''
                        # Push the Docker image
                        docker push $DOCKER_IMAGE:${BUILD_NUMBER}

                    '''
                }
            }
        }
    }
}
