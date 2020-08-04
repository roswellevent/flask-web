pipeline
{
  agent none
  stages
  {
          stage('Test') {
            agent { dockerfile true }
             steps {
                echo 'Testing Now'
                  withEnv(["HOME=${env.WORKSPACE}"]) {
                      sh 'pytest test_program.py --junitxml=test-reports/result.xml'
                      junit 'test-reports/*.xml'
                  }
              }
          }

       stage('Build') {
             agent any
             steps {
                echo 'Building Container from Dockerfile'
                 //script {
                 //   def customImage = docker.build("my-image:${env.BUILD_ID}")
                 //   customImage.push()
                 //}
             }
       }
  }
}