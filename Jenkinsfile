pipeline {
  agent { dockerfile true  }
  stages {
    stage('Build') {
         steps {
            echo 'Building Conatiner from Dockerfile'
         }
    }
    stage('Test') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'pytest test_program.py --junitxml=test-reports/result.xml'
        }
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
        success {
        stages{
            stage ('Build Image'){
                steps{
                    sh "sudo docker build -t flask-web ."
                }
            }
        }
        }
      }
    }
  }
}