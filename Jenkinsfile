pipeline {

 agent any
 
    environment {
        JAVA_HOME="${tool 'Java 8u181'}"
        PATH="${JAVA_HOME}/bin:${PATH}"
    }
	
    stages {
	     stage('Git Clone') {
            steps {
                git branch: 'master',
                credentialsId: 'gitrepository-test',//this has been taken from jenkins credentials
                url: 'https://github.com/n96perera/jenkins-example.git'

			}	
        }
	    
        stage ('Run Stage') {
            steps {
                withEnv(['PYTHONPATH=C:/Python27']) {
                    bat 'python "https://github.com/n96perera/jenkins-example/blob/master/testpipe.py"'
                }
            }
        }

    }
}
