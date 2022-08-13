class Name(string)

@Abstract
class Email(string)

@Abstract
class Account {
  fun createName(string): Name
  fun createEmail(string): Email
}
