pipeline {

 agent any
 def pipeline = load 'https://github.com/n96perera/jenkins-example/blob/master/testpipe.py'

	environment {
        JAVA_HOME="${tool 'Java 8u181'}"
        PATH="${JAVA_HOME}/bin:${PATH}"
    }
	
    stages {   
        stage ('Run Stage') {
            steps {
                withEnv(['PYTHONPATH=C:/Python27']) {
                    bat 'python "pipeline"'
                }
            }
        }

    }
}
