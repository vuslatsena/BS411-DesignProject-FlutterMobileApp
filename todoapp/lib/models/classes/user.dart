import 'package:flutter/rendering.dart';

class User {
  String username;
  String surname;
  String firstname;
  String email;
  String password;
  // ignore: non_constant_identifier_names
  String api_key;
  int id;

  User(this.username, this.surname, this.firstname, this.email, this.password,
      this.id, this.api_key);

  factory User.fromJson(Map<String, dynamic> parsedJson) {
    return User(
        parsedJson['username'],
        parsedJson['surname'],
        parsedJson['emailadress'],
        parsedJson['firstname'],
        parsedJson['password'],
        parsedJson['id'],
        parsedJson['api_key']);
  }
}
