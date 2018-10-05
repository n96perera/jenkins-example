
pipeline {
    agent any

    def cmdArray2 = ["python", "https://github.com/n96perera/jenkins-example/blob/master/testpipe.py"]
    def process = new ProcessBuilder(cmdArray2).redirectErrorStream(true).start()
    process.inputStream.eachLine {
      log.warn(it)
    }
    process.waitFor()
    return process.exitValue()
}
