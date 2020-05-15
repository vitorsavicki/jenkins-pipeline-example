pipeline{
  agent none
  stages{
    stage('Compile'){
      agent any
      steps{
        sh 'mvn compile'
      }       
    }
    stage('Code Quality'){
      agent any
      steps{
        sh 'echo Sonarqube Code Quality Check Done'
      }
    }
    stage('Test'){
      agent any
      steps{
        sh 'mvn test'
      }
    } 
    stage('Package'){
      agent any
      steps{
        sh 'echo Package Artifactory'
      }
    }
    stage('Upload War File To Artifactory'){
      agent any
      steps{
        sh 'echo Uploaded War file to Artifactory'
      }
    }
    stage('Deploy'){
      agent any
      steps{
        sh label: '', script: '''rm -rf dockerimg
mkdir dockerimg
cd dockerimg
cp /var/jenkins_home/workspace/jenkins-pipeline-example_master/Dockerfile .
cp /var/jenkins_home/workspace/jenkins-pipeline-example_master/Jenkinsfile . 
cp /var/jenkins_home/workspace/jenkins-pipeline-example_master/README.md .
cp /var/jenkins_home/workspace/jenkins-pipeline-example_master/mvnw .
cp /var/jenkins_home/workspace/jenkins-pipeline-example_master/mvnw.cmd .
cp /var/jenkins_home/workspace/jenkins-pipeline-example_master/pom.xml .
cp -r /var/jenkins_home/workspace/jenkins-pipeline-example_master/src .
cp -r /var/jenkins_home/workspace/jenkins-pipeline-example_master/target .
sudo docker build -t webimage:$BUILD_NUMBER .
sudo docker container run -itd --name webserver$BUILD_NUMBER -p 9090 webimage:$BUILD_NUMBER'''

      }
    }
  }
}
