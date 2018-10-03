
pipeline {
 agent any
    environment {
        JAVA_HOME="${tool 'java 8'}"
        PATH="${JAVA_HOME}/bin:${PATH}"
    }
    stages {
        stage ('Compile Stage') {
            steps {
                withMaven(maven : 'maven_3_5_0') {
                    bat 'mvn clean compile'
                }
            }
        }

        stage ('Testing Stage') {

            steps {
                withMaven(maven : 'maven_3_5_0') {
                    bat 'mvn test'
                }
            }
        }


    }
}
