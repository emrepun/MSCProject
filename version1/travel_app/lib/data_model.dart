import 'dart:convert';
import 'dart:io';


class Data {
  final int age;
  final int budget;
  final String season;

  Data(this.age, this.budget, this.season);

//  factory Data.fromJson(Map<String, dynamic> json) {
//    return Data(
//      age: json['age'],
//      budget: json['budget'],
//      season: json['season'],
//    );
//  }

  Map toMap() {
    var map = new Map<String, dynamic>();
    map["userId"] = '123';
    map["title"] = 'lalalala';
    map["body"] = 'bigbig';

    return map;
  }

  Map<String, dynamic> toJson() => _itemToJson(this);

}

Map<String, dynamic> _itemToJson(Data instance) {
  return <String, dynamic>{
    'age': instance.age,
    'budget': instance.budget,
    'season': instance.season,
  };
}