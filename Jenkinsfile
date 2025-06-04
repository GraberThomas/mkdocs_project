pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/monuser/monrepo.git'
      }
    }
    stage('Build') {
      steps {
        sh 'docker build -t monimage:test .'
      }
    }
    stage('Test') {
      steps {
        sh 'pytest'
      }
    }
    stage('Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh '''
            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
            docker push monimage:test
          '''
        }
      }
    }
  }
}
