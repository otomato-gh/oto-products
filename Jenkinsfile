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
      docker.withRegistry('', '0d81b0a7-79bb-4a5f-b4c1-327b828ef25a'){
        image.push()
      }
  }
  stage ('deploy-to-cf'){
      codefreshRun cfBranch: 'cf-example', cfPipeline: 'oto-products', cfVars: [[Value: "${env.BUILD_NUMBER}", Variable: 'BUILD_NUMBER']]
  }
}
