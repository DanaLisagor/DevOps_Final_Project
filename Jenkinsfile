pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                dir('Final_Project_Phase1') {
                    sh 'docker build -t hello-flask-app:latest .'
                }
            }
        }

        stage('Test Python App') {
            steps {
                dir('Final_Project_Phase1') {
                    sh 'python3 -m py_compile hello_world.py'
                }
            }
        }

        stage('Deploy With Helm Dry Run') {
            steps {
                dir('Final_Project_Phase3') {
                    sh 'helm upgrade --install hello-flask-test ./hello-flask-chart --dry-run'
                }
            }
        }
    }
}
