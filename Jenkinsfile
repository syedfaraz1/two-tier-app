pipeline{
    agent any
    stages{
        stage('Code clone'){
            steps{
                git branch: 'main', url: 'https://github.com/syedfaraz1/two-tier-app.git'
            }
        }
        stage('Build the app using docker'){
            steps{
                sh "docker build -t my-flask-app ."
            }
        }
        
        stage('Push to docker Hub'){
            steps{
                withCredentials([usernamePassword(
                    credentialsId: "dockerHubCreds",
                    usernameVariable: "dockerHubUser",
                    passwordVariable: "dockerHubPass")])
                    {
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                    sh "docker image tag my-flask-app ${env.dockerHubUser}/my-flask-app-cicd"
                    sh "docker push ${env.dockerHubUser}/my-flask-app-cicd"
                }
            }
        }
        
        stage('Test'){
            steps{
                echo 'Tester will take care'
            }
        }
        stage('Deploy'){
            steps{
                sh "docker compose up -d --build"
            }
        }
    }
}
