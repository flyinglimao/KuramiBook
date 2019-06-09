workflow "Publisher" {
  on = "schedule(0 9 * * 1)"
  resolves = ["./publisher/"]
}

action "./publisher/" {
  uses = "./publisher/"
  env = {
    COMMIT_EMAIL = "hi@limaois.me"
    COMMIT_NAME = "flyinglimao"
  }
  secrets = ["GITHUB_TOKEN"]
}
