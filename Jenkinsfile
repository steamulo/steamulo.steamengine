properties ([gitLabConnection('jenkins'), buildDiscarder(logRotator(artifactDaysToKeepStr: '5', artifactNumToKeepStr: '10', daysToKeepStr: '10', numToKeepStr: '5'))])

node ('vagrant') {
    try {
        checkout scm
        sh "virtualenv .env"
        sh "source .env/bin/activate"
        sh "pip install -r requirements.txt"
        sh "molecule test"
    } finally {
        cleanWs notFailBuild: true
    }
}
