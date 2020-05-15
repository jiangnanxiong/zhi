pipeline {
  agent {
    node {
      label 'win7'
    }

  }
  stages {
    stage('git pull') {
      steps {
        git 'https://github.com/jiangnanxiong/zhi.git'
      }
    }

    stage('run') {
      steps {
        bat 'python testsuite/run_discover.py'
      }
    }

  }
}