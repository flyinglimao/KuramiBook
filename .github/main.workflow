workflow "Publisher" {
  resolves = ["./publisher/"]
  on = "push"
}

action "./publisher/" {
  uses = "./publisher/"
  env = {
    COMMIT_EMAIL = "hi@limaois.me"
    COMMIT_NAME = "flyinglimao"
  }
  secrets = ["PUSH_TOKEN"]
}
