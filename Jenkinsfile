pipeline{
    agent any
    stages {
        stage("checkout"){
            steps{
                checkout scm
            }
        }
        stage("build"){
            steps{
                sh 'docker-compose build serverapp'
            }
        }
        stage("Check dockerfile update"){
            def CHANGE = sh(script: "git diff ${SCM_VARS.GIT_PREVIOUS_SUCCESSFUL_COMMIT} ${SCM_VARS.GIT_COMMIT} main.py", returnStdout: true)
            script{
                if (CHANGE.length() > 0){
                    withCredentials([[$class: 'UsernamePasswordMultiBinding',
                    credentialsId: 'docker-hub', 
                    usernameVariable: 'DOCKER_USER_ID', 
                    passwordVariable: 'DOCKER_USER_PASSWORD'
                    ]]) {
                        sh "docker tag jenkins-piplines_web:latest ${DOCKER_USER_ID}/jenkins-app:${BUILD_NUMBER}"
                        sh "docker login -u ${DOCKER_USER_ID} -p ${DOCKER_USER_PASSWORD}"
                        sh "docker push ${DOCKER_USER_ID}/jenkins-app:${BUILD_NUMBER}"
                    }
                }
            }
        }
        stage('deploy'){
            steps{
                sh 'docker-compose up -d'
            }
        }
    }
}
