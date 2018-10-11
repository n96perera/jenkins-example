pipeline {

 agent any
 
    environment {
        JAVA_HOME="${tool 'Java 8u181'}"
        PATH="${JAVA_HOME}/bin:${PATH}"
    }
	
    stages {
        stage ('Run Stage') {
            steps {
                withEnv(['PYTHONPATH=C:/Python27']) {
                    bat 'python C:/Program Files (x86)/Jenkins/workspace/Test/Test/pipeline-with-python/testpipe.py'
                }
            }
        }

    }
}
