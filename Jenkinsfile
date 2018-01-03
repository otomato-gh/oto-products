node{
  def svcName = 'products'
  def nsName = "${svcName}-testing-${env.BUILD_NUMBER}"
  stage ('git'){
     checkout scm
  }
  def image = ''
  stage ('dockerize'){
	  image = docker.build "otomato/oto-${svcName}:${env.BUILD_NUMBER}"
  }
  stage ('push'){
      image.push()
  }
  stage ('deploy-to-cf'){
      codefreshRun cfBranch: 'cf-example', cfPipeline: 'checkKube', cfVars: [[Value: '${env.BUILD_NUMBER}', Variable: 'BUILD_NUMBER']]
  }
}
