pipeline {
  agent none
  stages {
    stage('') {
      steps {
        sh '''file_name=$1
echo ${file_name}
#-- Create build info file
echo -e "Jenkins: ${BUILD_TAG}\\nGit: ${GIT_BRANCH} ${GIT_COMMIT}" > build_info_impl.txt

zip -r ${file_name} * -x build.sh
echo "The build is completed"
'''
      }
    }
  }
}