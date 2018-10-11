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
                credentialsName: 'gitrepository-test',//this has been taken from jenkins credentials
                url: 'https://github.com/n96perera/jenkins-example.git'

			}	
        }
	    
        stage ('Run Stage') {
            steps {
                withEnv(['PYTHONPATH=C:/Python27']) {
                    bat 'python "C:/Program Files (x86)/Jenkins/workspace/Test/Test/pipeline-with-python/testpipe.py"'
                }
            }
        }

    }
}
