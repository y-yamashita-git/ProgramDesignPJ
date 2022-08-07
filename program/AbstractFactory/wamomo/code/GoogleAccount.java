class EmailGoogle extends Email(string address) {
  this.value = address + "@gmail.com"
}


class AccountGoogle extends Account {
  @override
  fun createName(string name): Name {
    return new Name(name)
  }

  @override
  fun createEmail(string address): Email { 
    return new EmailGoogle(address)
  }
}
