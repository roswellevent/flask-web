pipeline {
  agent none
  stages {
        stage('Build') {
         agent any
             steps {
                echo 'Building Conatiner from Dockerfile'
             }
        }
        stage('Test') {
          agent { dockerfile true  }
          steps {
            withEnv(["HOME=${env.WORKSPACE}"]) {
                sh 'pytest test_program.py --junitxml=test-reports/result.xml'
            }
          }

         stage ('Build Image') {
          agent any
            steps {
                docker.build "my-image:${env.BUILD_ID}"
            }
        }



          post
          {
            always {
              junit 'test-reports/*.xml'
            }
            success {
                        echo "======Build OK!!!!======="

            }
          }
    }
  }

  agent any
  stages {

  }





}