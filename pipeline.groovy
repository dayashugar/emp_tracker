pipeline {
    agent any
    stages {
        // STAGE 1: Pull code from GitHub
        stage('Download-Code') {
            steps {
                git branch: 'master', url: "https://github.com/chethansh54/app-tracker.git"
            }
        }
        // STAGE 2: Build Docker Image
        stage('Build-Docker-Image') {
            steps {
                script {
                    sh 'echo "Building Docker Image......" '
                    sh 'docker build -t app_tracker .'
                }
            }
        }
        // STAGE 3: Test Docker Image
        stage('Test-Docker-Image') {
            steps {
                script {
                    sh 'docker rm container1'
                    sh 'docker run --name container1 -v /home/chethan/appData:/app/data app_tracker'
                    sh 'echo "Checking /home/chethan/appData location for Output-Image"'
                    sh 'ls /home/chethan/appData/ScreenTime.png'
                }
            }
        }
        // STAGE 4: Deploy
        stage('Deploy-Docker-Container') {
            steps {
                script {
                    sh 'echo "DEPLOYING APP TRACKER"'
                    sh 'echo "removing old container....."'
                    sh 'docker rm container2'
                    sh 'docker run --name container2 -v /var/lib/jenkins/workspace/Stage-1-Download-Code:/app/data app_tracker'
                    sh 'echo "DEPLOYMENT SUCCESS"'
                }
            }
        }
    }
}