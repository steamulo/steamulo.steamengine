properties ([gitLabConnection('jenkins'), buildDiscarder(logRotator(artifactDaysToKeepStr: '5', artifactNumToKeepStr: '10', daysToKeepStr: '10', numToKeepStr: '5'))])

node ('vagrant') {
    try {
        withPythonEnv('/usr/bin/python2.7') {
            sh "mkdir steamulo.steamengine"
            dir('steamulo.steamengine') {
                checkout scm
                gitlabBuilds(builds: ['Testing']) {
                    stage ('Testing') {
                        gitlabCommitStatus('Testing') {
                            sh "pip install -r requirements.txt"
                            sh "molecule test --all"
                        }
                    }
                }
            }
        }
    } finally {
        cleanWs()
    }
}
