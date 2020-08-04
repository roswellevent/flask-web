pipeline
{
  agent any
  stages
  {
          stage('Test') {
             steps {
                echo 'Testing Now'
                  withEnv(["HOME=${env.WORKSPACE}"]) {
                      sh 'pytest test_program.py --junitxml=test-reports/result.xml'
                      junit 'test-reports/*.xml'
                  }
              }
          }

       stage('Build') {
             steps {
                echo 'Building Container from Dockerfile'
                 script {
                    def customImage = docker.build("my-image:${env.BUILD_ID}")
                    customImage.push()
                 }
             }
       }
  }
}