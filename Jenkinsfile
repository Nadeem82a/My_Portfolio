pipeline {
  agent none
  stages {
    stage('Initialize') {
      agent {
        dockerfile {
          filename 'Dockerfile'
        }

      }
      steps {
        echo 'This is minimal pipeline'
      }
    }
  }
}