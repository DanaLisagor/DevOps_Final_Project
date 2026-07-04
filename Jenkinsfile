pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                dir('app') {
                    sh 'docker build -t hello-flask-app:latest .'
                }
            }
        }

        stage('Test Python App') {
            steps {
                dir('app') {
                    sh 'python3 -m py_compile hello_world.py'
                }
            }
        }

        stage('Deploy With Helm Dry Run') {
            steps {
                dir('helm') {
                    sh 'helm upgrade --install hello-flask-test ./hello-flask-chart --dry-run'
                }
            }
        }
    }
}
