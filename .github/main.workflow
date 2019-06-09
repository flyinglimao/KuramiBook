workflow "Publisher" {
  resolves = ["./publisher/"]
  on = "schedule(*/5 * * * *)"
}

action "./publisher/" {
  uses = "./publisher/"
  env = {
    COMMIT_EMAIL = "hi@limaois.me"
    COMMIT_NAME = "flyinglimao"
  }
  secrets = ["GITHUB_TOKEN"]
}
